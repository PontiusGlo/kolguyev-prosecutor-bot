import os
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import View, Button
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен!")

    try:
        synced = await bot.tree.sync()
        print(f"Синхронизировано команд: {len(synced)}")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping", description="Проверка работы системы")
async def ping(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🏛 Генеральная прокуратура",
        description="**АГИС «Прокуратура» работает в штатном режиме.**",
        color=0x0B6623
    )

    embed.add_field(name="Статус", value="🟢 Онлайн", inline=True)
    embed.add_field(name="Версия", value="1.0", inline=True)
    embed.add_field(name="Генеральный прокурор", value="Понтиус Гло", inline=False)

    embed.set_footer(
    text="Генеральная прокуратура Колгуевского автономного округа"
)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="info", description="Информация о прокуратуре")
async def info(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🏛 Генеральная прокуратура",
        description="Информация о государственном органе.",
        color=0x8B0000
    )

    embed.add_field(
        name="Руководитель",
        value="Понтиус Гло",
        inline=False
    )

    embed.add_field(
        name="Основные задачи",
        value="• Надзор за соблюдением законов\n"
              "• Контроль государственных органов\n"
              "• Рассмотрение жалоб граждан",
        inline=False
    )

    embed.set_footer(
    text="Генеральная прокуратура Колгуевского автономного округа"
)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="help", description="Список команд")
async def help(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📖 Справка",
        color=0x1F8B4C
    )

    embed.add_field(
        name="Доступные команды",
        value="/панель\n/ping\n/info\n/help",
        inline=False
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

# =========================================================
# Панель Генерального прокурора
# =========================================================

class MainPanel(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="📂 Производства",
        style=discord.ButtonStyle.green
    )
    async def productions(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Производства» находится в разработке.",
            ephemeral=True
        )

    @discord.ui.button(
        label="📝 Жалобы",
        style=discord.ButtonStyle.blurple
    )
    async def complaints(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Жалобы» находится в разработке.",
            ephemeral=True
        )

    @discord.ui.button(
        label="📄 Документы",
        style=discord.ButtonStyle.grey
    )
    async def documents(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Документы» находится в разработке.",
            ephemeral=True
        )

    @discord.ui.button(
        label="📚 Архив",
        style=discord.ButtonStyle.red
    )
    async def archive(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Архив» находится в разработке.",
            ephemeral=True
        )


@bot.tree.command(
    name="панель",
    description="Главная панель Генеральной прокуратуры"
)
async def panel(interaction: discord.Interaction):

    embed = discord.Embed(
        title="⚖️ Генеральная прокуратура",
        description="**Колгуевского автономного округа**",
        color=0x0B6623
    )

    embed.add_field(
        name="👤 Генеральный прокурор",
        value="Понтиус Гло",
        inline=False
    )

    embed.add_field(
        name="🏛 АИС «Прокурор»",
        value="Добро пожаловать в электронную систему прокуратуры.",
        inline=False
    )

    embed.add_field(
        name="📊 Состояние",
        value="""
📂 Производств: **0**
📝 Жалоб: **0**
📄 Документов: **0**
""",
        inline=False
    )

    embed.set_footer(
        text="Генеральная прокуратура Колгуевского автономного округа"
    )

    await interaction.response.send_message(
        embed=embed,
        view=MainPanel()
    )

        
bot.run(TOKEN)
