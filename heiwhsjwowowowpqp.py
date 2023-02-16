# -- The bot was made by the capitalist! --

#pylint:disable=E0237
from discord.ext import commands
import discord
import praw
import datetime
import asyncio


intents = discord.Intents().all()
intents.members = True
intents.messages = True
intents.message_content = True

prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)

class AHSError(Exception):
     """
     Raised when the subreddit name is not AgainstHateSubreddits 
     """
     def __init__(self, error, message="The subreddit name must be AgainstHateSubreddits):
        self.error = error 
        self.message = message 
        super().__init__(self.message)

# Create an application on Reddit to get necessary data
reddit = praw.Reddit(
client_id='REDACTED',
client_secret='REDACTED',
user_agent='REDACTED',
username='REDACTED',
password='REDACTED'
)

reddit.read_only = False


# Sends an alarm about new report            
async def send_dm():
            while True:
                user_ids = "Paste your user id as a integer. Otherwise it will throw an exception."
                subreddit = reddit.subreddit("The subreddit name itself")
                if subreddit != "AgainstHateSubreddits":
                  raise AHSError(subreddit)
                new_posts = subreddit.new(limit=1)
                # Using a for loop to iterate over the posts
                for x in new_posts:
                    user = await bot.fetch_user(user_ids)
                    await user.send(f"Your subreddit was reported in {subreddit.display_name}: {x.title}\n{x.url}")
                # Checking new posts every 5 seconds
                await asyncio.sleep(5)
                
                                                                                                                                      
@bot.event
async def on_ready():
            now = datetime.datetime.now()
            channel = discord.utils.get(bot.get_all_channels(), name='general')
            embed = discord.Embed(title="The bot is now online!")
            embed.add_field(name="Online: ", value=":green_circle:")
            embed.add_field(name=f"The date is: ", value=str(now))
            embed.add_field(name=":information_source:", value="Type !info for the commands!")
            await channel.send(embed=embed)
            bot.loop.create_task(send_dm())                                                                                                                                                                                                                           
                                                                
@bot.command()
async def post(ctx):           
           # Using same method as in send_dm()
           subreddit = reddit.subreddit('AgainstHateSubreddits')
            for post in subreddit.new(limit=1):
                 new_embed = discord.Embed(title=post.title, url=post.shortlink)
                 new_embed.add_field(name="Post text: ", value="Some text")
                 new_embed.set_image(url=post.url) 
                 await ctx.send(embed=new_embed)
                      
                      
                           
                                
                                          
if __name__ == "__main__":
    # Go to Discord Developer Portal and create an application there
    NEW_TOKEN = "DISCORD BOT TOKEN"
    bot.run(NEW_TOKEN)                                                                                                                   
