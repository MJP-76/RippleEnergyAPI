import requests

def get_data(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get("https://api.rippleenergy.com/data", headers=headers)
    return response.json()
