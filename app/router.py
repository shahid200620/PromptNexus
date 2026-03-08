import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from app.prompts import PROMPTS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LOG_FILE = "logs/route_log.jsonl"

def route_and_respond(message: str, intent_data: dict):

    intent = intent_data.get("intent")
    confidence = intent_data.get("confidence")

    if intent == "unclear":
        final_response = "I am not sure what kind of help you need. Are you asking about coding, data analysis, writing improvement, or career advice?"
    else:
        system_prompt = PROMPTS.get(intent)

        if not system_prompt:
            final_response = "I could not determine the correct expert to handle your request."
        else:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                temperature=0.4
            )

            final_response = response.choices[0].message.content

    log_entry = {
        "intent": intent,
        "confidence": confidence,
        "user_message": message,
        "final_response": final_response
    }

    with open(LOG_FILE, "a") as file:
        file.write(json.dumps(log_entry) + "\n")

    return final_response