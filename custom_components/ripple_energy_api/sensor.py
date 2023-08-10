import requests

#API_URL = "https://api.rippleenergy.com/data"  # Update with the actual API URL
API_URL = "https://rippleenergy.com/rest/member_data/KR8IOQKc_VujCBcL:arCYlJieSW1BmnjIvcdLB_9GPUQncKFgUtO3eGoBoRk"

def get_ripple_data():
    response = requests.get(API_URL)
    data = response.json()
    return data

def create_home_assistant_sensors(data):
    # Iterate through the data and create sensors in Home Assistant
    for entry in data:
        sensor_name = f"ripple_{entry['id']}_sensor"  # Customize the sensor naming
        sensor_value = entry['value']  # Update with the actual JSON structure
        
        # Use Home Assistant API or MQTT to create/update the sensor
        # Example (using Home Assistant API):
        requests.post("http://172.16.1.2/api/states/sensor." + sensor_name, json={"state": sensor_value})
        
        # Alternatively, you can use MQTT to publish the sensor value
        
        print(f"Created sensor: {sensor_name} with value: {sensor_value}")

if __name__ == "__main__":
    ripple_data = get_ripple_data()
    create_home_assistant_sensors(ripple_data)
