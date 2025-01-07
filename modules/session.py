import json
from typing import Tuple, Optional
from utils.connect import ApiConnect
from utils.config import Config

class Session:
    def __init__(self):
        self.config = Config.load()
        self.api = ApiConnect(self.config)
        self.jwt_token = None

    def login(self) -> bool:
        try:
            totp = self.api.generate_totp()
            payload = json.dumps({
                "clientcode": self.config.USERNAME,
                "password": self.config.MPIN,
                "totp": totp,
                "state": "state_variable"
            })
            response = self.api.make_request(
                "POST",
                "https://apiconnect.angelone.in/rest/auth/angelbroking/user/v1/loginByPassword",
                payload,
                self.api.get_headers()
            )
            if response.get('status'):
                self.jwt_token = response['data']['jwtToken']
                print("Login successful")
                return True
            print(f"Login failed: {response.get('message', 'Unknown error')}")
            return False
        except Exception as e:
            print(f"Login error: {e}")
            return False

    def logout(self) -> bool:
        if not self.jwt_token:
            return False
        try:
            payload = json.dumps({"clientcode": self.config.USERNAME})
            response = self.api.make_request(
                "POST",
                "https://apiconnect.angelone.in/rest/secure/angelbroking/user/v1/logout",
                payload,
                self.api.get_headers(self.jwt_token)
            )
            if response.get('status'):
                print("Logout successful")
                return True
            print(f"Logout failed: {response.get('message', 'Unknown error')}")
            return False
        except Exception as e:
            print(f"Logout error: {e}")
            return False
