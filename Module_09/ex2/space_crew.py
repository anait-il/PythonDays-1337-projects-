from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import List
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10, description="Unique member ID, 3-10 characters")
    name: str = Field(..., min_length=2, max_length=50, description="Full name, 2-50 characters")
    rank: Rank = Field(..., description="Crew member rank")
    age: int = Field(..., ge=18, le=80, description="Age in years, 18-80")
    specialization: str = Field(..., min_length=3, max_length=30, description="Area of specialization, 3-30 characters")
    years_experience: int = Field(..., ge=0, le=50, description="Years of experience, 0-50")
    is_active: bool = Field(default=True, description="Whether crew member is active, defaults to True")


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15, description="Unique mission ID, 5-15 characters")
    mission_name: str = Field(..., min_length=3, max_length=100, description="Mission name, 3-100 characters")
    destination: str = Field(..., min_length=3, max_length=50, description="Mission destination, 3-50 characters")
    launch_date: datetime = Field(..., description="Scheduled launch datetime")
    duration_days: int = Field(..., ge=1, le=3650, description="Duration in days, max 10 years (3650)")
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12, description="List of crew members, 1-12")
    mission_status: str = Field(default="planned", description="Mission status, defaults to planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0, description="Budget in millions, 1.0-10000.0")

    @model_validator(mode="after")
    def validate_mission(self):

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            if experienced < len(self.crew) / 2: 
                raise ValueError("Long missions need" "at least 50% experienced crew (5+ years)")

        inactive = [member.name
                    for member in self.crew
                    if not member.is_active]
        if inactive:
            raise ValueError("All crew must be active")

        return self


def display_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}")


def main() -> None:
    try:
        print("Space Mission Crew Validation")
        print("=" * 41)
        print("Valid mission created:")
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Engineering",
                    years_experience=5,
                ),
            ]
        )
        display_mission(mission)
        print()
        print("=" * 41)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg'][13:]}")

    try:
        bad_mission = SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Bad Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=366,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Junior",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Cleaning",
                    years_experience=0,
                ),
            ]
        )
        display_mission(bad_mission)
        print()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg'][13:]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
