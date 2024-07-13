from crewai import Agent
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from tools.browser_tools import ScrapingAnt
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
import os
# from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.tools import YahooFinanceNewsTool

from dotenv import load_dotenv
load_dotenv()

## call the LLM model

llm=ChatNVIDIA(model="meta/llama3-70b-instruct",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("NVIDIA_API_KEY"),
                           top_p=0.5,
                           max_tokens=512,
                           stream=False
                        )


class StockAnalysisAgents(object):
    def financial_analyst(self):
        return Agent(
            role='The Best Financial Analyst',
            goal="""Impress all customers with your financial data 
                    and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
                         lots of expertise in stock market analysis and investment
                         strategies that is working for a super important customer.""",
            verbose=True,
            tools=[
                ScrapingAnt.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
            ],
            llm=llm,
            allow_delegation=True
        )

    def research_analyst(self):
        return Agent(
            role='Staff Research Analyst',
            goal="""Be the best at gathering and interpreting data, and amaze
                    your customer with it""",
            backstory="""Known as the BEST research analyst, you're
                         skilled in sifting through news, company announcements, 
                         and market sentiments. Now you're working on a super 
                         important customer""",
            verbose=True,
            tools=[
                ScrapingAnt.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool()
            ],
            llm=llm,
            allow_delegation=True
        )

    def investment_advisor(self):
        return Agent(
            role='Private Investment Advisor',
            goal="""Impress your customers with thorough analyses of stocks
                    and complete investment recommendations""",
            backstory="""You're the most experienced investment advisor
                         and you combine various analytical insights to formulate
                         strategic investment advice. You are now working for
                         a super important customer you need to impress.""",
            verbose=True,
            tools=[
                ScrapingAnt.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool()
            ],
            llm=llm,
            allow_delegation=True
        )
