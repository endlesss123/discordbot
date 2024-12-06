from discord.ext import commands
import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata
load_dotenv('token.env')

#Create intents object
intents = discord.Intents.default()  # Enables default intents
intents.messages = True  # Ensure the bot can read messages
intents.message_content = True  # Specifically enable message content intent

client = commands.Bot(command_prefix="!", intents=intents)

token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f"Logged in as a bot {client.user}")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_message(message):


    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "tell me a joke":
            jokes = [
                "Can someone please shed more light on how my lamp got stolen?",
                "Why is she called llene? She stands on equal legs.",
                "What do you call a gazelle in a lion's territory? Denzel."
            ]
            await message.channel.send(random.choice(jokes))
        elif user_message.lower() == "tell me about my server":
            await message.channel.send(f"here your server info,ip:{ec2_metadata.public_ipv4},region{ec2_metadata.region},availability zone,{ec2_metadata.availability_zone}")
client.run(token)