import asyncio
import os
import random
import datetime

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Hey, I am Kiddo! | $about"))
	print(f'{client.user.name} has connected to Discord!\n\n  _  ___     _     _       \n | |/ (_)   | |   | |      \n | \' / _  __| | __| | ___  \n |  < | |/ _` |/ _` |/ _ \ \n | . \| | (_| | (_| | (_) |\n |_|\_\_|\__,_|\__,_|\___/ \n             by Ajgor#0001')
	print('\nBot is online since: ', datetime.datetime.now().time())

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel_send(
		f'Hi {member.name}, welcome to my Discord server!'
	)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	jokes = [
		'Q: What do you call a lazy baby kangaroo?\nA: A pouch potato.',
		'Q: What did the snail say as he rode along on the turtle\'s back?\nA: Wheeee!',
		'Q: What is the best way to cook a gator?\nA: In a crock-pot',
		'Q: What do you call a penguin in the desert?\nA: Lost',
	]

	if message.content.startswith('$joke'):
		response_joke = random.choice(jokes)
		await message.add_reaction('🤣')
		joke = discord.Embed(title = f'{response_joke} 🤣', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=joke)

	if message.content.startswith('$about'):
		await message.add_reaction('📬')
		about = discord.Embed(title = '**Hey, My name is Kiddo!**\n***I was made by Ajgor#0001.***\n\n**I am here to tell you some jokes and have fun with this server users!**\n**Use** ***$help*** **command for list of all commands!**', description = '[Invite me!](https://discord.com/api/oauth2/authorize?client_id=819276513140670466&permissions=37088832&scope=bot) | [Donate](https://streamlabs.com/ajgor_rycerski_boj/tip) | [Vote on us!](https://top.gg/bot/819276513140670466) | [Support server](https://discord.gg/AYHtS2fzND) | [Source Code](https://github.com/AjgorDev/Kiddo-Discord-Bot-Python/blob/main/bot.py)' , color = 0x71368a)
		about.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/749256199702315008/de592db5d4bf3f9378e0773b6f6820ec.png?size=1024')
		await message.channel.send(embed=about)

	memes = [
		'https://media.discordapp.net/attachments/819276050466734092/819918378738122782/612bff8412e03dc3c84ea5aabe743d51.png?width=757&height=676',
		'https://media.discordapp.net/attachments/819276050466734092/819918543150907392/4e906cff-de39-45f5-a156-395597600cd5.png?width=557&height=676',
		'https://media.discordapp.net/attachments/819276050466734092/819918585509838928/628a356e4a78f4716166826bc20126f7.png',
		'https://media.discordapp.net/attachments/819276050466734092/819918642929336350/4d0b2b3c5b990d47b445074c05f5ca51.png?width=471&height=676',
		'https://media.discordapp.net/attachments/819276050466734092/819918705571004416/azmYnVz_460s.png',
		'https://media.discordapp.net/attachments/819276050466734092/819918855488143405/9748373.png',
		'https://media.discordapp.net/attachments/819276050466734092/819918944760496128/The-Burger-Index-1024x761.png?width=910&height=676',
		'https://media.discordapp.net/attachments/819276050466734092/819918990590738452/maxresdefault.png?width=1202&height=676',
	]

	if message.content.startswith('$meme'):
		response_meme = random.choice(memes)
		await message.add_reaction('🤣')
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(response_meme)

	dice = str(random.choice(range(1, 10)))

	if message.content.startswith('$roll'):
		await message.add_reaction('🎲')
		roll = discord.Embed(title = f'{dice} 🎲' , color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=roll)

	if message.content.startswith('$ping'):
		await message.add_reaction('🏓')
		pong = discord.Embed(title = 'Pong! 🏓', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=pong)

	iq = str(random.choice(range(50, 250)))

	if message.content.startswith('$iq'):
		await message.add_reaction('🧠')
		iqemb = discord.Embed(title = 'Your IQ is:', description = f'{iq} 🧠', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=iqemb)

	if message.content.startswith('$weekend'):
		await message.add_reaction('🕑')
		await message.channel.send(f'**{message.author}**')
		if datetime.datetime.today().weekday() == 0:
			weekend = 'Weekend starts in 5 days! 🕑'
		if datetime.datetime.today().weekday() == 1:
			weekend = 'Weekend starts in 4 days! 🕑'
		if datetime.datetime.today().weekday() == 2:
			weekend = 'Weekend starts in 3 days! 🕑'
		if datetime.datetime.today().weekday() == 3:
			weekend = 'Weekend starts in 2 days! 🕑'
		if datetime.datetime.today().weekday() == 4:
			weekend = 'Weekend starts tomorrow! 🕑'
		if datetime.datetime.today().weekday() == 5:
			weekend = 'Weekend goes on! 🕑'
		if datetime.datetime.today().weekday() == 6:
			weekend = 'Weekend goes on! 🕑'
		weekendemb = discord.Embed(title = f'{weekend}', color = 0x71368a)
		await message.channel.send(embed=weekendemb)

	if message.content.startswith('$lenny'):
		await message.add_reaction('😏')
		lenny = discord.Embed(title = '( ͡° ͜ʖ ͡°)', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=lenny)

	flip = [
		'Heads 🪙',
		'Tails 🪙',
		'Heads 🪙',
		'Tails 🪙',
	]

	if message.content.startswith('$coinflip'):
		await message.add_reaction('🪙')
		coin = random.choice(flip)
		coinflip = discord.Embed(title = f'{coin}', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=coinflip)

	if message.content.startswith('$help'):
		await message.add_reaction('📬')
		helpemb = discord.Embed(title = 'List of commands for Kiddo 👶 :', color = 0x71368a)
		helpemb.add_field(name='$joke', value = 'sends random joke', inline = False)
		helpemb.add_field(name='$roll', value = 'rolls a number from 1 to 10', inline = False)
		helpemb.add_field(name='$meme', value = 'sends random meme', inline = False)
		helpemb.add_field(name='$ping', value = 'what can I say... just ***pong!***', inline = False)
		helpemb.add_field(name='$iq', value = 'shows your IQ', inline = False)
		helpemb.add_field(name='$weekend', value = 'shows when the weekend will start', inline = False)
		helpemb.add_field(name='$lenny', value = '( ͡° ͜ʖ ͡°)', inline = False)
		helpemb.add_field(name='$coinflip', value = 'flips a coin', inline = False)
		helpemb.add_field(name='$report [name] <BETA>', value = 'report some bad guys like a boss :sunglasses:', inline = False)
		helpemb.add_field(name='$undo-report <BETA>', value = 'deletes your last report', inline = False)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=helpemb)

	#--------------------------------------------------------------------report system--------------------------------------------------------------------------
	
	if message.content.startswith('$report'):
		await message.add_reaction('❗')
		report = discord.Embed(title = 'Your report has been sent ✅', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=report)
		print(message.author,':',message.content)

	if message.content.startswith('$undo-report'):
		await message.add_reaction('✅')
		undoreport = discord.Embed(title = 'Your report has been deleted ✅', color = 0x71368a)
		await message.channel.send(f'**{message.author}**')
		await message.channel.send(embed=undoreport)
		print(message.author,':',message.content)

client.run(TOKEN)