import discord
import random

def gen_pass():
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(10):
        password += random.choice(elements)
    return password

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('pass'):
        await message.channel.send("genn_pass")
    else:
        await message.channel.send(message.content)

client.run("MTE1NTA2NjcyOTA0MzU5NTMzNQ.GQGUOT.Gj64GR2IMiWXtad2i7p_UpGytDpaN_cPj-6SyQ")

#Новая функция гитхаб сделал
