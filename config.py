from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv("instagram_username")
password = os.getenv("instagram_password")
newsapi = os.getenv("newsapi_key")
headlines_file = os.getenv("headlines_file")

