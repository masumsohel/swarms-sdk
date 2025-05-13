"""
Single Agent Example

This example demonstrates how to run a single agent with various configurations.
"""

import asyncio
import os
from swarms_client import SwarmsClient


async def main():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        # Define tools for the agent (optional)
        tools = [
            {
                "name": "search",
                "description": "Search the internet for information",
                "parameters": {"query": "string"},
            }
        ]

        try:
            # Run a single agent
            result = await client.run_agent(
                agent_name="research_assistant",
                task="Research the latest developments in quantum computing",
                model_name="gpt-4",
                temperature=0.7,
                max_tokens=2000,
                system_prompt="You are an expert research assistant specializing in quantum computing.",
                description="A research assistant that helps gather and analyze information",
                auto_generate_prompt=True,
                role="researcher",
                max_loops=1,
                tools_dictionary=tools,
            )
            print("Agent Result:", result)

        except Exception as e:
            print(f"Error running agent: {e}")


if __name__ == "__main__":
    asyncio.run(main())
