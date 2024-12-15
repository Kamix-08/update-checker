import asyncio
import discord
from discord import Webhook
import aiohttp

from data import *

async def execute():
    (url, selector, webhook_url) = load_data()
    
    if compare(url, selector):
        return
    
    await send(webhook_url)

async def send(webhook_url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, session=session)
        embed = discord.Embed(title="Update detected!")
        await webhook.send(embed=embed)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(execute())
    loop.close()