import discord
import json
import colorama
import os
from discord.ext import commands
from colorama import Fore

colorama.init(autoreset=True)
intents = discord.Intents.all()
bot=commands.Bot(command_prefix="!", intents=intents, self_bot=True)

print("  ____  _                        _   ____")                                 
print(" |  _ \(_)___  ___ ___  _ __ __| | / ___|  ___ _ __ __ _ _ __   ___ _ __ ") 
print(" | | | | / __|/ __/ _ \| '__/ _` | \___ \ / __| '__/ _` | '_ \ / _ \ '__|") 
print(" | |_| | \__ \ (_| (_) | | | (_| |  ___) | (__| | | (_| | |_) |  __/ |")    
print(" |____/|_|___/\___\___/|_|  \__,_| |____/ \___|_|  \__,_| .__/ \___|_|")    
print("                                                        |_|")
print("\n")
print("         github.com/xoela		      xyl.lol/z")
print("\n")
print(Fore.RED +   "If it doesn't start scraping or gives an error, you did something wrong.")
print("\n")

config = json.load(open("config.json"))
channel_id = input("Channel ID: ")

@bot.event
async def on_ready():
    print(f"Logged in, {bot.user}")
    print(Fore.GREEN + "Successfully logged in, started scraping")
    os.system('cls')
    print(Fore.RED + "If it doesn't start scraping or gives an error, you did something wrong")
    channel = bot.get_channel(int(channel_id))
    async for message in channel.history(limit=None):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.url.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".mkv")):
                    await attachment.save(f"./media\{attachment.filename}")
                    print(Fore.GREEN + "Succesfully saved")


bot.run(config['token'], bot=False)