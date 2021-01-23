import discord
import os
import re
from collections import OrderedDict

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
    with open("shakespeare_sonnets.txt") as my_sonnets:
        all_sonnets = my_sonnets.read()
    roman_id = "\n\n" #"^ *M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
    by_sonnet = re.split(roman_id, all_sonnets)
    # print(len(by_sonnet))
    # print(by_sonnet[0:3])
    for i in range(1, len(by_sonnet), 2):
        sonnets[write_roman((i + 1) // 2)] = f"Sonnet {write_roman((i + 1) // 2)}\n{by_sonnet[i]}"

        
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
        await message.channel.send(get_sonnet(message.content.split()[1].upper()))
def get_sonnet(num):
  try:
    return sonnets[write_roman(int(num))]
  except:
    return sonnets[num]

if __name__ == "__main__":
    client.run(os.getenv('TOKEN'))