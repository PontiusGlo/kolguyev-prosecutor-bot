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
        title="⚖️ АС «Надзор»",
        description="**Автоматизированная система прокурорского надзора**",
        color=0x0F2D5C
    )

    embed.add_field(
    name="Статус системы",
    value="🟢 Работает",
    inline=True
)
    embed.add_field(
    name="Версия",
    value="2.0",
    inline=True
)
    embed.add_field(name="Генеральный прокурор", value="Понтиус Гло", inline=False)

    embed.set_footer(
    text="⚖️ АС «Надзор» • На страже закона."
)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="info", description="Информация о прокуратуре")
async def info(interaction: discord.Interaction):

    embed = discord.Embed(
        title="⚖️ АС «Надзор»",
        description="Автоматизированная система прокурорского надзора.",
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
    text="⚖️ АС «Надзор» • На страже закона."
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
        style=discord.ButtonStyle.primary
    )
    async def productions(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Производства» находится в разработке.",
            ephemeral=True
        )

    @discord.ui.button(
        label="📝 Жалобы",
        style=discord.ButtonStyle.primary
    )
    async def complaints(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Жалобы» находится в разработке.",
            ephemeral=True
        )

    @discord.ui.button(
        label="📄 Документы",
        style=discord.ButtonStyle.primary
    )
    async def documents(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "🚧 Раздел «Документы» находится в разработке.",
            ephemeral=True
        )

    @discord.ui.button(
        label="📚 Архив",
        style=discord.ButtonStyle.primary
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
        title="⚖️ АС «Надзор»",
        description=(
    "**Автоматизированная система прокурорского надзора**\n\n"
    "Генеральная прокуратура\n"
    "Колгуевского автономного округа\n\n"
    "*На страже закона.*"
),
        color=0x0F2D5C
    )

    embed.add_field(
        name="👤 Генеральный прокурор",
        value="Понтиус Гло",
        inline=False
    )

  embed.add_field(
    name="💻 Система",
    value=(
        "Добро пожаловать в АС «Надзор».\n"
        "Выберите необходимый раздел для начала работы."
    ),
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
    text="⚖️ АС «Надзор» • На страже закона."
)

    await interaction.response.send_message(
        embed=embed,
        view=MainPanel()
    )

        
bot.run(TOKEN)
