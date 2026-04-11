from dotenv import load_dotenv
import os
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
print("Base URL:", BASE_URL)