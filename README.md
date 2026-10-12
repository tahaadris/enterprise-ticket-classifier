# Enterprise Support Ticket Classifier

An AI-driven backend service that leverages Large Language Models (LLMs) to analyze raw, unstructured customer support conversations and extract validated, database-ready JSON payloads.

## Architecture & Tech Stack
* **Framework:** LangChain (LCEL)
* **Backend:** Flask (Python)
* **Data Validation:** Pydantic (`JsonOutputParser`)
* **LLM Provider:** OpenAI API (configurable for enterprise models like IBM Granite/Watsonx)

## Core Features
1. **Unstructured Data Ingestion:** Takes multi-turn chat history between users and agents.
2. **Contextual Reasoning:** Uses prompt engineering and LangChain pipelines to determine ticket category, sentiment, urgency, and recommended next actions.
3. **Strict Schema Enforcement:** Implements Pydantic to ensure the LLM output strictly adheres to a predefined JSON schema, preventing downstream application crashes caused by hallucinated formatting.
4. **REST API Integration:** Exposes the LangChain pipeline via a Flask POST endpoint (`/api/resolve`).

## Sample Output
When a raw conversation string is sent to the `/api/resolve` endpoint, the system returns a validated JSON object ready for database insertion:

```json
{
  "status": "success",
  "ticket": {
    "ticket_id": "TCK-A9B2C4",
    "category": "Billing & Invoicing",
    "priority": "High",
    "sentiment": "Negative",
    "summary": "User charged twice for Enterprise seat renewal on Oct 8.",
    "recommended_action": "Route to Accounts Receivable for duplicate transaction refund."
  }
}
