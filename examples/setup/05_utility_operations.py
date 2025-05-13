"""
Utility Operations Example

This example demonstrates how to use various utility operations like getting available models,
swarm types, and API logs.
"""

import asyncio
import os
from swarms_client import SwarmsClient


async def main():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        try:
            # Get available models
            models = await client.get_available_models()
            print("Available Models:", models)

            # Get available swarm types
            swarm_types = await client.get_swarm_types()
            print("Available Swarm Types:", swarm_types)

            # Get API logs
            api_logs = await client.get_api_logs()
            print("API Logs:", api_logs)

        except Exception as e:
            print(f"Error in utility operations: {e}")


if __name__ == "__main__":
    asyncio.run(main())
