import requests
import config_flow
import json

from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import SensorEntityDescription

def get_data(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get("https://rippleenergy.com/rest/member_data/", headers=headers)
    return response.json()


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    api_key = config.get("api_key")
    data = await hass.async_add_executor_job(get_data, api_key)
    
    sensors = []
    for item in data:
        sensors.append(RippleEnergySensor(item))
    
    async_add_entities(sensors, True)

class RippleEnergySensor(SensorEntity):
    def __init__(self, data):
        self._data = data
        self._state = None

    @property
    def name(self):
        return self._data["generation_assets[*].name"]

    @property
    def state(self):
        return self._state

    def update(self):
        self._state = self._data["value"]
