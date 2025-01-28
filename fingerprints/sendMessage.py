import requests
from dotenv import dotenv_values
from django.utils import timezone

config = dotenv_values(".env")

class TeleMessages:
    @staticmethod
    def send(message, chat_id):
        url = f"https://api.telegram.org/bot{config.get('BOT_TOKEN')}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": message
        }

        response = requests.post(url, data=payload)

        return response.json()
    
    @staticmethod
    def get_weekday():
        day = timezone.now().weekday()
        match day:
            case 0:
                return "mon"
            case 1:
                return "tue"
            case 2:
                return "wed"
            case 3:
                return "thu"
            case 4:
                return "fri"
            case 5:
                return "sat"
            case 6:
                return "sun"