#!/usr/bin/env python

import config
import datetime
import time
from telegram import TelegramBot

bot = TelegramBot(config.BOT_TOKEN)


def prepare_message():
    now = datetime.datetime.now()
    target = datetime.datetime.fromtimestamp(config.DEAD_UNIX_TIME)
    diff = target - now
    days, hours, minutes, seconds = diff.days, diff.seconds / 3600, (diff.seconds % 3600) / 60, diff.seconds % 60
    return config.TEMPLATE.format(days=days, hours=hours, minutes=minutes, seconds=seconds)


if __name__ == "__main__":
    try:
        result = bot.send_message(prepare_message(), config.CHAT_ID)
        if not result[0]:
            print "Error on sending message, " + result[1]
            exit(1)

        message_id = result[1]
        while True:
            result = bot.update_message(prepare_message(), config.CHAT_ID, message_id)
            if not result[0]:
                print "Error on updating message, " + result[1]
                exit(2)

            time.sleep(config.INTERVAL)
    except KeyboardInterrupt:
        pass
