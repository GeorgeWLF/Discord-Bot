import discord
from disctoken import token
import json
import requests
from discord import Embed

greet_words = ["Hi", "hi", "Hello", "hello"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print("+" + "-"*60 + "+")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        for text in greet_words:
            if message.content.startswith(text):
                await message.reply(f"Hello! {message.author.display_name}", mention_author=True)

        if message.content.startswith('/joke'):

            async def get_joke():
                joke_url_single = requests.get(
                    'https://v2.jokeapi.dev/joke/Programming')
                json_joke = json.loads(joke_url_single.text)
                if json_joke["type"] == "single":
                    print("fetching a single joke")
                    return(json_joke["joke"])
                else:
                    print("fetching a two part joke")
                    return(f"**{json_joke['setup']}**\n\n||{json_joke['delivery']}||")
            the_joke = await get_joke()
            await message.channel.send(the_joke)

        if message.content.startswith('/help'):
                embed_help = Embed(color=0xe74c3c, title="General Commands")
                embed_help.add_field(name="/help", value="displays all the available commands", inline=False)
                embed_help.add_field(name="/joke", value="gives you a random programing joke", inline=False)
                await message.channel.send(embed=embed_help)
            #     return embed
            # help_command = await get_help()
            # await message.channel.send(help_command)

    async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Welcome {member.mention} to {guild.name}!"
            embed_help = Embed(color=0xe74c3c, title="General Commands")
            embed_help.add_field(name="/help", value="displays all the available commands", inline=False)
            embed_help.add_field(name="/joke", value="gives you a random programing joke", inline=False)
            await guild.system_channel.send(to_send, embed=embed_help)




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)