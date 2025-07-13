from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()  # load values from .env file

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]