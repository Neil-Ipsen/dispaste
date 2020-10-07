import os
import discord
from dotenv import load_dotenv

load_dotenv()


class DiscordInt:
    # Write __init__() here

    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()


class PastebinInt:
    # Write __init__() here

    TOKEN = os.getenv('PASTEBIN_TOKEN')
