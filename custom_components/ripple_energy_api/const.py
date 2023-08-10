"""Constants for the Ripple Energy integration."""

DOMAIN = "ripple_energy"
CONFIG_NAME = "Ripple Energy"
CONFIG_SCAN_INTERVAL = "300"
CONFIG_API_KEY: "API Key"

DATA_SCHEMA_ACCOUNT = vol.Schema({
  vol.Required(CONFIG_API_KEY): str
})