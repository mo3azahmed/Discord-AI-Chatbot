import discord
from discord.ext import commands
import random
import google.generativeai as genai
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()  # loads variables from .env

#bot basics:
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True  # Allow reading messages

bot = commands.Bot(command_prefix="!", intents=intents) #prefix just in case, ill use mentions

#configuring Gemeni here:---------------------------------------------.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY) # type: ignore #if it works, dont touch it
model = genai.GenerativeModel( # type: ignore #same here
    'gemini-2.5-flash',
    system_instruction=("a chill guy, cool but not too energetic (anime protagonist cold vibe) avoid using periods unless necessary to look more casual and stuff yk")
) #please ignore this
#the above sets up gemini----------------------------------------------.

@bot.event
async def on_ready():
    print(f'Logged in!') #prints this when the bot is online

#.-------------- Handling messages, the AI part: ---------------------------.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore own messages

    # Trigger if the bot is mentioned (e.g., @Randomly)
    if bot.user in message.mentions:
        user_input = message.content.replace(f"<@{bot.user.id}>", "").strip()  # type: ignore # here aswell  -# Remove mention from text 
        
        if not user_input:
            responses = ["yo~ here to help", "here", "what?", "need help?", "yo"]
            await message.reply(random.choice(responses))
            return

# Show "typing..." while thinking
        async with message.channel.typing():
            try:
                # Ask Gemini for a response
                response = await asyncio.to_thread(lambda: model.generate_content(user_input))
                reply = response.text

 # Send the reply (split if too long for Discord)
                if len(reply) > 2000:
                    chunks = [reply[i:i+1990] for i in range(0, len(reply), 1990)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(reply)
            except Exception as e:
                await message.reply(f"Oops! Error: {e}") #sends the error so i dont hurt my head

    await bot.process_commands(message)  # For future commands          

print(f"TOKEN loaded: {TOKEN}")
bot.run(TOKEN)