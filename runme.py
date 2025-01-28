import requests
from dotenv import dotenv_values
import json

config = dotenv_values(".env")

url = f"https://api.telegram.org/bot{config.get('BOT_TOKEN')}/getUpdates"

response = requests.get(url)
print(json.dumps(response.json(), indent=4))