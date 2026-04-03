from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10, description="ID")
    name: str = Field(..., min_length=1, max_length=50, description="name")
    crew_size: int = Field(..., ge=1, le=20, description="crew size")
    power_level: float = Field(...,
                               ge=0.0,
                               le=100.0,
                               description="power level")
    oxygen_level: float = Field(...,
                                ge=0.0,
                                le=100.0,
                                description="oxygen level")
    last_maintenance: datetime = Field(...,
                                       description="last maintenance")
    is_operational: bool = Field(default=True,
                                 description="is the station operational")
    notes: Optional[str] = Field(default=None,
                                 max_length=200,
                                 description="notes")


def print_station(station: SpaceStation) -> None:

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Inoperative"
    print(f"Status: {status}")


def main() -> None:
    try:

        print("Space Station Data Validation")
        print("=" * 30)
        valid_station = SpaceStation(
            station_id="ISS001",
            name="international Space station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 4, 3, 16, 52, 0)
        )
        print_station(valid_station)

        print()
        print("=" * 30)

        notvalidation_station = SpaceStation(
            station_id="ISS001",
            name="international Space station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 4, 3, 16, 52, 0)
        )
        print_station(notvalidation_station)

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
