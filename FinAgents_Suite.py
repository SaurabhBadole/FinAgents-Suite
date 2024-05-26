import streamlit as st

# Main Interface
st.title("**:orange[FinAgents Suite🕵🏻]**")
st.write("""
Welcome to FinAgents Suite, your ultimate financial decision-making platform. Our suite of advanced tools helps you derive strategic Investment plans, assess Credit Risk, and forecast Earnings Per Share (EPS) with confidence.
""")


st.write(":blue-background[**👈 Click on the module listed on the side panel**]"" by  Using these modules, you can make strategic financial decisions that are data-driven and well-informed.")


# Tool 1: MultiAgent Finance Consultant
st.subheader(":blue[MultiAgent Finance Consultant🔍]")
st.write("""
:grey[Enter any company name listed in the stock market to derive strategic investment plans. Our multi-agent system, which includes a research analyst, financial analyst, and investment advisor agent, works together to provide you with the best-informed decisions.
] """)

# Tool 2: AI-Driven Predictive Credit Risk Engine
st.subheader(":blue[AI-Driven Predictive Credit Risk Engine]")
st.write("""
:grey[This tool predicts the credit risk categories for loan applicants based on their financial and personal data. Using advanced machine learning algorithms, it provides a clear and intuitive way to assess and manage credit risk, helping you make informed lending decisions. Make data-driven decisions with confidence using our AI-Driven Predictive Credit Risk Engine!]
""")

# Tool 3: EPS Forecaster
st.subheader(":blue[Investment Decisions through EPS Forecasting]")
st.write("""
:grey[Predict the Earnings Per Share (EPS) for banks using key financial indicators. This tool provides an AI-generated analysis to offer deeper insights into the financial health of banks and performance-based suggestions.]
""")



# Sidebar: Get Started and Privacy Notice
st.sidebar.subheader("Get Started")
st.sidebar.caption("""
Welcome to **FinAgents Suite**! Follow these steps to get started:

1. **Install Dependencies**: Make sure all required packages are installed.
2. **Explore Modules**: Use this side panel to navigate through different modules as per business use case.
3. **Input Data**: Enter relevant data for the selected module to get personalized financial insights.
4. **Analyze Results**: Review the generated reports and make informed financial decisions, and download reports as necessary.

For detailed instructions, refer to the [FinAgents](https://github.com/SaurabhBadole/FinAgents-Suite).
""")

st.sidebar.subheader("Privacy Notice")
st.sidebar.caption("""
We value your privacy and are committed to protecting your personal information. Here's how we handle your data:

- **Usage**: Your data is used exclusively for generating investment plans, credit risk assessments, and EPS forecasts.
- **Security**: We implement strict security measures to safeguard your information from unauthorized access.
- **No Sharing**: We do not share your data with third parties without your explicit consent.

""")

st.sidebar.subheader("Investments Risk Policy")
st.sidebar.caption("""
:red[**Investments are Subjected to Market Risk**]

Please note that all investment decisions carry inherent risks. While our tools provide advanced analysis and predictions to support your decision-making, :red[we cannot guarantee specific outcomes.] It is essential to conduct your due diligence and consider various risk factors before making any investment.

**Disclaimer**: FinAgents Suite does not take responsibility for any financial losses incurred from using the insights and recommendations provided by our tools.
""")