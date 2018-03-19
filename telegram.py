import requests


class TelegramBot:
    def __init__(self, token):
        self.base_url = "https://api.telegram.org/bot{}/".format(token)

    def send_message(self, text, chat_id):
        r = requests.get(self.base_url + "sendMessage?text={}&chat_id={}".format(text, chat_id))
        r = r.json()
        if r["ok"]:
            return True, r["result"]["message_id"]
        return False, r["description"]

    def update_message(self, text, chat_id, message_id):
        r = requests.get(
            self.base_url + "editMessageText?text={}&chat_id={}&message_id={}".format(text, chat_id, message_id))
        r = r.json()
        if r["ok"]:
            return True, "ok"
        return False, r["description"]
