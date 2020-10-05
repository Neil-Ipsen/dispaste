import os
import discord
from dotenv import load_dotenv


class DiscordInt:
    # Write __init__() here

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()
