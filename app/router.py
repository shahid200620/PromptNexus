import os
from openai import OpenAI
from dotenv import load_dotenv
from app.prompts import PROMPTS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def route_and_respond(message: str, intent_data: dict):

    intent = intent_data.get("intent")
    confidence = intent_data.get("confidence")

    if intent == "unclear":
        return "I am not sure what kind of help you need. Are you asking about coding, data analysis, writing improvement, or career advice?"

    system_prompt = PROMPTS.get(intent)

    if not system_prompt:
        return "I could not determine the correct expert to handle your request."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content