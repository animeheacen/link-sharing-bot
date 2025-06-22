📱 Advanced Link Sharing Bot

Welcome to the Advanced Link Sharing Bot! 🚀

This bot helps you keep your Telegram channels safe from copyright issues by sharing links securely and efficiently. Whether you're an individual creator or a large group admin, this bot has your back! 💪


---

🌟 Features

📤 Secure Link Sharing

🔒 Advanced Protection from malicious links

🚀 Easy-to-use /start to get going

🛠️ Admin Controls for managing users & channels



---

🚀 Deployment

🌐 Deploy on Heroku

> Before deploying, fork the repo and rename it (optional)






---

⚙️ Deploy on Render, Koyeb, or Railway

These platforms require a web server to keep the bot alive, which is already supported.

🔸 Render

1. Connect your GitHub repo


2. Set start command to:

python3 main.py


3. Add environment variables


4. Use Dockerfile or auto Python environment



🔸 Railway

1. Import project from GitHub


2. Add environment variables


3. Set main.py as entry point



🔸 Koyeb

1. Create a service from GitHub


2. Choose Docker or Python runtime


3. Add required secrets and build




---

🔑 Environment Variables

Variable	Description

TG_BOT_TOKEN	Telegram Bot Token from @BotFather
APP_ID	Telegram API ID from my.telegram.org
API_HASH	Telegram API Hash
OWNER_ID	Your Telegram user ID
DATABASE_URL	MongoDB connection URI
DATABASE_NAME	MongoDB database name
PORT	Required for HTTP server (use 8080)
ADMINS (opt)	Space-separated admin user IDs



---

⚡ Bot Commands

Command	Description

/start	Start the bot and get welcome message
/broadcast	Send message to all users
/users	List all users
/channelpost	Generate invite links
/reqpost	Generate request links
/setchannel	Set a channel to manage
/delchannel	Remove a managed channel
/stats	View usage and uptime



---

🧑‍💻 Credits

Created by Hunter
Thanks to all contributors and testers 🙏


---

📞 Contact & Support

Telegram: @Otakukart7

Channel: Bots Kingdom



---

⭐ Thank you for using Advanced Link Sharing Bot ⭐

> Stay protected. Share securely. Grow safely. 🌐
