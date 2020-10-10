import os
import discord
from dotenv import load_dotenv
import requests

load_dotenv()


class DiscordInt:
    # Write __init__() here

    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()


class PastebinInt:
    # Write __init__() here

    TOKEN = os.getenv('PASTEBIN_TOKEN')
    url = 'https://pastebin.com/api/api_post.php'
    text = ''
    title = ''
    #login = {}
    paste = {
        'api_option': 'paste',
        'api_dev_key': TOKEN,
        'api_paste_code': text,
        'api_paste_name': title,
        'api_paste_expire_date': 'see_https://pastebin.com/api',
        'api_user_key': None,
        'api_paste_format': 'see_https://pastebin.com/api'
    }
    
    x = requests.post(url, data = paste)
