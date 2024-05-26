import streamlit as st
from eps_app.model import predict_eps
from eps_app.chat import get_gpt_analysis

# Streamlit App
st.title("Investment Decisions through EPS Forecasting")
st.caption("This tool **predicts the Earnings Per Share (EPS)** for banks using key **Financial Indicators** and provides an **AI-generated Analysis** to provide deeper insights into the financial health and performance-based suggestions.")

st.sidebar.caption("[Explore the EPS Intelligence code Directory](https://colab.research.google.com/drive/125maAL_cEP6IPTYwHaC89Uelk2kxUF_7?usp=sharing)")
st.sidebar.header(":orange[Investment Decisions through EPS Forecasting]")
st.sidebar.subheader('Input Parameters')


params = {
    'ROCE (%)': st.sidebar.number_input('ROCE (%)', help='Return on Capital Employed, a measure of a company\'s profitability and the efficiency with which its capital is employed.'),
    'CASA (%)': st.sidebar.number_input('CASA (%)', help='Current Account Savings Account, the ratio of deposits in current and savings accounts to total deposits.'),
    'Return on Equity / Networth (%)': st.sidebar.number_input('Return on Equity / Networth (%)', help='A measure of financial performance, calculated by dividing net income by shareholders\' equity.'),
    'Non-Interest Income/Total Assets (%)': st.sidebar.number_input('Non-Interest Income/Total Assets (%)', help='Income from sources other than interest on loans, as a percentage of total assets.'),
    'Operating Profit/Total Assets (%)': st.sidebar.number_input('Operating Profit/Total Assets (%)', help='Operating profit as a percentage of total assets, indicating operational efficiency.'),
    'Operating Expenses/Total Assets (%)': st.sidebar.number_input('Operating Expenses/Total Assets (%)', help='Operating expenses as a percentage of total assets, showing cost management efficiency.'),
    'Interest Expenses/Total Assets (%)': st.sidebar.number_input('Interest Expenses/Total Assets (%)', help='Interest expenses as a percentage of total assets, indicating the cost of borrowing.'),
    'Face_value': st.sidebar.number_input('Face_value', help='The nominal or dollar value of a security stated by the issuer.')
}


if st.sidebar.button('Predict EPS and Generate AI Analysis'):
    eps_predicted = predict_eps(params)
    st.write(f"**Predicted EPS:** Rs. {eps_predicted}")

    analysis = get_gpt_analysis(params, eps_predicted)
    st.markdown(":blue-background[**FinAI EPS Forecast:**]")
    st.write(analysis)
