from app.classifier import classify_intent
from app.router import route_and_respond

def main():

    print("Prompt Router CLI")
    print("Type 'exit' to quit")

    while True:

        message = input("\nEnter message: ")

        if message.lower() == "exit":
            break

        intent_data = classify_intent(message)

        intent = intent_data.get("intent")
        confidence = intent_data.get("confidence")

        print("\nIntent:", intent)
        print("Confidence:", confidence)

        response = route_and_respond(message, intent_data)

        print("\nResponse:")
        print(response)

if __name__ == "__main__":
    main()