import pyotp
import requests
from typing import Any, Dict
from dotenv import load_dotenv
from .config import Config

load_dotenv()  # Load environment variables from .env file

def get_env_var(var_name):
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Missing environment variable: {var_name}")
    return value

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
