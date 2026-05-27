import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path(__file__).parent / '.env')

token = os.getenv('DISCORD_TOKEN')
if token is None:
    raise SystemExit('DISCORD_TOKEN not found. Make sure .env exists and contains DISCORD_TOKEN.')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.INFO, handlers=[handler])
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

TARGET_USER_ID = 1112599688315686922
REACTION = "😭"

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author.id == TARGET_USER_ID:
        await message.add_reaction(REACTION)

    await bot.process_commands(message)

bot.run(token)