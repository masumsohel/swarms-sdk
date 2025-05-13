"""
Basic Client Example

This example demonstrates how to initialize the Swarms client and check API health.
"""

import asyncio
import os
from swarms_client import SwarmsClient


async def main():
    # Initialize the client
    # You can either pass the API key directly or set it as an environment variable
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(
        api_key=api_key, max_retries=3, timeout=30, max_concurrent_requests=5
    ) as client:
        # Check API health
        try:
            health_status = await client.get_health()
            print("API Health Status:", health_status)
        except Exception as e:
            print(f"Error checking health: {e}")


if __name__ == "__main__":
    asyncio.run(main())
