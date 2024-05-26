import streamlit as st
import pandas as pd
import numpy as np
import pickle
from io import BytesIO

# Load the pre-trained model
with open('models/credit_risk.sav', 'rb') as file: 
    model = pickle.load(file)

st.header("AI-Driven Predictive Credit Risk Engine")
st.caption("This tool predicts the credit risk categories for loan applicants based on their financial and personal data")


# Adding a sidebar with detailed information
st.sidebar.header(":orange[Predictive Credit Risk Engine]")
st.sidebar.caption("""This powerful tool leverages advanced machine learning algorithms to predict the credit risk categories for loan applicants based on their financial and personal data. It provides a clear and intuitive way to assess and manage credit risk, helping you make informed lending decisions.

Make data-driven decisions with confidence using our AI-Driven Predictive Credit Risk Engine!
""")




# Instructions for use
st.markdown("""
#### Instructions for Use:
1. Upload an Excel file with the required features listed on Kaggle.
2. Download the processed file with the predictions.
3. The `Approved_Flag` column in the processed file indicates the credit risk category:
    - `P1`: Best
    - `P2`: Second best
    - `P3`: Third best
    - `P4`: Last
4. Business decisions based on risk appetite:
    - **Low Risk Appetite**: Provide loan to `P1` only.
    - **High Risk Appetite**: Provide loan to `P1`, `P2`, and `P3`.
    - **Severely High Risk Appetite**: Provide loan to `P1`, `P2`, `P3`, and `P4`.
""")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel file to get started", type=["xlsx"])

if uploaded_file:
    # Read the uploaded Excel file
    a3 = pd.read_excel(uploaded_file)

    cols_in_df = list(a3.columns)
    if 'Approved_Flag' in cols_in_df:
        cols_in_df.remove('Approved_Flag')

    df_unseen = a3[cols_in_df]

    # Encoding categorical features
    # EDUCATION encoding
    education_mapping = {
        'SSC': 1,
        '12TH': 2,
        'GRADUATE': 3,
        'UNDER GRADUATE': 3,
        'POST-GRADUATE': 4,
        'OTHERS': 1,
        'PROFESSIONAL': 3
    }
    if 'EDUCATION' in df_unseen.columns:
        df_unseen['EDUCATION'] = df_unseen['EDUCATION'].map(education_mapping).astype(int)

    # One-hot encoding
    categorical_features = ['MARITALSTATUS', 'GENDER', 'last_prod_enq2', 'first_prod_enq2']
    existing_features = [col for col in categorical_features if col in df_unseen.columns]

    if existing_features:
        df_encoded_unseen = pd.get_dummies(df_unseen, columns=existing_features)
    else:
        df_encoded_unseen = df_unseen.copy()

    # Ensuring all required columns are present after encoding
    required_columns = model.feature_names_in_  # Assuming the model has an attribute for feature names
    for col in required_columns:
        if col not in df_encoded_unseen.columns:
            df_encoded_unseen[col] = 0

    df_encoded_unseen = df_encoded_unseen[required_columns]  # Aligning the order of columns

    # Predicting with the model
    y_pred_unseen = model.predict(df_encoded_unseen)

    # Decode predictions to P1, P2, P3, P4
    prediction_mapping = {0: 'P1', 1: 'P2', 2: 'P3', 3: 'P4'}
    a3['Approved_Flag'] = [prediction_mapping[pred] for pred in y_pred_unseen]

    # Button to download the processed file
    output = BytesIO()
    a3.to_excel(output, index=False)
    output.seek(0)

    st.download_button(label="Download Processed File",
                       data=output,
                       file_name="Final_Prediction.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
st.caption("[Check out the Credit Risk Engine and Data on Kaggle for more details](https://www.kaggle.com/code/saurabhbadole/predictive-credit-risk-modeling)")



