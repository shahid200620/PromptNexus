import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_intent(message: str):

    prompt = f"""
Classify the user's intent.

Choose one label from:
code
data
writing
career
unclear

Respond ONLY with JSON.

Example:
{{"intent":"code","confidence":0.9}}

User message:
{message}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You classify user intent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        result = json.loads(content)

        return result

    except Exception as e:
        print("Classifier error:", e)
        return {"intent": "unclear", "confidence": 0.0}