**TL;DR:**
A super simple Discord bot that lets you chat with Gemini AI. Just mention the bot in a server and it’ll reply~

Setup:

Put your Discord token and Gemini API key in a .env file (or hardcode if you don’t care).

Run it, ping it, get answers. Easy.



**Features:**

* Responds when mentioned in a server.
* Uses Google Gemini AI for replies.
  
**Setup:**

1. Clone the repo.
2. Create a `.env` file with your bot token and Gemini API key:

   ```
   TOKEN=your_discord_token
   GEMINI_API_KEY=your_gemini_api_key
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Run the bot:

   ```
   python gemeni.py
   ```

**Notes:**

* You can hardcode your tokens instead of using `.env`, but using `.env` is safer.
* Customize the bot’s “personality” in `system_instruction` in the code.
