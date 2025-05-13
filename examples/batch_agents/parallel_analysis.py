"""
Batch Agent Processing Example

This example demonstrates how to run multiple agents in parallel to perform
different analysis tasks simultaneously.
"""

import asyncio
from swarms_client import SwarmsClient


async def main():
    # Initialize the client
    async with SwarmsClient() as client:
        # Define multiple agents for different tasks
        agents = [
            {
                "agent_name": "sentiment_analyzer",
                "task": "Analyze the sentiment of: 'Great product, highly recommended!'",
                "model_name": "gpt-4",
                "temperature": 0.7,
                "max_tokens": 500,
            },
            {
                "agent_name": "language_translator",
                "task": "Translate to French: 'Hello, how are you today?'",
                "model_name": "gpt-4",
                "temperature": 0.3,
                "max_tokens": 500,
            },
            {
                "agent_name": "code_reviewer",
                "task": "Review this code: 'def add(a,b): return a+b'",
                "model_name": "gpt-4",
                "temperature": 0.5,
                "max_tokens": 1000,
            },
        ]

        # Run all agents in parallel
        results = await client.run_agent_batch(agents)

        # Process results
        for i, result in enumerate(results):
            print(f"\nAgent {i+1} ({agents[i]['agent_name']}) Response:")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
