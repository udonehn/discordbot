import discord
import numgame
import Palindrome
import maze
import baseball
from discord.ext import commands

intents=discord.Intents.all()
bot=commands.Bot(intents=intents,command_prefix='!')

@bot.event
async def on_ready(): #봇이 처음 실행 될 때 하는 행동
    print('bot is ready')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('대기'))    #online, idle, dnd
    global running
    running=False
    
@bot.event
async def on_message(message):
    global running
    con = message.content.split()
    
    if con[0]=='help':
        await message.channel.send("1. start numgame \n2. start Palindrome \n3. start baseball \n4. done")

    elif con[0]=='done':
        running=False
        await bot.change_presence(activity=discord.Game('대기'))
        await message.channel.send('봇을 종료합니다.')
        print('done')
    
    elif con[0]=='start':
        if con[1]=='numgame':
            running='numgame'
            await bot.change_presence(activity=discord.Game('numgame'))
            mes = numgame.start()
            await message.channel.send(mes)
            
        if con[1]=='Palindrome':
            running='Palindrome'
            await bot.change_presence(activity=discord.Game('Palindrome'))
            mes = Palindrome.start()
            await message.channel.send(mes)
            
        if con[1]=='baseball':
            running='baseball'
            await bot.change_presence(activity=discord.Game('baseball'))
            mes = baseball.start()
            await message.channel.send(mes)    
                    
    else:
        if running=='numgame':
            if con[0].isdigit():
                mes = numgame.check(int(con[0]))
                await message.channel.send(mes)
            if con[0]=='answer':
                mes = numgame.answer()
                await message.channel.send(mes)
                
        if running=='Palindrome':
            if con[0].isdigit():
                mes = Palindrome.check(con[0])
                await message.channel.send(mes)

        if running=='baseball':
            if con[0].isdigit():
                mes = baseball.check(con[0])
                await message.channel.send(mes)
            if con[0]=='answer':
                mes = baseball.answer()
                await message.channel.send(mes)

bot.run('') #키 입력