# Invite link: https://rb.gy/rd0qea

import discord
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from keep_alive import keep_alive
from discord_slash import SlashCommand, SlashContext

bot_token = os.environ['token']
client = commands.Bot(command_prefix = 'u/', intents = discord.Intents.all())
client.remove_command('help')
slash = SlashCommand(client, sync_commands = True)
status = cycle(['Proudly serving Snoo cocks to the world.','Reddit version: u/snoocockbot','Release: Stable'])

@client.event
async def on_ready():
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
  await ctx.send("<https://cutt.ly/OnWvS00>")

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
  await ctx.send("<https://cutt.ly/OnWvS00>")

keep_alive()
client.run(bot_token)
