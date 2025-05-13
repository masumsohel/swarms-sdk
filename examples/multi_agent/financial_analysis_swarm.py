"""
Financial Analysis Swarm Example

This example demonstrates a multi-agent swarm for comprehensive financial analysis,
using the provided example as a base and incorporating tools.
"""

import asyncio
import os
import json
from swarms_client import SwarmsClient
from swarms_client.models import AgentSpec
from examples.tools.tools import SwarmTools


async def run_financial_analysis_swarm():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    # Example financial data
    financial_data = """
    MARKET ANALYSIS DATA
    Asset: S&P 500 E-mini Futures
    Date Range: Last 30 days
    
    PRICE DATA:
    - Current Price: 4,780
    - 30-day High: 4,850
    - 30-day Low: 4,680
    - Average Daily Volume: 2.1M contracts
    
    VOLATILITY METRICS:
    - 30-day Historical Volatility: 15.2%
    - VIX Index: 14.5
    - Implied Volatility (ATM): 16.1%
    
    CORRELATION DATA:
    - Correlation with US 10Y Yields: -0.35
    - Correlation with EUR/USD: 0.28
    - Correlation with Gold: -0.12
    """

    async with SwarmsClient(api_key=api_key) as client:
        # Define agents with their specialized roles and tools
        agents = [
            AgentSpec(
                agent_name="Data Analyzer",
                description="Analyzes financial data and identifies patterns",
                system_prompt="""You are a quantitative data analyst specializing in financial markets.
                Use the search tool to gather additional market data and the code executor for analysis.
                Focus on identifying patterns, trends, and potential trading opportunities.""",
                model_name="gpt-4",
                role="analyst",
                max_tokens=4000,
                temperature=0.5,
                tools_dictionary=[SwarmTools.search_tool(), SwarmTools.code_executor()],
            ),
            AgentSpec(
                agent_name="Risk Analyst",
                description="Calculates risk metrics and assesses exposures",
                system_prompt="""You are an expert risk analyst responsible for evaluating market risks.
                Use the code executor to calculate risk metrics and create risk models.
                Focus on VaR calculations, stress testing, and risk factor analysis.""",
                model_name="gpt-4",
                role="risk_manager",
                max_tokens=4000,
                temperature=0.5,
                tools_dictionary=[SwarmTools.code_executor()],
            ),
            AgentSpec(
                agent_name="Strategy Validator",
                description="Reviews analysis and validates conclusions",
                system_prompt="""You are a senior quantitative strategist.
                Review the analyses from other agents and validate their conclusions.
                Use the code executor to verify calculations and test robustness.""",
                model_name="gpt-4",
                role="validator",
                max_tokens=4000,
                temperature=0.5,
                tools_dictionary=[SwarmTools.code_executor()],
            ),
        ]

        try:
            # Create and run the financial analysis swarm
            result = await client.create_swarm(
                name="Financial Analysis Swarm",
                task=f"""Analyze the following financial data and provide comprehensive analysis:
                {financial_data}
                
                Provide:
                1. Key market patterns and trends
                2. Risk metrics and exposure analysis
                3. Trading strategy recommendations
                4. Implementation considerations
                5. Risk management guidelines""",
                agents=agents,
                description="A swarm for comprehensive financial market analysis",
                max_loops=1,
                swarm_type="SequentialWorkflow",
                service_tier="standard",
            )

            print("\nFinancial Analysis Swarm Results:")
            print(json.dumps(result, indent=2))
            return result

        except Exception as e:
            print(f"Error running financial analysis swarm: {e}")
            raise


if __name__ == "__main__":
    asyncio.run(run_financial_analysis_swarm())
