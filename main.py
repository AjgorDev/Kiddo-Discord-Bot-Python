import discord
from discord.ext import commands

import random
import datetime

description = '''Kiddo!'''


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents, description=description)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="Hey, I am Kiddo! | $about"))


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            welcome = discord.Embed(title='WELCOME TO KIDDO BOT', description='Thank you for inviting me to your server!\nIf you want to have more information about me use command **$about**.', color=0x71368a)
            welcome.set_image(url='https://cdn.discordapp.com/attachments/1049653476046671945/1049773234826002512/kiddobranding.gif')
            await channel.send(embed=welcome)
        break


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
        joke = discord.Embed(title=f'{response_joke} 🤣', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=joke)

    if message.content.startswith('$about'):
        await message.add_reaction('📬')
        about = discord.Embed(
            title='**Hey, My name is Kiddo!**\n*I was made by Igor Corleone#1182.*\n\nI am here to tell you some jokes and have fun with this server users!\n**Use** ***$help*** **command for list of all commands!**',
            description='[Invite me!](https://discord.com/api/oauth2/authorize?client_id=819276513140670466&permissions=37088832&scope=bot) | [Vote on us!](https://top.gg/bot/819276513140670466) | [Support server](https://discord.gg/AYHtS2fzND) | [Source Code](https://github.com/AjgorDev/Kiddo-Discord-Bot-Python/blob/main/bot.py)',
            color=0x71368a)
        about.set_image(url='https://cdn.discordapp.com/attachments/1049653476046671945/1049773234826002512/kiddobranding.gif')
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
        memeemb = discord.Embed(title=f'Here is meme for **{message.author}** 🤣', color=0x71368a)
        memeemb.set_image(url=response_meme)
        await message.channel.send(embed=memeemb)

    dice = str(random.choice(range(1, 10)))

    if message.content.startswith('$roll'):
        await message.add_reaction('🎲')
        roll = discord.Embed(title=f'{dice} 🎲', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=roll)

    if message.content.startswith('$ping'):
        await message.add_reaction('🏓')
        pong = discord.Embed(title='Pong! 🏓', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=pong)

    iq = str(random.choice(range(50, 250)))

    if message.content.startswith('$iq'):
        await message.add_reaction('🧠')
        iqemb = discord.Embed(title='Your IQ is:', description=f'{iq} 🧠', color=0x71368a)
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
        weekendemb = discord.Embed(title=f'{weekend}', color=0x71368a)
        await message.channel.send(embed=weekendemb)

    if message.content.startswith('$lenny'):
        await message.add_reaction('😏')
        lenny = discord.Embed(title='( ͡° ͜ʖ ͡°)', color=0x71368a)
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
        coinflip = discord.Embed(title=f'{coin}', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=coinflip)

    if message.content.startswith('$version'):
        await message.add_reaction('🤖')
        version = discord.Embed(title='Current version of Kiddo: 2.0 🤖', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=version)

    if message.content.startswith('$doge'):
        await message.add_reaction('🐶')
        doge = discord.Embed(title=f'Here is doge for **{message.author}** 🐶', color=0x71368a)
        doge.set_image(
            url='https://cdn.discordapp.com/attachments/819916120777555998/820960875133272084/5845e770fb0b0755fa99d7f4.png')
        await message.channel.send(embed=doge)

    if message.content.startswith('$cookie'):
        await message.add_reaction('🍪')
        cookie = discord.Embed(title=f'Here is cookie for **{message.author}** 🍪', color=0x71368a)
        cookie.set_image(
            url='https://cdn.discordapp.com/attachments/819916120777555998/820974520575590421/cookie_PNG13648.png')
        await message.channel.send(embed=cookie)

    eightball = [
        'Yes 🎱',
        'No 🎱',
        'Maybe 🎱',
    ]

    if message.content.startswith('$8ball'):
        await message.add_reaction('🎱')
        eightball_response = random.choice(eightball)
        eightballemb = discord.Embed(title=f'{eightball_response}', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=eightballemb)

    curse = [
        'Fuck you 🤬',
        'You are piece of shit 🤬',
        'I hate you 🤬',
        'You are so dumb 🤬',
    ]

    if message.content.startswith('$curse'):
        await message.add_reaction('🤬')
        curse_response = random.choice(curse)
        curseemb = discord.Embed(title=f'{curse_response}', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=curseemb)

    motivate = [
        'You are so beautiful 😃',
        'I love you 😃',
        'Do not give up 😃',
        'Have a nice day 😃',
    ]

    if message.content.startswith('$motivate'):
        await message.add_reaction('😃')
        motivate_response = random.choice(motivate)
        motivateemb = discord.Embed(title=f'{motivate_response}', color=0x71368a)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=motivateemb)

    # --------------------------------------------------------------emotes----------------------------------------------------------------------

    if message.content.startswith('$blush'):
        await message.add_reaction('😳')
        blushemb = discord.Embed(title=f'**{message.author}** 😳', color=0x71368a)
        blushemb.set_image(
            url='https://cdn.discordapp.com/attachments/819916120777555998/828014296788893787/84307582253a96e4552d20e3ecef3a33.gif')
        await message.channel.send(embed=blushemb)

    if message.content.startswith('$cry'):
        await message.add_reaction('😢')
        cryemb = discord.Embed(title=f'**{message.author}** 😢', color=0x71368a)
        cryemb.set_image(url='https://cdn.discordapp.com/attachments/819916120777555998/828016094509269002/cry.gif')
        await message.channel.send(embed=cryemb)

    if message.content.startswith('$dance'):
        await message.add_reaction('🕺')
        danceemb = discord.Embed(title=f'**{message.author}** 🕺', color=0x71368a)
        danceemb.set_image(url='https://cdn.discordapp.com/attachments/819916120777555998/828191745647837194/dance.gif')
        await message.channel.send(embed=danceemb)

    if message.content.startswith('$pout'):
        await message.add_reaction('😡')
        poutemb = discord.Embed(title=f'**{message.author}** 😡', color=0x71368a)
        poutemb.set_image(url='https://cdn.discordapp.com/attachments/823155630767996938/828202565082021918/pout.gif')
        await message.channel.send(embed=poutemb)

    if message.content.startswith('$shrug'):
        await message.add_reaction('🤷')
        shrugemb = discord.Embed(title=f'**{message.author}** 🤷', color=0x71368a)
        shrugemb.set_image(url='https://cdn.discordapp.com/attachments/823155630767996938/828203963169374208/shrug.gif')
        await message.channel.send(embed=shrugemb)

    if message.content.startswith('$sleepy'):
        await message.add_reaction('😴')
        sleepyemb = discord.Embed(title=f'**{message.author}** 😴', color=0x71368a)
        sleepyemb.set_image(
            url='https://cdn.discordapp.com/attachments/823155630767996938/828205263445033030/sleepy.gif')
        await message.channel.send(embed=sleepyemb)

    if message.content.startswith('$smile'):
        await message.add_reaction('😊')
        smileemb = discord.Embed(title=f'**{message.author}** 😊', color=0x71368a)
        smileemb.set_image(url='https://cdn.discordapp.com/attachments/823155630767996938/828208980962443264/smile.gif')
        await message.channel.send(embed=smileemb)

    if message.content.startswith('$thumbsup'):
        await message.add_reaction('👍')
        thumbsupemb = discord.Embed(title=f'**{message.author}** 👍', color=0x71368a)
        thumbsupemb.set_image(
            url='https://cdn.discordapp.com/attachments/823155630767996938/828210539712479312/thumbsup.gif')
        await message.channel.send(embed=thumbsupemb)

    if message.content.startswith('$triggered'):
        await message.add_reaction('😠')
        triggeredemb = discord.Embed(title=f'**{message.author}** 😠', color=0x71368a)
        triggeredemb.set_image(
            url='https://cdn.discordapp.com/attachments/823155630767996938/828213252055105536/triggered.gif')
        await message.channel.send(embed=triggeredemb)

    # --------------------------------------------------------------------actions------------------------------------------------------------------------------

    if message.content.startswith('$hug'):
        await message.add_reaction('🤗')
        hugemb = discord.Embed(title=f'**{message.author}** 🤗', color=0x71368a)
        hugemb.set_image(url='https://cdn.discordapp.com/attachments/823155630767996938/828219913382395934/hug.gif')
        await message.channel.send(embed=hugemb)

    if message.content.startswith('$kiss'):
        await message.add_reaction('💋')
        kissemb = discord.Embed(title=f'**{message.author}** 💋', color=0x71368a)
        kissemb.set_image(url='https://cdn.discordapp.com/attachments/823155630767996938/828221396378320946/kiss.gif')
        await message.channel.send(embed=kissemb)

    if message.content.startswith('$kill'):
        await message.add_reaction('🔪')
        killemb = discord.Embed(title=f'**{message.author}** 🔪', color=0x71368a)
        killemb.set_image(url='https://cdn.discordapp.com/attachments/823155630767996938/828222584955863040/kill.gif')
        await message.channel.send(embed=killemb)

    # ------------------------------------------------------------------lists-------------------------------------------------------------------

    if message.content.startswith('$help'):
        await message.add_reaction('📬')
        helpemb = discord.Embed(title='List of commands for Kiddo 👶 :', color=0x71368a)
        helpemb.add_field(name='$joke', value='sends random joke', inline=False)
        helpemb.add_field(name='$roll', value='rolls a number from 1 to 10', inline=False)
        helpemb.add_field(name='$meme', value='sends random meme', inline=False)
        helpemb.add_field(name='$ping', value='what can I say... just ***pong!***', inline=False)
        helpemb.add_field(name='$iq', value='shows your IQ', inline=False)
        helpemb.add_field(name='$weekend', value='shows when the weekend will start', inline=False)
        helpemb.add_field(name='$lenny', value='( ͡° ͜ʖ ͡°)', inline=False)
        helpemb.add_field(name='$coinflip', value='flips a coin', inline=False)
        helpemb.add_field(name='$version', value='shows current version of bot', inline=False)
        helpemb.add_field(name='$doge', value='sends doge', inline=False)
        helpemb.add_field(name='$cookie', value='gives you a cookie', inline=False)
        helpemb.add_field(name='$8ball [question]', value='helps you with a hard decision', inline=False)
        helpemb.add_field(name='$curse', value='demotivate yourself in weird way', inline=False)
        helpemb.add_field(name='$motivate', value='motivate yourself in weird way', inline=False)
        helpemb.add_field(name='$emotes', value='shows a list of emotes', inline=False)
        helpemb.add_field(name='$actions', value='shows a list of actions', inline=False)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=helpemb)

    if message.content.startswith('$emotes'):
        await message.add_reaction('📬')
        emoteemb = discord.Embed(title='List of emotes which you can use with Kiddo 👶 :', color=0x71368a)
        emoteemb.add_field(name='$blush', value='😳', inline=False)
        emoteemb.add_field(name='$cry', value='😢', inline=False)
        emoteemb.add_field(name='$dance', value='🕺', inline=False)
        emoteemb.add_field(name='$pout', value='😡', inline=False)
        emoteemb.add_field(name='$shrug', value='🤷', inline=False)
        emoteemb.add_field(name='$sleepy', value='😴', inline=False)
        emoteemb.add_field(name='$smile', value='😊', inline=False)
        emoteemb.add_field(name='$thumbsup', value='👍', inline=False)
        emoteemb.add_field(name='$triggered', value='😠', inline=False)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=emoteemb)

    if message.content.startswith('$actions'):
        await message.add_reaction('📬')
        actionsemb = discord.Embed(title='List of actions which you can use with Kiddo 👶 :', color=0x71368a)
        actionsemb.add_field(name='$hug', value='hug someone', inline=False)
        actionsemb.add_field(name='$kiss', value='kiss someone', inline=False)
        actionsemb.add_field(name='$kill', value='kill someone', inline=False)
        await message.channel.send(f'**{message.author}**')
        await message.channel.send(embed=actionsemb)



client.run('token')
