import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------------')

bot.remove_command('help')

@bot.event
async def connect(ctx):
    id_chan_bot = bot.get_channel(593143209178431489)
    if ctx.channel == id_chan_bot
        @bot.command()
        async def info(ctx):
            embed = discord.Embed(title="osiris", description="bot du conseil", color=0xeee657)

            # give info about you here
            embed.add_field(name="dévellopeur", value="aro20")

            # Shows the number of servers the bot is member of.
            embed.add_field(name="serveur connecté avec osiris", value=f"{len(bot.guilds)}")

            # give users a link to invite thsi bot to their server
            embed.add_field(name="Invite", value="non")

            embed.add_field(name="droits", value="administrateur")

            await ctx.send(embed=embed)

        @bot.command()
        async def help(ctx): # faire que seul les rangs 4 et le chef y accede
            embed = discord.Embed()

            embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
            embed.add_field(name="!help", value="Gives this message", inline=False)

            await ctx.send(embed=embed)

        @bot.command()
        async def users(ctx):
            id_serv = bot.get_guild(593129527417241636)
            await ctx.send(f"""#of member: {id.member_count}""")
    else:
        await ctx.send("le salon n est pas le bon")
    
bot.run("NTkzNDQ5MTQyNzc3NDEzNjM3.XRXRKQ.beZQO8iVlxKT7WzkEs7SWBZgA9g")
