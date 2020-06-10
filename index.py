import os
import discord
import json
from dotenv import load_dotenv

load_dotenv()

#JSON files input
json_file1 = open('JSONfiles/bodies.json' , 'r')
json_file2 = open('JSONfiles/copies.json' , 'r')
json_file3 = open('JSONfiles/gadgets.json', 'r')
json_file4 = open('JSONfiles/weapons.json', 'r')
json_file5 = open('JSONfiles/wheels.json' , 'r')

#Loading the files
json_data1 = json.load(json_file1)
json_data2 = json.load(json_file2)
json_data3 = json.load(json_file3)
json_data4 = json.load(json_file4)
json_data5 = json.load(json_file5)

#Getting parts in lists
bodies = []
for i in range(22):
    data1 = json_data1[i]
    bodies.append(data1['a'].lower().replace(" ", ""))

copies = []
for i in range(5):
    data2 = json_data2[i]
    copies.append(data2['a'].lower().replace(" ", ""))

gadgets = []
for i in range(26):
    data3 = json_data3[i]
    gadgets.append(data3['a'].lower().replace(" ", ""))

weapons = []
for i in range(28):
    data4 = json_data4[i]
    weapons.append(data4['a'].lower().replace(" ", ""))

wheels = []
for i in range(42):
    data5 = json_data5[i]
    wheels.append(data5['a'].lower().replace(" ", ""))

#Getting the discord Bot Token
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready() -> str:
    print(f'{client.user.name} has been connected to discord')


@client.event
async def on_message(message):
    
    if not message.content.startswith('$'):
        return

    if message.author == client.user:
        return 

    if message.content[1:] == 'help':
        response = """```
    Categories:
    1: Bodies
    2: Copies(+Cost)
    3: Gadgets
    4: Weapons
    5: Wheels```
            """
        await message.channel.send(response)

    if message.content[1:].lower() == 'bodies':
        response = "\n".join(bodies)
        await message.channel.send(f"```{response}```")

    if message.content[1:].lower() == 'copies':
        response = "\n".join(copies)
        await message.channel.send(f"```{response}```")

    if message.content[1:].lower() == 'gadgets':
        response = "\n".join(gadgets)
        await message.channel.send(f"```{response}```")

    if message.content[1:].lower() == 'weapons':
        response = "\n".join(weapons)
        await message.channel.send(f"```{response}```")

    if message.content[1:].lower() == 'wheels':
        response = "\n".join(wheels)
        await message.channel.send(f"```{response}```")

    if message.content[1:] in bodies:
        health = json_data1[bodies.index(message.content[1:])]
        response = f"""
    Name     = {health['a']}
    Battery  = {health['b']}
    rarity   = {health['c']}
    Health   = {health['d']}
    Bonus    = {health['e']}
    --------------------------
    Level-1  = {health['1']}
    Level-2  = {health['2']}
    Level-3  = {health['3']}
    Level-4  = {health['4']}
    Level-5  = {health['5']}
    Level-6  = {health['6']}
    Level-7  = {health['7']}
    Level-8  = {health['8']}
    Level-9  = {health['9']}
    Level-10 = {health['10']}
    Level-11 = {health['11']}
    Level-12 = {health['12']}
    Level-13 = {health['13']}
    """
        await message.channel.send(f'```{response}```')

    if message.content[1:] in copies:
        copy = json_data2[copies.index(message.content[1:])]
        response = f"""
    Type  = {copy['a']}
    ----------------------
    Level Parts  == Cost
    ----------------------
    2     {copy['1']}         {copy['2']}
    3     {copy['3']}         {copy['4']}
    4     {copy['5']}         {copy['6']}
    5     {copy['7']}         {copy['8']}
    6     {copy['9']}         {copy['10']}
    7     {copy['11']}        {copy['12']}
    8     {copy['13']}        {copy['14']}
    9     {copy['15']}        {copy['16']}
    10    {copy['17']}       {copy['18']}
    11    {copy['19']}       {copy['20']}
    12    {copy['21']}       {copy['22']}
    13    {copy['23']}       {copy['24']}

    """
        await message.channel.send(f'```{response}```')

    if message.content[1:] in gadgets:
        health = json_data3[gadgets.index(message.content[1:])]
        response = f"""
    Name     = {health['a']}
    Battery  = {health['b']}
    rarity   = {health['c']}
    Health   = {health['d']}
    Bonus    = {health['e']}
    --------------------------
    Level-1  = {health['1']}
    Level-2  = {health['2']}
    Level-3  = {health['3']}
    Level-4  = {health['4']}
    Level-5  = {health['5']}
    Level-6  = {health['6']}
    Level-7  = {health['7']}
    Level-8  = {health['8']}
    Level-9  = {health['9']}
    Level-10 = {health['10']}
    Level-11 = {health['11']}
    Level-12 = {health['12']}
    Level-13 = {health['13']}
    """
        await message.channel.send(f'```{response}```')

    if message.content[1:] in weapons:
        damage = json_data4[weapons.index(message.content[1:])]
        response = f"""
    Name     = {damage['a']}
    Battery  = {damage['b']}
    rarity   = {damage['c']}
    Damage   = {damage['d']}
    Bonus    = {damage['e']}
    --------------------------
    Level-1  = {damage['1']}
    Level-2  = {damage['2']}
    Level-3  = {damage['3']}
    Level-4  = {damage['4']}
    Level-5  = {damage['5']}
    Level-6  = {damage['6']}
    Level-7  = {damage['7']}
    Level-8  = {damage['8']}
    Level-9  = {damage['9']}
    Level-10 = {damage['10']}
    Level-11 = {damage['11']}
    Level-12 = {damage['12']}
    Level-13 = {damage['13']}
    """
        await message.channel.send(f'```{response}```')

    if message.content[1:] in wheels:
        health = json_data5[wheels.index(message.content[1:])]
        response = f"""
    Name     = {health['a']}
    Battery  = {health['b']}
    rarity   = {health['c']}
    Health   = {health['d']}
    Bonus    = {health['e']}
    --------------------------
    Level-1  = {health['1']}
    Level-2  = {health['2']}
    Level-3  = {health['3']}
    Level-4  = {health['4']}
    Level-5  = {health['5']}
    Level-6  = {health['6']}
    Level-7  = {health['7']}
    Level-8  = {health['8']}
    Level-9  = {health['9']}
    Level-10 = {health['10']}
    Level-11 = {health['11']}
    Level-12 = {health['12']}
    Level-13 = {health['13']}
    """
        await message.channel.send(f'```{response}```')


client.run(TOKEN)