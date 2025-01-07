from utils.connect import generate_totp, create_connection, make_request, API_KEY, USERNAME, MPIN, TOTP_SECRET, CLIENT_LOCAL_IP, CLIENT_PUBLIC_IP, MAC_ADDRESS
import json

def login():
    try:
        totp = generate_totp(TOTP_SECRET)
        conn = create_connection()
        payload = json.dumps({
            "clientcode": USERNAME,
            "password": MPIN,
            "totp": totp,
            "state": "state_variable"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-UserType': 'USER',
            'X-SourceID': 'WEB',
            'X-ClientLocalIP': CLIENT_LOCAL_IP,
            'X-ClientPublicIP': CLIENT_PUBLIC_IP,
            'X-MACAddress': MAC_ADDRESS,
            'X-PrivateKey': API_KEY
        }
        response_data = make_request(conn, "POST", "https://apiconnect.angelone.in/rest/auth/angelbroking/user/v1/loginByPassword", payload, headers)
        if response_data.get('status'):
            jwt_token = response_data['data']['jwtToken']
            print("Login successful")
            return conn, jwt_token
        else:
            print(f"Login failed: {response_data.get('message', 'Unknown error')}")
            return None, None
    except http.client.HTTPException as e:
        print(f"HTTP Request error: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred while logging in: {e}")
        return None, None
