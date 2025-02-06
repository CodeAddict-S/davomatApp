from fingerprints.sendMessage import TeleMessages
from celery import shared_task

@shared_task
def send_message(message, chat_id): 
    TeleMessages.send(message, chat_id)