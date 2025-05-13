"""
Multi-Agent Collaborative Research System

This example demonstrates how to create a swarm of agents that work together
to perform comprehensive research on a topic, with different agents handling
different aspects of the research process.
"""

import asyncio
from swarms_client import SwarmsClient


async def main():
    # Initialize the client
    async with SwarmsClient() as client:
        # Create a research swarm with multiple specialized agents
        research_swarm = await client.create_swarm(
            name="research_team",
            task="Research and analyze the impact of artificial intelligence on healthcare",
            description="A collaborative research team analyzing AI in healthcare",
            agents=[
                {
                    "agent_name": "literature_reviewer",
                    "model_name": "gpt-4",
                    "role": "researcher",
                    "task": "Review and summarize recent academic papers on AI in healthcare",
                },
                {
                    "agent_name": "data_analyst",
                    "model_name": "gpt-4",
                    "role": "analyst",
                    "task": "Analyze trends and patterns in the research findings",
                },
                {
                    "agent_name": "ethics_evaluator",
                    "model_name": "gpt-4",
                    "role": "evaluator",
                    "task": "Evaluate ethical implications and concerns",
                },
                {
                    "agent_name": "report_writer",
                    "model_name": "gpt-4",
                    "role": "writer",
                    "task": "Compile findings into a comprehensive report",
                },
            ],
            max_loops=3,  # Allow multiple iterations for refinement
            swarm_type="collaborative",
            service_tier="standard",
        )

        # Run the swarm
        result = await client.run_swarm(research_swarm["swarm_id"])
        print("\nResearch Swarm Results:")
        print(result)

        # Get swarm logs to see the collaboration process
        logs = await client.get_swarm_logs(research_swarm["swarm_id"])
        print("\nCollaboration Process Logs:")
        for log in logs:
            print(f"\n{log['agent_name']}: {log['message']}")


if __name__ == "__main__":
    asyncio.run(main())
