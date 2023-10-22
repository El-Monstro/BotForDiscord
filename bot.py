import discord

# Определите интенты, которые ваш бот будет использовать
intents = discord.Intents.default()
intents.typing = False  # Пример: выключить интент для набора текста
intents.presences = False  # Пример: выключить интент для наличия пользователей

# Создайте объект клиента с интентами
client = discord.Client(intents=intents)

token = "MTE2NTY3MjI0NDE4NjQ2ODM3Mw.GwjSR3.QgwjamcPlf36urJy3eGDjx2xqnNFc2EffCQH9c"


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")


client.run(token)
