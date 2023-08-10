import requests

def get_data(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get("https://rippleenergy.com/rest/member_data", headers=headers)
    return response.json()
