from datetime import datetime, timezone

from pydantic import BaseModel

SENSOR_IDS = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3",
}
LOCATIONS = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen",
}


def get_sensor_id(location: str) -> str:
    return SENSOR_IDS.get(location, "0")


def get_location(sensor_id: str) -> str:
    return LOCATIONS.get(sensor_id, "Unknown")


class TemperatureResponse(BaseModel):
    value: float
    unit: str = 'C'
    timestamp: datetime = datetime.now(timezone.utc).isoformat()
    location: str
    status: str = 'Working'
    sensor_id: str
    sensor_type: str = 'Temperature'
    description: str = 'WarmHouse temperature sensor.'
