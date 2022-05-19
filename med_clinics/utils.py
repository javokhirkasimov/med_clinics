import requests
from django.conf import settings


class Bot:
    SEND_MESSAGE = (
        "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    )

    def __init__(self):
        self.token = settings.BOT_TOKEN
        self.chat_id = settings.CHAT_ID

    def get_url(self, text):
        url = self.SEND_MESSAGE.format(
            token=self.token,
            chat_id=self.chat_id,
            text=text
        )
        return url

    def send_message(self, text):
        url = self.get_url(text)
        res = requests.get(url)
        if res.status_code != 200:
            self.send_message(res.content)


bot = Bot()
text = """
Appointment ID: {appointment_id}
Client:
    Full Name: {client_name}
    Medical Card: {client_medical_card}
    Contact: {client_contact}
    Address: {client_address}
Clinic:
    Clinic ID: {clinic_id}
    Title: {clinic_title}
Services:
"""