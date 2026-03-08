import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_intent(message: str):

    prompt = f"""
Your task is to classify the user's intent.

Choose one of these labels:
code
data
writing
career
unclear

Respond only with a JSON object in this format:
{{"intent": "label", "confidence": 0.0}}

User message:
{message}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You classify user intent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        result = json.loads(content)

        if "intent" not in result or "confidence" not in result:
            return {"intent": "unclear", "confidence": 0.0}

        return result

    except Exception:
        return {"intent": "unclear", "confidence": 0.0}