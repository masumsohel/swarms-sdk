"""
Basic Single Agent Example

This example demonstrates how to use a single agent to perform a simple task
using the Swarms API client, showing both synchronous and asynchronous usage.
"""

import asyncio
import os
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

# Example text for analysis
SAMPLE_TEXT = (
    "The new AI developments have shown promising results in healthcare, "
    "though some experts express concerns about privacy implications."
)


def run_sync_example():
    """Run synchronous example."""
    print("\nRunning synchronous example...")

    # Initialize the client with optimized settings
    with SwarmsClient(
        api_key=os.getenv("SWARMS_API_KEY"),
        enable_cache=True,
        max_concurrent_requests=25,
        timeout=120,
        max_retries=5,
        retry_delay=0.5,
        jitter=True,
    ) as client:
        # Get available models
        models = client.get_available_models()
        print("\nAvailable Models:", models)

        # Run a single agent for text analysis
        result = client.run_agent(
            agent_name="text_analyzer",
            task=f"Analyze the sentiment and key themes in the following text: '{SAMPLE_TEXT}'",
            model_name="gpt-4",
            system_prompt="You are a helpful assistant that analyzes text and provides a summary of the sentiment and key themes.",
            temperature=0.7,
            max_tokens=1000,
        )
        print("\nSync Agent Response:")
        print(result)


async def run_async_example():
    """Run asynchronous example."""
    print("\nRunning asynchronous example...")

    # Initialize the client with optimized settings
    async with SwarmsClient(
        api_key=os.getenv("SWARMS_API_KEY"),
        enable_cache=True,
        max_concurrent_requests=25,
        timeout=120,
        max_retries=5,
        retry_delay=0.5,
        jitter=True,
    ) as client:
        # Get available models
        models = await client.async_get_available_models()
        print("\nAvailable Models:", models)

        # Run a single agent for text analysis
        result = await client.async_run_agent(
            agent_name="text_analyzer",
            task=f"Analyze the sentiment and key themes in the following text: '{SAMPLE_TEXT}'",
            model_name="gpt-4",
            system_prompt="You are a helpful assistant that analyzes text and provides a summary of the sentiment and key themes.",
            temperature=0.7,
            max_tokens=1000,
        )
        print("\nAsync Agent Response:")
        print(result)


async def run_parallel_example():
    """Run multiple agents in parallel."""
    print("\nRunning parallel example...")

    async with SwarmsClient(
        api_key=os.getenv("SWARMS_API_KEY"),
        enable_cache=True,
        max_concurrent_requests=25,
    ) as client:
        # Run multiple agents in parallel
        tasks = []
        for i in range(3):
            task = client.async_run_agent(
                agent_name=f"agent_{i}",
                task=f"Analyze part {i+1} of the text: '{SAMPLE_TEXT}'",
                model_name="gpt-4",
                temperature=0.7,
                max_tokens=1000,
            )
            tasks.append(task)

        # Wait for all agents to complete
        results = await asyncio.gather(*tasks)
        print("\nParallel Results:")
        for i, result in enumerate(results):
            print(f"\nAgent {i} Response:")
            print(result)


if __name__ == "__main__":
    # Run sync example
    run_sync_example()

    # Run async examples
    # asyncio.run(run_async_example())
    # asyncio.run(run_parallel_example())
