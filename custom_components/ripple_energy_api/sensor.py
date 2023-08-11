import json
import requests
from homeassistant.helpers import config_entry_flow
from homeassistant.helpers.entity import Entity

DOMAIN = "ripple_energy"
PLATFORMS = ["sensor"]

# Example of API endpoint and headers
API_ENDPOINT = "https://rippleenergy.com/rest/member_data/"
HEADERS = {
    "Authorization": "Bearer YOUR_API_TOKEN",
    "Content-Type": "application/json"
}

async def async_setup_entry(hass, entry, async_add_entities):
    api_data = await fetch_data_from_api()
    sensors = []

    for device in api_data.get("devices", []):
        sensors.append(RippleEnergySensor(device))

    async_add_entities(sensors, True)

async def fetch_data_from_api():
    try:
        response = requests.get(API_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print("Error fetching data from API:", error)
        return {}

class RippleEnergySensor(Entity):
    def __init__(self, device_info):
        self._device_info = device_info
        self._state = None

    @property
    def name(self):
        return f"Ripple Energy {self._device_info['name']}"

    @property
    def unique_id(self):
        return self._device_info["id"]

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return "kWh"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._device_info["id"])},
            "name": self._device_info["name"],
            "manufacturer": "Ripple Energy",
        }

    async def async_update(self):
        api_data = await fetch_data_from_api()
        device = next((d for d in api_data.get("devices", []) if d["id"] == self.unique_id), None)
        if device:
            self._state = device.get("energy_consumed", None)

async def async_step_import(hass, config):
    return await async_step_user(hass, config)

config_entry_flow.register_webhook_flow(
    DOMAIN,
    "Ripple Energy",
    {
        "config_entries": config_entry_flow.HANDLERS,
        "discovery": "discovery",
        "import": async_step_import,
    },
)

