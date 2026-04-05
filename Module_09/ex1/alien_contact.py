from pydantic import Field, ValidationError, BaseModel, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
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
                          description="Location of the contact")
    contact_type: ContactType = Field(...,
                                      description="Type of alien contact")
    signal_strength: float = Field(...,
                                   ge=0.0,
                                   le=10.0,
                                   description="Signal strength")
    duration_minutes: int = Field(...,
                                  ge=1,
                                  le=1440,
                                  description="Duration in minutes")
    witness_count: int = Field(...,
                               ge=1,
                               le=100,
                               description="Number of witnesses, 1-100")
    message_received: Optional[str] = Field(None,
                                            max_length=500,
                                            description="Optional message")
    is_verified: bool = Field(default=False,
                              description="Verification status")

    @model_validator(mode='after')
    def custom_validation(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "contact_id must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def print_contact_log(contact: AlienContact) -> None:

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received}")


def main() -> None:
    try:
        print("Alien Contact Log Validation")
        print('=' * 41)

        valid_contact = AlienContact(
            contact_id="AC001",
            timestamp=datetime.now(),
            location="Roswell, New Mexico",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=3,
            message_received="Greetings from Zeta Reticuli",
        )
        print_contact_log(valid_contact)

    except ValidationError as e:
        print('Expected validation error:')
        for error in e.errors():
            print(error['msg'][13:])
    try:
        print()
        print('=' * 41)
        nonvalid_contact = AlienContact(
            contact_id="AC001",
            timestamp=datetime.now(),
            location="Roswell, New Mexico",
            contact_type=ContactType.PHYSICAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=3,
            message_received="Greetings from Zeta Reticuli",
        )
        print_contact_log(nonvalid_contact)

    except ValidationError as e:
        print('Expected validation error:')
        for error in e.errors():
            print(error['msg'][13:])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
