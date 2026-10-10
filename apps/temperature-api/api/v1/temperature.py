import random

from fastapi import APIRouter, status

from schemas.response.temperature import TemperatureResponse, get_sensor_id, get_location

MIN_TEMPERATURE, MAX_TEMPERATURE = 0, 40

router = APIRouter()


@router.get('/temperature', response_model=TemperatureResponse, status_code=status.HTTP_200_OK,
            summary='Temperature', description='Temperature value for location.',
            response_description='Random integer + sensor info.')
async def get_temperature_by_location(
        location: str
) -> TemperatureResponse:
    print("Location: ", location)
    return TemperatureResponse(
        value=random.uniform(MIN_TEMPERATURE, MAX_TEMPERATURE),
        location=location, sensor_id=get_sensor_id(location)
    )


@router.get('/temperature/{sensor_id}', response_model=TemperatureResponse, status_code=status.HTTP_200_OK,
            summary='Temperature', description='Temperature value for location.',
            response_description='Random integer + sensor info.')
async def get_temperature_by_sensor(
        sensor_id: str
) -> TemperatureResponse:
    print("Sensor ID: ", sensor_id)
    return TemperatureResponse(
        value=random.uniform(MIN_TEMPERATURE, MAX_TEMPERATURE),
        location=get_location(sensor_id), sensor_id=sensor_id
    )
