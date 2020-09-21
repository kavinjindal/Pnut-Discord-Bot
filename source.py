import discord
import random
from discord.ext import commands
import asyncio
from datetime import datetime

client = commands.Bot(command_prefix = ".")

client.remove_command('help')

# Command Prompt -----------------------------
@client.event
async def on_ready():
    print("Bot is ready for testing")

#about = 'Pnut is a discord bot created by Kavin Jindal. This bot has been programmed in Python.'
#'\n' "It is made for a purpose of teaching and helping people in technology and development"
  
#functions = 'Pnut provides information and resources to help people learn programming languages. '
#'\n' 'By writing particular commands like ".python" or ".java", it will post a whole list of paid and free courses on  the programming languages'
#'\n' 'It will also show you videos regarding different topics like penetration testing, daily tips, ethical hacking etc.'  
#token = '#mytokenhere'
#bot=commands.Bot(command_prefix='!')

#send_time='8:00' #time is in 24hr format
#message_channel_id='725605918049435698' #channel ID to send images to


#async def time_check():
#    await client.wait_until_ready()
#    message_channel=client.get_channel(message_channel_id)
#    while not client.is_closed:
#        now=datetime.strftime(datetime.now(),'%H:%M')
#        if now.hour() == 8 and now.minute() == 11:
#            await message_channel.send(f"Good Morning @everyone, I hope your day goes awesome")
#            time=90
#        else:
#            time=1
#        await asyncio.sleep(time)

#bot.loop.create_task(time_check())
 

#CHANNEL = '725605918049435698'
#INTERVAL = 7200
#MESSAGE = '!d bump'   
#async def send_interval_message():
#    await client.wait_until_ready()
#    channel = CHANNEL
#    interval = INTERVAL
#    message = MESSAGE
#    channel = discord.Object(id=channel)
#    while not client.is_closed:
#        await client.send_message(channel, message)
#       await asyncio.sleep(interval)



        
    






@client.command(pass_context=True)
async def pnut(ctx):
    author = ctx.message.author

    embed = discord.Embed(

        
        title = 'Pnut Bot at your service',
        colour = discord.Colour.green())

        

    embed.set_author(name='Pnut Bot Help ', url='https://github.com/kavinjindal/Pnut-Discord-Bot')
    embed.set_image(url='https://i.imgur.com/u716EqD.jpg')
    embed.add_field(name = 'About Pnut :robot:', 
        value='Pnut is a discord bot created by Kavin Jindal. This bot has been programmed in Python.'
              '\n' "It is made for a purpose of teaching and helping people in technology and development :desktop:", 
              inline=True)
    embed.add_field(name = '**Info:**'
    , value= '**VERSION 1.1.1 TO COME OUT SOON**'
          '**Version:** 1.1.1'
    '\n'  '**Developed by  : ** Kavin Jindal'
    '\n'  '**Programmed in : **' 'Python'
    , inline=False )
    embed.add_field(name = 'Functions' , 
        value='Pnut provides information and resources to help people learn programming languages. '
        ,inline=False)
    embed.add_field(name = 'Commands', 
        value = 'Type the command `.cmd` to get the commands list')
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def cmd(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        
        title = 'Commands for Pnut bot',
        colour = discord.Colour.orange())

    embed.set_author(name = 'Pnut Bot Help')
    embed.add_field(name = '`.python`', value=
        "This command shows all the info, resources and learning material for Python"
        , inline=False)
    embed.add_field(name = '`.ethical`',
        value = 'This command lists out the requirements, info and learning material for Ethical Hacking',
         inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def python(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        
        title = 'Python Resources',
        colour = discord.Colour.orange())

    embed.set_author(name = 'Pnut bot')
    embed.set_thumbnail(url = 'https://i.imgur.com/E8qsnWt.png')
    embed.add_field(name = ':arrow_forward: `.paid_py` ', value=
        "Write .paid_py to get all paid courses for python "
        , inline=False)
    embed.add_field(name = ':arrow_forward:`.free_py`',
        value = 'This command shows all the free resources for python',
         inline=False)
    embed.add_field(name = ':arrow_forward:`.extra_py`',
        value = 'This command shows some extra info about python and more videos related to it',
         inline=False)
    
    await ctx.send(embed=embed) 

@client.command(pass_context = True)
async def paid_py(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        
        title = 'Paid Python Resources',
        colour = discord.Colour.orange())

    embed.set_author(name = 'Pnut Bot')
    embed.add_field(name = 'Paid Python Courses', value=
        '**BEST SELLER ON UDEMY**'
        '\n'':arrow_forward: https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/'
        '\n'"-----------------------------------------------------------------------------------"
        '\n'':arrow_forward: https://www.udemy.com/course/python-for-beginners-learn-all-the-basics-of-python/'
        '\n'':arrow_forward: https://www.coursera.org/specializations/python'
            , inline=False)
    embed.set_image(url = 'https://i.imgur.com/E8qsnWt.png')

    await ctx.send(f'Hey there {ctx.author.mention}, '
        '\n Here are some selected paid courses for Python, that you would like',embed=embed)

@client.command(pass_context = True)
async def free_py(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = 'Free Python Resources',
        colour = discord.Colour.orange())
    embed.set_author(name = 'Pnut Bot')
    embed.set_image(url = 'https://i.imgur.com/E8qsnWt.png')
    embed.add_field(name = 'Free Python Courses',
        value = ':arrow_forward:https://www.udemy.com/course/winning-at-python-start-learning-python-for-free/'
        '\n' ":arrow_forward:https://www.udemy.com/course/python-core-and-advanced/"
        '\n' ":arrow_forward:https://www.udemy.com/course/python-the-complete-python-developer-course/"
        '\n' "**Videos For Python**"
        '\n' ':play_pause:https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=21618s'
        '\n' ':play_pause:https://www.youtube.com/watch?v=rfscVS0vtbw&t=10598s'
        '\n' ':play_pause:https://www.youtube.com/watch?v=4F2m91eKmts&t=32933s',


         inline=False)
    await ctx.send(embed=embed)
@client.command(pass_context = True)
async def extra_py(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = 'Extra Python Resources',
        colour = discord.Colour.orange())
    embed.set_author(name = 'Pnut Bot')
    embed.set_image(url = 'https://i.imgur.com/E8qsnWt.png')
    embed.add_field(name = 'Extra Resources for Python',
        value = ':play_pause:https://www.youtube.com/watch?v=WvhQhj4n6b8'
        '\n' ':play_pause:https://www.youtube.com/watch?v=Y8Tko2YC5hA'
        '\n' ':play_pause:https://www.youtube.com/watch?v=xxeBb7OyKXY',
         inline=False)
    
    await ctx.send(embed=embed) 
#@client.event
#async def on_message(message):
#   if message.author == client.user:
#       return

@client.command(pass_context = True)
async def obfile(ctx):
    embed = discord.Embed(
        title = 'ObFile Updates', url='https://github.com/kavinjindal/ObFile', 
        colour = discord.Colour.blue())
    embed.set_image(url='https://i.imgur.com/45xapbb.jpg')
    embed.set_author(name = 'ObFile 1.1.1')
    embed.add_field(name = 'About', 
        value = 'It is a Python Compiler and Obfuscator for Windows developed by Kavin Jindal ',
        inline = False)
    embed.add_field(name = 'Latest Updates'
        ,value= '**ObFile 1.1.1**'
        '\n' 'Updated : 10/09/2020'
        '\n' 'ObFile version 1.1.1 is out!! Go check it out!!!!',
        inline=False)
    embed.add_field(name = 'Download ObFile 1.1.1 and know more about it'
        ,value='https://github.com/kavinjindal/ObFile',
        inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def ethical(ctx):
    embed = discord.Embed(
        title = 'Learn Ethical Hacking',
        colour = discord.Colour.orange()
    
    )
    embed.set_thumbnail(url='https://i.imgur.com/3Yv3QaN.png')
    embed.add_field(name = 'Pnut Bot', 
    value='Here are the commands to access **Ethical Hacking Resources**'
    ,inline=False )
    embed.add_field(name = ':arrow_forward: `.paid_hack`'
    , value = 'Get paid but the best resources for Ethical Hacking'
    , inline=False)
    embed.add_field(name = ':arrow_forward: `.free_hack`'
    , value = 'Get free resources to learn Ethical Hacking'
    , inline=False)
    
    await ctx.send(f'Here are the commands for you to get info on Ethical Hacking'
    '\n', embed=embed)

@client.command(pass_context = True)
async def paid_hack(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        
        title = 'Paid Ethical Hacking Resources',
        colour = discord.Colour.orange())

    embed.set_author(name = 'Pnut Bot')
    embed.add_field(name = 'Paid Ethical Hacking Courses', value=
        '**BEST SELLER ON UDEMY**'
        '\n'':arrow_forward: https://www.udemy.com/course/learn-ethical-hacking-from-scratch/'
        '\n'"-----------------------------------------------------------------------------------"
        '\n'':arrow_forward: https://www.udemy.com/course/hands-on-complete-penetration-testing-and-ethical-hacking/'
        '\n'':arrow_forward: https://www.udemy.com/course/wireshark-packet-analysis-and-ethical-hacking-core-skills/'
        '\n'':arrow_forward: https://www.udemy.com/course/penetration-testing/'

            , inline=False)
    embed.set_image(url = 'https://i.imgur.com/8vaIbxR.jpg')

    await ctx.send(f'Hey there {ctx.author.mention}, '
        '\n Here are some selected paid courses for Ethical Hacking, that you would like',embed=embed)

@client.command(pass_context = True)
async def free_hack(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        
        title = 'Free Ethical Hacking Resources',
        colour = discord.Colour.orange())

    embed.set_author(name = 'Pnut Bot')
    embed.add_field(name = 'Free Ethical Hacking Courses', value=
        
        '\n'':arrow_forward: https://www.udemy.com/course/ethical-hacker/'
        
        '\n'':arrow_forward: https://www.coursera.org/learn/introduction-cybersecurity-cyber-attacks'
        '\n' '**YOUTUBE VIDEOS**'
        '\n' ':arrow_forward: https://www.youtube.com/watch?v=dz7Ntp7KQGA&t=14514s'
        '\n' ':arrow_forward: https://www.youtube.com/watch?v=3Kq1MIfTWCE&t=35s'
        
                    , inline=False)
    embed.set_image(url = 'https://i.imgur.com/8vaIbxR.jpg')

    await ctx.send(f'Hey there {ctx.author.mention}, '
        '\n Here are some selected few courses for Ethical Hacking, that you would like',embed=embed)
#@client.command(aliases=['user', 'info'])
#async def who_is(ctx, member : discord.Member):
#    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.red())
#    embed.add_field(name = "ID" , value= member.id , inline = True )
#    embed.set_thumbnail(url = member.avatar_url)
#    embed.set_footer(icon_url = ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
 #   await ctx.send(embed=embed)

#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return

#    if message.content.startswith('hello'):
#        await message.channel.send(f'Hey there.....{message.author.mention}')

#    if message.content.startswith('bye'):
 #       await message.channel.send(f"Bye {message.author.mention},c ya")
#
#    if message.content.startswith('hi'):
#        await message.channel.send(f'Hi {message.author.mention}, ssup')



#-------------Normal command-----------------------------

client.run('token)










# Random omitted codes---------------------------------------------------------------------
#        
#@client.command()
#async def hi():
 #   await client.say("Hello")

#@client.command()
#async def start():
 #   await client.say('Hey there, I am KJ a discord bot made by Kavin Jindal')

#@client.event
#async def on_message(message):
#    channel = message.channel
#    if message.content.startswtih(".start"):
#        await client.send_message(channel, "Hello I am KJ a discord bot")

#--------------------------------------------------------------------------------------------
#@client.event
#async def sunrise():
#    while(True):
#        await client.wait_until_ready()
#        online_members = []
#        for member in client.get_all_members():
#            if member.status != discord.status.offline and member.id != client.user.id:
#                online_members.append(member.id)
#            if len(online_members) > 0:
#                user = random.choice(online_members)
#                current_time = int(datetime.now().strftime("%I"))
#                message = f'Happy Morning @everyone, I hope your day goes amazing'
#                await channel.send(message)

#client.loop.create_task(sunrise())
# -------------------------------------------------------------------------------------------
