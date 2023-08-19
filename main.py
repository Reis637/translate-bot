import botToken
import discord
from discord.ext import commands

from translate import Translator

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True
intents.presences = True
intents.members = True

# Add more languages here, along with their respectives emojis in unicode

languages = {
    '\U0001F1FA\U0001F1F8': 'en',
    '\U0001F1EA\U0001F1F8': 'es',
    '\U0001F1E7\U0001F1F7': 'pt'
}

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message.content
    language = languages.get(reaction.emoji)

    if language is None:
        return

    translator = Translator(to_lang=language, from_lang="autodetect")
    translation = translator.translate(message)
    
    if translation == "PLEASE SELECT TWO DISTINCT LANGUAGES":
        translation = message

    await reaction.message.reply(translation, mention_author=False)
    
bot.run(botToken.TOKEN)

