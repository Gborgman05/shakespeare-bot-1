import discord
import os
import re

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])

client = discord.Client()
sonnets = {}
def build_sonnets():
    with open("shakespeare_sonnets.txt") as sonnets:
        all_sonnets = sonnets.read()
    for i in range(len(re.split(all_sonnets))):
        sonnets[write_roman(i)] = all_sonnets[i]

        
@client.event
async def on_ready():
    ''' callback to do when ready '''
    print(f"We have logged in as {client.user}")
    build_sonnets()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!sonnet'):
        await message.channel.send(sonnets[message.content.split()[1]])
def main():
    pass

if __name__ == "__main__":
    client.run(os.getenv('TOKEN'))