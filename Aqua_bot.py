from http import client
import discord
import random

TOKEN = 'OTc3MjExNTA5MDkwNDIyODI0.GoNz3A.rldaUnW5B1nuEZ8lRGGb0o0H_C6--x5WOpLFKk'

client = discord.Client()

@client.event 
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message}: ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'discord-bot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'random Number: {random.randrange(1000000)}!'
            await message.channel.send(response)
            return

    if user_message.lower() == "!anywhere":
        await message.channel.send('Over Here!')
        return
            

client.run(TOKEN)