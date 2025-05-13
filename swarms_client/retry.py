"""
Retry handler module for Swarms API client.

This module provides retry functionality with exponential backoff for API requests.
"""

import asyncio
import random
from typing import Callable, Optional, Set, TypeVar, Any
from loguru import logger

from .config import SwarmsConfig

T = TypeVar("T")


class RetryHandler:
    """Handles retry logic with exponential backoff for API requests."""

    def __init__(
        self,
        max_retries: int = SwarmsConfig.DEFAULT_MAX_RETRIES,
        retry_delay: int = SwarmsConfig.DEFAULT_RETRY_DELAY,
        max_retry_delay: int = SwarmsConfig.DEFAULT_MAX_RETRY_DELAY,
        retry_on_status: Optional[Set[int]] = None,
        jitter: bool = True,
    ):
        """
        Initialize retry handler.

        Args:
            max_retries (int): Maximum number of retry attempts
            retry_delay (int): Initial delay between retries in seconds
            max_retry_delay (int): Maximum delay between retries in seconds
            retry_on_status (Optional[Set[int]]): HTTP status codes to retry on
            jitter (bool): Whether to add random jitter to retry delays
        """
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.max_retry_delay = max_retry_delay
        self.retry_on_status = retry_on_status or set(
            SwarmsConfig.DEFAULT_RETRY_ON_STATUS
        )
        self.jitter = jitter

    def calculate_delay(self, attempt: int) -> float:
        """
        Calculate delay for current retry attempt with exponential backoff.

        Args:
            attempt (int): Current retry attempt number

        Returns:
            float: Delay in seconds
        """
        delay = min(self.retry_delay * (2 ** (attempt - 1)), self.max_retry_delay)

        if self.jitter:
            delay *= 0.5 + random.random()

        return delay

    async def execute_with_retry(
        self, func: Callable[..., T], *args: Any, **kwargs: Any
    ) -> T:
        """
        Execute function with retry logic.

        Args:
            func (Callable): Function to execute
            *args: Positional arguments for func
            **kwargs: Keyword arguments for func

        Returns:
            T: Function result

        Raises:
            Exception: If all retries fail
        """
        last_exception = None

        for attempt in range(1, self.max_retries + 2):  # +2 for initial try
            try:
                return await func(*args, **kwargs)

            except Exception as e:
                last_exception = e

                # Check if we should retry based on the exception
                if hasattr(e, "status") and e.status not in self.retry_on_status:
                    raise

                if attempt > self.max_retries:
                    logger.error(f"Max retries ({self.max_retries}) exceeded")
                    raise

                delay = self.calculate_delay(attempt)
                logger.warning(
                    f"Attempt {attempt} failed: {str(e)}. "
                    f"Retrying in {delay:.2f} seconds..."
                )

                await asyncio.sleep(delay)

        # This should never be reached due to the raise in the loop
        raise last_exception if last_exception else Exception("Retry failed")
