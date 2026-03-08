# PromptNexus — LLM Powered Prompt Router for Intent Classification

## Overview

PromptNexus is a lightweight backend service that intelligently routes user requests to specialized AI personas using intent classification. Instead of using one large prompt to handle every type of query, the system first determines the user's intent and then forwards the request to an expert prompt designed specifically for that task.

This approach improves response quality, system modularity, and scalability for real-world AI applications.

The system performs a two-step workflow:

1. **Intent Classification** — A lightweight LLM call identifies the user's intent and returns a structured JSON response.
2. **Expert Routing** — Based on the detected intent, the system routes the request to a specialized AI persona to generate a focused response.

All requests are logged for observability and analysis.

---

## Features

* Intent classification using a Large Language Model
* Specialized expert prompt routing
* Structured JSON output from the classifier
* Graceful handling of malformed responses
* Logging of routing decisions and responses
* Command Line Interface for interaction
* Docker containerization for reproducible deployment

---

## System Architecture

User Message
↓
Intent Classifier (LLM Call)
↓
Intent Label + Confidence Score
↓
Router
↓
Specialized Expert Prompt
↓
Final AI Response

Each request is also logged to a JSON Lines file for traceability.

---

## Supported Intents

The classifier routes messages into one of the following expert personas:

| Intent  | Expert Persona | Description                                                      |
| ------- | -------------- | ---------------------------------------------------------------- |
| code    | Code Expert    | Provides programming solutions and technical explanations        |
| data    | Data Analyst   | Interprets data patterns and suggests insights or visualizations |
| writing | Writing Coach  | Gives feedback on clarity, tone, and structure                   |
| career  | Career Advisor | Provides actionable career guidance                              |
| unclear | Clarification  | Asks the user to clarify their request                           |

---

## Project Structure

```
PromptNexus
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── classifier.py
│   ├── router.py
│   └── prompts.py
│
├── logs
│   └── route_log.jsonl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

### Clone the Repository

```
git clone https://github.com/shahid200620/PromptNexus.git
cd PromptNexus
```

### Create Environment File

Create a `.env` file using the template:

```
cp .env.example .env
```

Add your API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## Running Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python -m app.main
```

You will see:

```
Prompt Router CLI
Type 'exit' to quit
```

Enter any message and the system will classify the intent and generate a response.

---

## Running with Docker

Build the container:

```
docker compose build
```

Start the application:

```
docker compose up
```

The CLI interface will appear inside the container.

---

## Logging

All routing decisions and responses are logged in:

```
logs/route_log.jsonl
```

Each entry contains:

```
{
  "intent": "code",
  "confidence": 0.94,
  "user_message": "how do i sort a python list",
  "final_response": "..."
}
```

This allows monitoring and debugging of routing behavior.

---

## Example Inputs

Coding request

```
how do i sort a list in python
```

Data analysis request

```
what is the average of these numbers: 12, 45, 23, 67
```

Writing improvement request

```
my writing sounds awkward can you help me improve it
```

Career advice request

```
I am preparing for a job interview any tips
```

Ambiguous request

```
hey
```

---

## Design Decisions

The system separates classification and generation into two independent steps. This design improves efficiency and response quality compared to using a single monolithic prompt.

Expert prompts are stored in a configuration structure instead of being embedded directly in business logic. This allows easy extension with additional expert personas in the future.

Error handling ensures the application does not crash if the classifier returns malformed responses.

---

## Future Improvements

* Confidence threshold routing
* Manual intent override using message prefixes
* Web interface using FastAPI or Flask
* More specialized expert personas
* Advanced analytics on routing logs

---

## Author

Shahid Mohammed

GitHub Repository
https://github.com/shahid200620/PromptNexus
