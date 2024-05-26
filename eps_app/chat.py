import os
from openai import OpenAI

def get_gpt_analysis(params, eps_predicted):
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.environ.get("NVIDIA_API_KEY")
    )
    
    input_text = f"Generate a detailed analysis and synthesis of predicted EPS (Earning per share) given ROCE (%) {params['ROCE (%)']} CASA (%) {params['CASA (%)']} Return on Equity / Networth (%) {params['Return on Equity / Networth (%)']} Non-Interest Income/Total Assets (%) {params['Non-Interest Income/Total Assets (%)']} Operating Profit/Total Assets (%) {params['Operating Profit/Total Assets (%)']} Operating Expenses/Total Assets (%) {params['Operating Expenses/Total Assets (%)']} Interest Expenses/Total Assets (%) {params['Interest Expenses/Total Assets (%)']} Face_value {params['Face_value']}. The model predicted EPS_Predicted (Rs.) {eps_predicted}."
    
    chat_completion = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": input_text,
            },
            {
                "role": "system",
                "content": "5 to 7 SENTENCES MAX GET TO THE POINTWISE NO FLUFF",
            },
        ],
        temperature=0.5,
        top_p=0.5,
        max_tokens=1024,
        stream=False
    )
    
    return chat_completion.choices[0].message.content
