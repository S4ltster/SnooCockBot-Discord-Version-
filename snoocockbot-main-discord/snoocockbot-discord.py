# Invite link: https://rb.gy/rd0qea

import discord
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from keep_alive import keep_alive
from discord_slash import SlashCommand, SlashContext
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

bot_token = os.environ['token']
client = commands.Bot(command_prefix = 'u/', intents = discord.Intents.all())
client.remove_command('help')
slash = SlashCommand(client, sync_commands = True)
status = cycle(['Proudly serving Snoo cocks to the world.','Reddit version: u/snoocockbot','Release: Stable','Shoutouts to Simpleflips','u/help', 'Shoutouts to Sparkster, Deltara#4947, Glass-Paramedic#8989, Nyperfox#6046'])

@client.event
async def on_ready():
  DiscordComponents(client, change_discord_methods = True)
  change_status.start()
  print("Bot is ready")

@tasks.loop(seconds = 10)
async def change_status():
  await client.change_presence(activity = discord.Game(next(status)))

@client.command()
async def snoocockbot(ctx):
  await ctx.send(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠈⡆⠀⣠⠞⢻⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣶⣤⠠⠓⠋⠁⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣀⣀⡀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡤⠖⠛⠉⠉⠉⠉⠉⠙⠛⢀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡾⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠉⠳⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⢡⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠇⠘⠛⠃⠀⠀⠀⠀⠒⠒⠢⠀⠀⠀⠠⡤⢄⡼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⢀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠘⢻⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠈⠉⠉⠉⠀⠀⣴⠛⣦⠀⠀⢀⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣤⣀⡀⠀⠀⠀⠀⡸⠀⠈⠛⣶⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⢛⡝⠁⠙⠿⡿⠛⠚⢇⠀⠀⠀⣽⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠁⣾⠁⠀⠀⠀⠀⠀⠀⢈⣳⡦⠚⠁⠀⠀⠀⠀⠀⠀
⠀⣴⢟⣿⣦⣄⡀⠈⢧⣿⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣮⣷⣤⡈⠙⠛⠲⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣖⠦⣤⣤⡄⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⠀⠸⣿⡗⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠉⠘⠧⡤⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

@client.command()
async def help(ctx):
  await ctx.send(type=InteractionType.ChannelMessageWithSource, content="This video should help you use the bot, if not then use u/snoocockbot to summon cocks, u/redditteam to view the reddit dev team or u/discordteam to view the discord dev team.", components=[Button(style=ButtonStyle.URL, label="Link", url="https://cutt.ly/OnWvS00")])

@client.command()
async def redditteam(ctx):
  await ctx.send("Elemento_Sphere (Defunct), IPV46, Glass-Paramedic, Nyperfox")

@client.command()
async def discordteam(ctx):
  await ctx.send("Sparkster#0000, Deltara#4947, Glass-Paramedic#6889, Nyperfox#6046")
#Tags which are #0000 are censored for privacy

@client.command()
async def invite(ctx):
  await ctx.send(type=InteractionType.ChannelMessageWithSource, content="Invite the bot!", components=[Button(style=ButtonStyle.URL, label="Invite link", url="https://discord.com/oauth2/authorize?client_id=836728250158809149&permissions=2147551232&redirect_uri=https%3A%2F%2Fdeltara3.github.io&scope=bot%20applications.commands")])

@slash.slash(name = "snoocock")
async def _snoocock(ctx: SlashContext):
  await ctx.send(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠈⡆⠀⣠⠞⢻⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣶⣤⠠⠓⠋⠁⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣀⣀⡀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡤⠖⠛⠉⠉⠉⠉⠉⠙⠛⢀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡾⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠉⠳⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⢡⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠇⠘⠛⠃⠀⠀⠀⠀⠒⠒⠢⠀⠀⠀⠠⡤⢄⡼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⢀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠘⢻⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠈⠉⠉⠉⠀⠀⣴⠛⣦⠀⠀⢀⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣤⣀⡀⠀⠀⠀⠀⡸⠀⠈⠛⣶⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⢛⡝⠁⠙⠿⡿⠛⠚⢇⠀⠀⠀⣽⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠁⣾⠁⠀⠀⠀⠀⠀⠀⢈⣳⡦⠚⠁⠀⠀⠀⠀⠀⠀
⠀⣴⢟⣿⣦⣄⡀⠈⢧⣿⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣮⣷⣤⡈⠙⠛⠲⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣖⠦⣤⣤⡄⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⠀⠸⣿⡗⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠉⠘⠧⡤⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

@slash.slash(name = "help")
async def _help(ctx: SlashContext):
  await ctx.send(type=InteractionType.ChannelMessageWithSource, content="This video should help you use the bot, if not then use u/snoocockbot to summon cocks, u/redditteam to view the reddit dev team or u/discordteam to view the discord dev team.", components=[Button(style=ButtonStyle.URL, label="Link", url="https://cutt.ly/OnWvS00")])

@slash.slash(name = "redditteam")
async def _redditteam(ctx: SlashContext):
  await ctx.send("Elemento_Sphere (Defunct), IPV46, Glass-Paramedic, Nyperfox")

@slash.slash(name = "discordteam")
async def _discordteam(ctx: SlashContext):
  await ctx.send("Sparkster#0000, Deltara#6969, Glass-Paramedic#8989, Nyperfox#6046")

@slash.slash(name = "invite")
async def _invite(ctx: SlashContext):
  await ctx.send(type=InteractionType.ChannelMessageWithSource, content="Invite the bot!", components=[Button(style=ButtonStyle.URL, label="Invite link", url="https://discord.com/oauth2/authorize?client_id=836728250158809149&permissions=2147551232&redirect_uri=https%3A%2F%2Fdeltara3.github.io&scope=bot%20applications.commands")])

keep_alive()
client.run(bot_token)
