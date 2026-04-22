# Social-to-Lead Agentic Workflow

This project implements a conversational AI agent for a fictional SaaS product (AutoStream). The agent can answer product-related queries, identify high-intent users, and capture leads through a structured conversation flow.

## Features

* Intent detection (greeting, pricing, high-intent)
* Knowledge-based responses using a local JSON file
* Lead capture workflow for interested users
* Simple state handling for conversation flow

## How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the application:
   python main.py

## Architecture

The system is designed in a modular way. The agent logic is handled in `agent.py`, while `utils.py` manages data loading and formatting. A local JSON file is used as a knowledge base to simulate RAG-style retrieval.

Intent detection is handled using keyword-based logic, and a simple state flag is used to track when a user becomes high-intent and trigger the lead capture flow.

## WhatsApp Integration (Approach)

To integrate this agent with WhatsApp, we can use Twilio’s WhatsApp API. Incoming messages can be routed to a backend endpoint (Flask/FastAPI), where this agent logic can process the input and generate a response. The response can then be sent back to the user through Twilio’s messaging service.

## Demo

A demo video is included showing:

* Product query handling
* Intent detection
* Lead capture workflow
