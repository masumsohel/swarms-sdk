"""
Configuration module for Swarms API client.

This module handles API settings, defaults, and environment configuration.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class SwarmsConfig:
    """Configuration class for Swarms API client."""

    # Default values
    DEFAULT_BASE_URL = "https://api.swarms.world"
    ALTERNATE_BASE_URL = "https://swarms-api-285321057562.us-east1.run.app"
    DEFAULT_TIMEOUT = 60
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_RETRY_DELAY = 1
    DEFAULT_MAX_RETRY_DELAY = 30
    DEFAULT_RETRY_ON_STATUS = [429, 500, 502, 503, 504]

    @staticmethod
    def get_api_key() -> Optional[str]:
        """
        Get API key from environment variables.

        Returns:
            Optional[str]: API key if found, None otherwise
        """
        return os.getenv("SWARMS_API_KEY")

    @staticmethod
    def get_base_url() -> str:
        """
        Get base URL from environment variables or use default.

        Returns:
            str: Base URL for API requests
        """
        return os.getenv("SWARMS_API_BASE_URL", SwarmsConfig.DEFAULT_BASE_URL)

    @staticmethod
    def get_timeout() -> int:
        """
        Get request timeout from environment variables or use default.

        Returns:
            int: Timeout in seconds
        """
        return int(os.getenv("SWARMS_API_TIMEOUT", SwarmsConfig.DEFAULT_TIMEOUT))

    @staticmethod
    def get_max_retries() -> int:
        """
        Get maximum retries from environment variables or use default.

        Returns:
            int: Maximum number of retries
        """
        return int(
            os.getenv("SWARMS_API_MAX_RETRIES", SwarmsConfig.DEFAULT_MAX_RETRIES)
        )

    @staticmethod
    def get_retry_delay() -> int:
        """
        Get initial retry delay from environment variables or use default.

        Returns:
            int: Retry delay in seconds
        """
        return int(
            os.getenv("SWARMS_API_RETRY_DELAY", SwarmsConfig.DEFAULT_RETRY_DELAY)
        )

    @staticmethod
    def get_max_retry_delay() -> int:
        """
        Get maximum retry delay from environment variables or use default.

        Returns:
            int: Maximum retry delay in seconds
        """
        return int(
            os.getenv(
                "SWARMS_API_MAX_RETRY_DELAY", SwarmsConfig.DEFAULT_MAX_RETRY_DELAY
            )
        )
