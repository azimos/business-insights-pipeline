import os
from openai import OpenAI

def generate_insights(df):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    anomalies = df[df["anomaly"] == -1]

    if anomalies.empty:
        return "No significant anomalies detected."

    prompt = f"""
    You are analyzing small business sales data.

    Here are unusual revenue patterns:
    {anomalies.to_string()}

    Explain:
    - What is happening
    - Possible causes
    - Suggested actions
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
