"""
Advanced Autonomous Research Platform Example

This example demonstrates an advanced use case that combines multiple features
of the Swarms API to create an autonomous research platform that can:
1. Process multiple research topics in parallel
2. Use specialized agents for different aspects of research
3. Coordinate between different swarms
4. Handle error recovery and logging
"""

import asyncio
import json
from typing import List, Dict, Any
from swarms_client import SwarmsClient


class ResearchTopic:
    def __init__(self, title: str, description: str, keywords: List[str]):
        self.title = title
        self.description = description
        self.keywords = keywords


class AutonomousResearchPlatform:
    def __init__(self, api_key: str = None):
        self.client = SwarmsClient(api_key=api_key)
        self.active_swarms: Dict[str, Dict] = {}
        self.results: Dict[str, Any] = {}

    async def create_research_swarm(self, topic: ResearchTopic) -> Dict[str, Any]:
        """Create a specialized research swarm for a topic."""
        swarm = await self.client.create_swarm(
            name=f"research_{topic.title.lower().replace(' ', '_')}",
            task=f"Conduct comprehensive research on: {topic.description}",
            description=f"Research team for {topic.title}",
            agents=[
                {
                    "agent_name": "initial_researcher",
                    "model_name": "gpt-4",
                    "role": "researcher",
                    "task": "Perform initial research and identify key areas to explore",
                },
                {
                    "agent_name": "fact_checker",
                    "model_name": "gpt-4",
                    "role": "validator",
                    "task": "Verify facts and cross-reference information",
                },
                {
                    "agent_name": "insight_generator",
                    "model_name": "gpt-4",
                    "role": "analyst",
                    "task": "Generate insights and identify patterns",
                },
                {
                    "agent_name": "report_compiler",
                    "model_name": "gpt-4",
                    "role": "writer",
                    "task": "Compile findings into a structured report",
                },
            ],
            max_loops=3,
            swarm_type="research",
            service_tier="standard",
        )
        return swarm

    async def process_topics(self, topics: List[ResearchTopic]):
        """Process multiple research topics in parallel."""
        # Create swarms for each topic
        swarms = []
        for topic in topics:
            swarm = await self.create_research_swarm(topic)
            swarms.append(swarm)
            self.active_swarms[topic.title] = swarm

        # Run all swarms in parallel
        results = await self.client.run_swarm_batch(swarms)

        # Process and store results
        for topic, result in zip(topics, results):
            self.results[topic.title] = result

        # Get detailed logs for each swarm
        for topic, swarm in self.active_swarms.items():
            logs = await self.client.get_swarm_logs(swarm["swarm_id"])
            self.results[topic.title]["logs"] = logs

    def save_results(self, output_file: str):
        """Save research results to a file."""
        with open(output_file, "w") as f:
            json.dump(self.results, f, indent=2)

    async def close(self):
        """Clean up resources."""
        self.client.close()


async def main():
    # Define research topics
    topics = [
        ResearchTopic(
            title="AI in Healthcare",
            description="Research the current applications and future potential of AI in healthcare",
            keywords=[
                "artificial intelligence",
                "healthcare",
                "medical diagnosis",
                "treatment",
            ],
        ),
        ResearchTopic(
            title="Sustainable Energy",
            description="Analyze trends and innovations in sustainable energy technologies",
            keywords=[
                "renewable energy",
                "sustainability",
                "clean tech",
                "green energy",
            ],
        ),
        ResearchTopic(
            title="Future of Work",
            description="Investigate how AI and automation are reshaping the workforce",
            keywords=["remote work", "automation", "workplace", "future skills"],
        ),
    ]

    # Initialize the research platform
    platform = AutonomousResearchPlatform()

    try:
        # Process all research topics
        await platform.process_topics(topics)

        # Save results
        platform.save_results("research_results.json")

        # Print summary
        print("\nResearch Summary:")
        for topic_title, result in platform.results.items():
            print(f"\n{topic_title}:")
            print(f"Number of insights: {len(result.get('insights', []))}")
            print(f"Number of sources: {len(result.get('sources', []))}")
            print("Key findings:", result.get("summary", "No summary available"))

    except Exception as e:
        print(f"Error during research: {str(e)}")
    finally:
        await platform.close()


if __name__ == "__main__":
    asyncio.run(main())
