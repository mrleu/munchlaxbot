import discord
import responses
import os

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Error with message:{e}")


def run_discord_bot():
    TOKEN = os.getenv('MUNCHLAXBOT_TOKEN')
    def_intents = discord.Intents.default()
    def_intents.members = True
    def_intents.message_content = True
    client = discord.Client(intents=def_intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running")

    @client.event
    async def on_message(message):
        print(message.author, client.user, message, client)
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"username: {username}, user_message: {user_message}, channel: {channel}, message:{message}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

