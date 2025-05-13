"""
Medical Analysis Swarm Example

This example demonstrates a multi-agent swarm for medical research and analysis,
incorporating search and analysis tools.
"""

import asyncio
import os
import json
from swarms_client import SwarmsClient
from swarms_client.models import AgentSpec
from examples.tools.tools import SwarmTools


async def run_medical_analysis_swarm():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        # Define specialized medical research agents
        agents = [
            AgentSpec(
                agent_name="Clinical Data Analyst",
                description="Analyzes clinical data, patient outcomes, and treatment efficacy",
                system_prompt="""You are a highly skilled Clinical Data Analyst with extensive experience in evaluating clinical trials and patient data.
                Use the search tool to gather current medical research and the code executor for statistical analysis.
                Focus on analyzing treatment outcomes, patient demographics, and clinical protocols.
                Provide evidence-based insights and identify significant patterns in the data.""",
                model_name="gpt-4",
                role="analyst",
                max_tokens=4000,
                temperature=0.5,
                tools_dictionary=[SwarmTools.search_tool(), SwarmTools.code_executor()],
            ),
            AgentSpec(
                agent_name="Medical Researcher",
                description="Researches latest medical treatments and therapies",
                system_prompt="""You are a Medical Researcher with deep knowledge of current medical literature.
                Use the search tool to investigate recent medical advances and emerging treatments.
                Focus on novel therapies, clinical trials, and treatment outcomes.
                Synthesize findings from multiple sources and evaluate their clinical significance.""",
                model_name="gpt-4",
                role="researcher",
                max_tokens=4000,
                temperature=0.5,
                tools_dictionary=[SwarmTools.search_tool()],
            ),
            AgentSpec(
                agent_name="Treatment Protocol Validator",
                description="Validates treatment protocols and recommendations",
                system_prompt="""You are a senior medical professional responsible for validating treatment protocols.
                Review the analyses and recommendations from other agents.
                Focus on safety, efficacy, and adherence to medical standards.
                Consider patient risk factors and potential contraindications.""",
                model_name="gpt-4",
                role="validator",
                max_tokens=4000,
                temperature=0.5,
                tools_dictionary=[SwarmTools.search_tool()],
            ),
        ]

        try:
            # Create and run the medical analysis swarm
            result = await client.create_swarm(
                name="Medical Analysis Swarm",
                task="""Investigate and analyze the latest advancements in cancer immunotherapy treatments.

                Focus on:
                1. Recent clinical trial results and outcomes
                2. Novel therapeutic approaches
                3. Patient response patterns
                4. Treatment efficacy metrics
                5. Safety considerations and side effects
                
                Provide a comprehensive analysis with:
                - Evidence-based findings
                - Statistical significance of results
                - Practical implementation guidelines
                - Risk-benefit assessments
                - Recommendations for clinical application""",
                agents=agents,
                description="A swarm for comprehensive medical research and analysis",
                max_loops=1,
                swarm_type="SequentialWorkflow",
                service_tier="standard",
            )

            print("\nMedical Analysis Swarm Results:")
            print(json.dumps(result, indent=2))
            return result

        except Exception as e:
            print(f"Error running medical analysis swarm: {e}")
            raise


if __name__ == "__main__":
    asyncio.run(run_medical_analysis_swarm())
