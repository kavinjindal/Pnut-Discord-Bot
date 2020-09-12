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






@client.command(pass_context=True)
async def pnut(ctx):
    author = ctx.message.author

    embed = discord.Embed(

        
        title = 'Pnut Bot at your service',
        colour = discord.Colour.orange())

        

    embed.set_author(name='Pnut Bot Help ')
    embed.set_image(url='https://i.imgur.com/u716EqD.jpg')
    embed.add_field(name = 'About Pnut :robot:', 
        value='Pnut is a discord bot created by Kavin Jindal. This bot has been programmed in Python.'
              '\n' "It is made for a purpose of teaching and helping people in technology and development :desktop:", 
              inline=True)
    embed.add_field(name = 'Functions' , 
        value='Pnut provides information and resources to help people learn programming languages. '
        ,inline=False)
    embed.add_field(name = 'Commands', 
        value = 'Type the command **.cmd** to get the commands list')
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def cmd(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        
        title = 'Commands for Pnut bot',
        colour = discord.Colour.orange())

    embed.set_author(name = 'Pnut Bot Help')
    embed.add_field(name = '.python', value=
        "This command shows all the info, resources and learning material for Python"
        , inline=False)
    embed.add_field(name = '.ethical',
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
    embed.add_field(name = '.paid_py', value=
        "Write .paid_py to get all paid courses for python "
        , inline=False)
    embed.add_field(name = ':arrow_forward:.free_py',
        value = 'This command shows all the free resources for python',
         inline=False)
    embed.add_field(name = ':arrow_forward:.extra_py',
        value = 'This command shows some extra info about python and more videos related to it',
         inline=False)
    embed.add_field(name = ':arrow_forward:.proj_py',
        value = 'You can see the project ideas for python',
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

    await ctx.send('Hey there @everyone, '
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




#-------------Normal command-----------------------------

client.run(TOKEN)










