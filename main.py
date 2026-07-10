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


@bot.tree.command(name="пинг", description="Проверка работы системы прокуратуры")
async def ping(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🏛️ Прокуратура Колгуевской автономной области",
        description="**АГИС «Прокуратура» работает в штатном режиме.**",
        color=0x1F8B4C
    )

    embed.add_field(name="Статус", value="🟢 Онлайн", inline=True)
    embed.add_field(name="Версия", value="v1.0", inline=True)
    embed.add_field(name="Генеральный прокурор", value="Понтиус Гло", inline=False)

    embed.set_footer(text="Колгуевская автономная область • 2008 год")

    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
