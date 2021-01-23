import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    ''' callback to do when ready '''
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!shakespeare'):
        await message.channel.send("To be or not to be, is that your question?")
def main():
    pass

if __name__ == "__main__":
    client.run(os.getenv('TOKEN'))