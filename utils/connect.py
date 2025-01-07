import pyotp
import requests
from typing import Any, Dict
from .config import Config

class ApiConnect:
    def __init__(self, config: Config):
        self.config = config
        self.session = requests.Session()
    
    def generate_totp(self) -> str:
        return pyotp.TOTP(self.config.TOTP_SECRET).now()
    
    def get_headers(self, jwt_token: str = None) -> Dict[str, str]:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-UserType': 'USER',
            'X-SourceID': 'WEB',
            'X-ClientLocalIP': self.config.CLIENT_LOCAL_IP,
            'X-ClientPublicIP': self.config.CLIENT_PUBLIC_IP,
            'X-MACAddress': self.config.MAC_ADDRESS,
            'X-PrivateKey': self.config.API_KEY
        }
        if jwt_token:
            headers['Authorization'] = f"Bearer {jwt_token}"
        return headers

    def make_request(self, method: str, url: str, payload: str, headers: Dict[str, str]) -> Dict[str, Any]:
        response = self.session.request(method, url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json()
