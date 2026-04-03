from pydantic import Field, ValidationError, BaseModel, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional

class ContactType(Enum):
    VISUAL    = "visual"
    AUDIO     = "audio"
    PHYSICAL  = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(...,
                            min_length=5,
                            max_length=15,
                            description="Unique contact ID, 5-15 characters")
    timestamp: datetime = Field(...,
                                description="DateTime of the contact event")
    location: str = Field(...,
                          min_length=3,
                          max_length=100,
                          description="Location of the contact, 3-100 characters")
    contact_type: ContactType = Field(...,
                                      description="Type of alien contact")
    signal_strength: float = Field(...,
                                   ge=0.0,
                                   le=10.0,
                                   description="Signal strength on a 0.0-10.0 scale")
    duration_minutes: int = Field(...,
                                  ge=1,
                                  le=1440,
                                  description="Duration in minutes, max 24 hours (1440)")
    witness_count: int = Field(...,
                               ge=1,
                               le=100,
                               description="Number of witnesses, 1-100")
    message_received: Optional[str] = Field(None,
                                            max_length=500,
                                            description="Optional message received, max 500 characters")
    is_verified: bool = Field(default=False,
                              description="Verification status, defaults to False")

    @model_validator(mode='after')
    def custom_validation(self) -> None:
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")


def print_contact_log(contact: AlienContact) -> None:

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received}")




def main() -> None:
    print("Alien Contact Log Validation")
    print('=' * 41)

    valid_contact = AlienContact(
        contact_id="AC001",
        timestamp=datetime.fromisoformat("2024-06-15T22:45:00"),
        location="Roswell, New Mexico",
        contact_type=ContactType.VISUAL,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=3,
        message_received="We come in peace",
    )

