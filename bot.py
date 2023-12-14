import os
import discord
from discord.ext import commands
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Retrieve MySQL credentials from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

# Initialize MySQL connection
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

if db_connection.is_connected():
    print("Connected to the database")

db_cursor = db_connection.cursor()

# Fetch the bot token from the database
db_cursor.execute("SELECT auth_token FROM discord_tokens LIMIT 1")
result = db_cursor.fetchone()

if result:
    BOT_TOKEN = result[0]
    print("Bot token retrieved from the database")
else:
    print("Bot token not found in the database")
    exit()

# Set up Discord bot
intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    # Send "Hello World" along with the Discord server name and bot token
    await ctx.send(f'Hello World from {ctx.guild.name}')

# Run the bot
bot.run(BOT_TOKEN)
