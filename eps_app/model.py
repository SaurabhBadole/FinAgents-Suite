import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the model from the pickle file
with open('models/eps_xgboost.sav', 'rb') as file:  
    model = pickle.load(file)

# Function to preprocess input and predict EPS
def predict_eps(params):
    df = pd.DataFrame([params], columns=[
        'ROCE (%)', 'CASA (%)', 'Return on Equity / Networth (%)',
        'Non-Interest Income/Total Assets (%)', 'Operating Profit/Total Assets (%)',
        'Operating Expenses/Total Assets (%)', 'Interest Expenses/Total Assets (%)', 'Face_value'
    ])
    
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(df)
    prediction = model.predict(x_scaled)
    
    return prediction[0]
