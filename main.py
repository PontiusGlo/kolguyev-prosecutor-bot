import os
import discord
from discord import app_commands
from database import load, save
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

    embed.set_footer(text="Колгуевская автономная область • 2008")

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

    embed.set_footer(text="Колгуевская автономная область • 2008")

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="help", description="Список команд")
async def help(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📖 Справка",
        color=0x1F8B4C
    )

    embed.add_field(
        name="Доступные команды",
        value="/ping\n/info\n/help",
        inline=False
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

class MedicalForm(discord.ui.Modal, title="Выдача медицинской справки"):

    cid = discord.ui.TextInput(
        label="CID гражданина",
        placeholder="Например: 121375"
    )

    spravka = discord.ui.TextInput(
        label="Тип справки",
        placeholder="Медсправка ВУ / Госслужба / Оружие"
    )

    doctor = discord.ui.TextInput(
        label="ФИО врача"
    )

    async def on_submit(self, interaction: discord.Interaction):

        data = load()

        data.append({
            "cid": str(self.cid),
            "type": str(self.spravka),
            "doctor": str(self.doctor)
        })

        save(data)

        embed = discord.Embed(
            title="🏥 ЦМиК",
            description="Выдана медицинская справка",
            color=0x2ECC71
        )

        embed.add_field(name="CID", value=self.cid.value, inline=False)
        embed.add_field(name="Тип", value=self.spravka.value, inline=False)
        embed.add_field(name="Врач", value=self.doctor.value, inline=False)

        await interaction.response.send_message(embed=embed)
        
     
@bot.tree.command(name="справка", description="Выдать медицинскую справку")
async def spravka(interaction: discord.Interaction):
    await interaction.response.send_modal(MedicalForm())
        
bot.run(TOKEN)
