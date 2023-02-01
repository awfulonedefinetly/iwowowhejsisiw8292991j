from discord.ext import commands
import discord
import asyncpraw


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

# Prefix will be '!'
client = commands.Bot(command_prefix= '!', intents=intents)

# Create an app on Reddit and get necessary information there
reddit = asyncpraw.Reddit(
client_id='',
client_secret='',
user_agent='Example u/reddit',
username='user',
password='admin'
)

reddit.read_only = False

subreddit = reddit.subreddit('AgainstHateSubreddits')

@client.event
async def post_please():
          while True:
              for post in reddit.subreddit('AgainstHateSubreddits').new(limit=1000):
                      channel = discord.utils.get(client.get_all_channels(), name='spam')
                      await channel.send(post.title + post.url)
              
# Go to Discord Developer Portal                                
client.run('Paste here Discord bot token')                                                                                         
