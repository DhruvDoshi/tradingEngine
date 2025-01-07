import json
import http.client
from utils.connect import make_request, USERNAME, CLIENT_LOCAL_IP, CLIENT_PUBLIC_IP, MAC_ADDRESS, API_KEY

def logout(conn, jwt_token):
    try:
        payload = json.dumps({"clientcode": USERNAME})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f"Bearer {jwt_token}",
            'X-UserType': 'USER',
            'X-SourceID': 'WEB',
            'X-ClientLocalIP': CLIENT_LOCAL_IP,
            'X-ClientPublicIP': CLIENT_PUBLIC_IP,
            'X-MACAddress': MAC_ADDRESS,
            'X-PrivateKey': API_KEY
        }
        response_data = make_request(conn, "POST", "https://apiconnect.angelone.in/rest/secure/angelbroking/user/v1/logout", payload, headers)
        if response_data.get('status'):
            print("Logout successful")
        else:
            print(f"Logout failed: {response_data.get('message', 'Unknown error')}")
    except http.client.HTTPException as e:
        print(f"HTTP Request error: {e}")
    except Exception as e:
        print(f"An error occurred while logging out: {e}")
