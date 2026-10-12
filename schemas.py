from pydantic import BaseModel, Field
import uuid

class SupportTicket(BaseModel):
    """
    Pydantic model defining the strict JSON schema for extracted support tickets.
    This ensures the LLM always returns predictable, database-ready data.
    """
    ticket_id: str = Field(
        default_factory=lambda: f"TCK-{uuid.uuid4().hex[:6].upper()}", 
        description="Unique identifier for the support ticket"
    )
    category: str = Field(
        description="The primary category of the issue (e.g., Billing, Technical Support, Account Management, Bug Report)"
    )
    priority: str = Field(
        description="The priority level of the issue: Low, Medium, High, or Critical based on urgency"
    )
    sentiment: str = Field(
        description="The overall sentiment of the customer: Positive, Neutral, or Negative"
    )
    summary: str = Field(
        description="A concise, 1-2 sentence summary of the customer's core issue"
    )
    recommended_action: str = Field(
        description="The immediate suggested next step or routing destination for the human support team"
    )
