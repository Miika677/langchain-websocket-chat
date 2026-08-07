# LangChain WebSocket AI Agent Chat (WIP)

A **work-in-progress** mini-project exploring real-time communication between clients and a LangChain-powered AI Agent through WebSockets.

The goal of this project is to experiment with the integration of:
- Real-time WebSocket communication
- LangChain agent workflows

This project is currently in active development and is primarily a learning/experimentation project rather than a finished application.

## Current Status

**WORK IN PROGRESS**

The project is incomplete and features may change significantly as the architecture evolves.

Current focus areas:

* [x] FastAPI WebSocket communication
* [x] Basic LangChain agent integration
* [x] Tool calling experiments
* [ ] Multi-user chat handling
* [ ] Persistent chat history
* [ ] Frontend implementation

## Tech Stack

- FastAPI
- WebSockets
- LangChain (Using Gemini 2.5 Flash)
- Python

## How to Setup

**Create a .env file in the root directory:**

GOOGLE_API_KEY=your_api_key_here

**Install dependencies:**

pip install -r requirements.txt

**Run the backend:**

uvicorn backend.main:app --reload

**Test using the temporary test script:**

python -m backend.test_websocket

## Notes

This repository exists primarily to demonstrate exploration of LangChain abstractions, real-time AI application architecture and WebSockets.

Expect unfinished features, architectural changes, and experimental code while the project develops.
