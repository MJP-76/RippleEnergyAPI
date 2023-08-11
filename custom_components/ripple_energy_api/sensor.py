import requests
import json

# URL of the Ripple Energy API endpoint
api_url = "https://rippleenergy.com/rest/member_data/KR8IOQKc_VujCBcL:arCYlJieSW1BmnjIvcdLB_9GPUQncKFgUtO3eGoBoRk"

# Make an HTTP GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant information from the JSON response
    energy_production = data.get("generation_assets[1].generation.today.generated")  # Replace with actual key
    
    # Assuming you want to create a sensor for energy production
    sensor_config = {
        "name": "Kirk Hill Generation Today",
        "state_class": "measurement",
        "unit_of_measurement": "kWh",
        "state": energy_production
    }
    
    # Convert the sensor configuration to JSON
    sensor_json = json.dumps(sensor_config)
    
    # URL of Home Assistant API endpoint to create/update sensors
    ha_api_url = "https://172.16.1.2/api/states/sensor.ripple_energy_generation_today"  # Replace with your Home Assistant IP
    
    # Headers for the Home Assistant API request
    headers = {
        "Authorization": "Bearer YOUR_HA_ACCESS_TOKEN",  # Replace with your Home Assistant access token
        "Content-Type": "application/json"
    }
    
    # Make a POST request to create/update the sensor in Home Assistant
    ha_response = requests.post(ha_api_url, headers=headers, data=sensor_json)
    
    if ha_response.status_code == 200:
        print("Sensor created/updated successfully in Home Assistant")
    else:
        print("Failed to create/update sensor in Home Assistant")
else:
    print("Failed to fetch data from Ripple Energy API")
