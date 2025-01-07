from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Config:
    API_KEY: str
    USERNAME: str
    MPIN: str
    TOTP_SECRET: str
    CLIENT_LOCAL_IP: str
    CLIENT_PUBLIC_IP: str
    MAC_ADDRESS: str
    DP_ID: str
    BO_ID: str
    PAN_CARD: str

    @staticmethod
    def load():
        load_dotenv()
        return Config(**{
            field: os.getenv(field) or ""
            for field in Config.__annotations__
        })
