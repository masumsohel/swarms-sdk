"""
Basic Single Agent Example

This example demonstrates how to use a single agent to perform a simple task
using the Swarms API client.
"""

import asyncio
from swarms_client import SwarmsClient


async def main():
    # Initialize the client
    async with SwarmsClient() as client:
        # Run a single agent for text analysis
        result = await client.run_agent(
            agent_name="text_analyzer",
            task="Analyze the sentiment and key themes in the following text: "
            "'The new AI developments have shown promising results in healthcare, "
            "though some experts express concerns about privacy implications.'",
            model_name="gpt-4",
            temperature=0.7,
            max_tokens=1000,
        )

        print("Agent Response:")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
