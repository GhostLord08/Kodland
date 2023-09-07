from discord.ext import commands
import discord
import random


intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.command()
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

    
@bot.command()
async def Hello(self,ctx):
    await ctx.send("HI!")

@bot.command()
async def Bye(self,ctx):
    await ctx.send("See you :)")

@bot.command()
async def HCICY(self,ctx):
    await ctx.send("You can use everyday chat phrases")


bot.run("ODI4MTg2MTA4NzU1MDUwNTI2.G5Faxy.8pbXrqyw3SEQlEgGEiUhnl02jRaIq_s9Zu0KN0")
