import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands

import aiohttp
import asyncio
import json
import re
import tracemalloc
import os
import requests
tracemalloc.start()

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_message(message):
    # Проверяем, что автор сообщения не является ботом
    if message.author.bot:
        return
    
    print(message.chat.id)

bot.run(token)
