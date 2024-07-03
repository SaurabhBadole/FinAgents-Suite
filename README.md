# FinAgents Suite🕵🏻

Welcome to FinAgents Suite, your ultimate financial decision-making platform. Our suite of advanced tools helps you derive strategic Investment plans, assess Credit Risk, and forecast Earnings Per Share (EPS) with confidence. Our sophisticated multi-agent system leverages advanced machine learning algorithms and large language models (LLMs) to provide precise and actionable financial insights.

## Overview

The FinAgents Suite is designed to provide comprehensive Financial Analysis and decision-making capabilities through various modules:![FinAgents_Suite](https://github.com/SaurabhBadole/FinAgents-Suite/assets/132877393/e442eeb3-a20e-4c2d-ae29-250cb0d1d062)



### MultiAgent Finance Consultant🔍

Enter any company name listed in the stock market (in Ticker) to derive strategic investment plans. Our team of multi-agents combines the expertise of a Research Analyst, Financial Analyst, and Investment Advisor, who work collaboratively to analyze and synthesise data, ensuring you receive comprehensive and reliable investment strategies with the best-informed decisions.

### AI-Driven Predictive Credit Risk Engine

This tool predicts the credit risk categories for loan applicants based on their financial and personal data. Using advanced machine learning algorithms, it provides a clear and intuitive way to assess and manage credit risk, helping you make informed lending decisions. Make data-driven decisions with confidence using our AI-Driven Predictive Credit Risk Engine!

### Investment Decisions through EPS Forecasting

Predict the Earnings Per Share (EPS) for banks using key financial indicators. This tool provides an AI-generated analysis to offer deeper insights into the financial health of banks and performance-based suggestions.

## Features

- **MultiAgent Finance Consultant:** Strategic Investment planning with a team of multi-agents combining the expertise of a Research Analyst, Financial Analyst, and Investment Advisor.![App_interface](https://github.com/SaurabhBadole/FinAgents-Suite/assets/132877393/2c27e7f5-5165-4796-a223-420ab2f11b9c)

  - **FinAgents Conversations:** these are the interactions where multiple autonomous agents (which could be software agents, robots, or virtual characters) communicate and collaborate to achieve specific goals.![FinAgents_conversation](https://github.com/SaurabhBadole/FinAgents-Suite/assets/132877393/b25d215d-b75d-4f3b-875a-c3fb56244307)


- **AI-Driven Predictive Credit Risk Engine:** Assess and manage credit risk with advanced ML algorithms.![Credit_Risk](https://github.com/SaurabhBadole/FinAgents-Suite/assets/132877393/51484eee-19d4-45c1-8a6a-8ca1a8d69715)

- **EPS Forecasting:** Predict EPS for banks using financial indicators and obtain an analysis and synthesis of the data.![EPS_Forecaster](https://github.com/SaurabhBadole/FinAgents-Suite/assets/132877393/0aefcfd5-19ad-46ec-8517-05735037b5c8)



## Getting Started

### Prerequisites

- Python 3.8+
- Install dependencies from `requirements.txt`
- Obtain API keys for external services (ScrapingAnt, Serper, NVIDIA)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SaurabhBadole/FinAgents-Suite.git
    cd FinAgents-Suite
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your environment variables by creating a `.env` file in the root directory and adding your API keys:
    ```sh
    NVIDIA_API_KEY=<your_nvidia_api_key>                  #https://build.nvidia.com/explore/discover#llama3-70b
    SERPER_API_KEY=<your_serper_api_key>                  #https://serper.dev/
    SCRAPINGANT_API_KEY=<your_scrapingant_api_key>        #https://app.scrapingant.com/
    ```

### Running the Application

Run the main file to start the application:
```sh
streamlit run FinAgents_Suite.py
```



## Project Structure

Here's an overview of the project's structure:
```
FinAgents_Suite/
├── eps_app/
│   ├── __pycache__/
│   ├── __init__.py          # Initializes the EPS application module.
│   ├── chat.py              # Contains the chat functionality for user interactions.
│   └── model.py             # Implements the model for EPS forecasting.
├── models/
│   ├── credit_risk.sav      # Pre-trained model for credit risk assessment.
│   └── eps_xgboost.sav      # Pre-trained XGBoost model for EPS forecasting.
├── pages/
│   ├── 1_MultiAgent_Finance_Consultant.py  # Streamlit page for MultiAgent Finance Consultant.
│   ├── 2_EPS_Forecaster.py                # Streamlit page for EPS Forecaster.
│   └── 3_Predictive_Credit_Risk.py        # Streamlit page for Predictive Credit Risk Engine.
├── tools/
│   ├── __pycache__/
│   ├── browser_tools.py     # Contains tools for web scraping and summarization using ScrapingAnt and LLMs.
│   ├── calculator_tools.py  # Provides a tool for mathematical calculations.
│   └── search_tools.py      # Implements internet search functionalities using Serper API.
├── venv/                    # Virtual environment for the project.
├── .env                     # Environment variables for API keys and other configurations.
├── agents.py                # Defines various agents like financial analyst, research analyst, and investment advisor. These agents use tools like ScrapingAnt, Serper API, and Yahoo Finance for data analysis.
├── FinAgents_Suite.py       # Main Streamlit interface to access the whole app.
├── README.md                # Project's README file.
├── requirements.txt         # Lists all the dependencies required for the project.
└── tasks.py                 # Contains predefined tasks for stock analysis, financial analysis, filings analysis, and investment recommendations. Each task leverages the multi-agent system for comprehensive analysis.
```

### Detailed Description of Files

- **eps_app/**
  - **__init__.py**:
    - Initializes the EPS application module, setting up the necessary imports and configurations for the other files within the `eps_app` directory.
  - **chat.py**:
    - Contains the chat functionality for user interactions within the EPS application. It manages the conversation flow and integrates with the model to provide EPS forecasts based on user inputs.
  - **model.py**:
    - Implements the model for EPS forecasting. It includes the logic for loading pre-trained models, processing input data, and generating EPS predictions.

- **models/**
  - **credit_risk.sav**:
    - Pre-trained model for credit risk assessment. This model is used by the Predictive Credit Risk Engine to evaluate the creditworthiness of loan applicants based on their financial and personal data.
  - **eps_xgboost.sav**:
    - Pre-trained XGBoost model for EPS forecasting. This model is utilized by the EPS Forecaster tool to predict Earnings Per Share for banks using key financial indicators.

- **pages/**
  - **1_MultiAgent_Finance_Consultant.py**:
    - Streamlit page for the MultiAgent Finance Consultant tool. This file sets up the user interface and integrates the functionalities of the research analyst, financial analyst, and investment advisor agents to provide strategic investment plans.
  - **2_EPS_Forecaster.py**:
    - Streamlit page for the EPS Forecaster tool. It presents the interface for users to input financial data and receive EPS predictions generated by the pre-trained model.
  - **3_Predictive_Credit_Risk.py**:
    - Streamlit page for the Predictive Credit Risk Engine. This file provides the interface for assessing the credit risk of loan applicants, utilizing the pre-trained credit risk model.

- **tools/**
  - **browser_tools.py**:
    - Contains tools for web scraping and summarization using ScrapingAnt and LLMs. It enables the scraping of website content, partitioning HTML elements, and summarizing the extracted data.
  - **calculator_tools.py**:
    - Provides a tool for mathematical calculations. This utility can perform basic arithmetic operations and is used across various components for calculations.
  - **search_tools.py**:
    - Implements internet search functionalities using the Serper API. It includes tools for general web searches and news-specific searches, returning relevant results for user queries.

- **venv/**:
  - Virtual environment for the project, containing all the necessary dependencies and packages required for running the FinAgents Suite application.

- **.env**:
  - Stores API keys and other environment variables. This file ensures that sensitive information, such as API credentials, is securely managed and not hard-coded within the application code.

- **agents.py**:
  - Defines various agents like the financial analyst, research analyst, and investment advisor. These agents use tools like ScrapingAnt, Serper API, and Yahoo Finance for data analysis and generating comprehensive investment recommendations.

- **FinAgents_Suite.py**:
  - Main Streamlit interface to access the whole app. This file sets up the overall layout, integrates different modules, and provides a seamless user experience for interacting with the FinAgents Suite tools.

- **README.md**:
  - Project's README file. It contains a detailed introduction, overview of each tool, features, getting started instructions, project structure, detailed descriptions of files, contributing guidelines, license information, acknowledgements, and contact details.

- **requirements.txt**:
  - Lists all the dependencies required for the project. This file ensures that all the necessary Python packages are installed for the application to run smoothly.

- **tasks.py**:
  - Contains predefined tasks for stock analysis, financial analysis, filings analysis, and investment recommendations. Each task leverages the multi-agent system for comprehensive analysis, ensuring that users receive well-informed and data-driven insights.


## Acknowledgements
Special thanks to all contributors and the open-source community for their invaluable support.
- [Crew AI](https://www.crewai.com/)
- [Streamlit](https://streamlit.io/)
- [NVIDIA](https://www.nvidia.com/)
- [LangChain](https://www.langchain.com/) [Yahoo Finance](https://python.langchain.com/v0.2/docs/integrations/tools/yahoo_finance_news/)
- [Serper](https://serper.dev/)
- [Scrapping Ant](https://app.scrapingant.com/dashboard)



## License
This project is licensed under the [MIT License](https://github.com/SaurabhBadole/FinAgents-Suite?tab=MIT-1-ov-file#) - see the LICENSE file for details.


## Contributing
Contributions are welcome! Please extend your contributions by forking the repository and submitting pull requests to contribute.


## Contact
For any queries or further information, please contact us at [Saurabh Khushal Badole](saurabhbadole25.98@gmail.com)

For access to the private AWS ECR and Docker repository for project demo/trial, please reach out via same contact window above.
