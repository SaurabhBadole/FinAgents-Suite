import streamlit as st
from crewai import Crew
from textwrap import dedent
from agents import StockAnalysisAgents
from tasks import StockAnalysisTasks
from dotenv import load_dotenv
import pdfkit

load_dotenv()

class FinancialCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        financial_analyst_agent = agents.financial_analyst()
        investment_advisor_agent = agents.investment_advisor()

        research_task = tasks.research(research_analyst_agent, self.company)
        financial_task = tasks.financial_analysis(financial_analyst_agent)
        recommend_task = tasks.recommend(investment_advisor_agent)

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent
            ],
            tasks=[
                research_task,
                financial_task,
                recommend_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result

def main():
    st.title("MultiAgent Finance Consultant🔍")
    company = st.text_input("**Enter the company name you want to research and analyze:**",help='This FinAI Consultant Analyzes Financial data, Research market trends, and provides expert Investment recommendations using advanced LLM based multi-agents.')

    # Adding a sidebar with detailed information
    st.sidebar.header(":orange[MultiAgent Finance Consultant]")
    st.sidebar.caption("""Leverage the power of a multi-agent system consisting of a **Research Analyst, Financial Analyst, and Investment Advisor** agent to derive strategic investment plans. """)
    st.sidebar.caption("""Enter the name of any stock market-listed company in Stock Ticker format, and let our team of virtual experts collaborate to provide you with the best-informed decisions. Experience the synergy of expert insights, all working together to guide your investments to success.""")



    st.sidebar.subheader("How to Use:")
    st.sidebar.caption("""
    1. **:orange[Enter Stock Ticker]**: Provide the ticker symbol of any company listed in the stock market (e.g., AAPL for Apple Inc.).
    2. **:orange[Submit]**: Click the "Analyze" button to start the analysis.
    """)

    st.sidebar.subheader("Features:")
    st.sidebar.caption("""
    - **:orange[Research Analys]t**: Gathers and summarizes recent news, press releases, and market trends.
    - **:orange[Financial Analyst]**: Examines key financial metrics like P/E ratio, EPS growth, and revenue trends.
    - **:orange[Investment Advisor]**: Synthesizes insights to provide strategic investment recommendations.
    """)

    st.sidebar.subheader("Benefits:")
    st.sidebar.caption("""
    - **:orange[Informed Decisions]**: Receive detailed reports combining qualitative and quantitative analysis.
    - **:orange[Expert Insights]**: Get guidance from virtual experts to enhance your investment strategy.
    - **:orange[Comprehensive Reports]**: Download comprehensive reports for further review and record-keeping.
    """)

    st.sidebar.subheader("Quick Tips:")
    st.sidebar.caption("""
    - Use up-to-date stock tickers for the most accurate analysis.
    - Review the detailed reports to understand the insights provided by each virtual expert.
    - Combine the insights with your own research for the best results.
    """)

    st.sidebar.subheader("Disclaimer:")
    st.sidebar.caption("""
    - **:orange[Risk Notice]**: :red[Investments are subject to market risks]. Please read all related documents carefully before investing. :red[FinAgents Suite provides analysis and recommendations based on the data available but does not guarantee returns.] Always consult with a financial advisor before making any investment decisions.
    """)



    if st.button("Analyze and Generate Report"):
        if company:
            financial_crew = FinancialCrew(company)
            result = financial_crew.run()
            
            st.markdown("## Investment Recommendations")
            st.markdown(result)
            
            if st.button("Download Report as PDF"):
                pdf = pdfkit.from_string(result, False)
                st.download_button("Download PDF", pdf, "report.pdf", "application/pdf")
        else:
            st.error("Please enter the company name that you'll like to research.")

if __name__ == "__main__":
    main()
