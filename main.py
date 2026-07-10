import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен!")
    try:
        synced = await bot.tree.sync()
        print(f"Синхронизировано команд: {len(synced)}")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping", description="Проверка работы бота")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🟢 АГИС «Прокуратура» работает!",
        ephemeral=True
    )


bot.run(TOKEN)
