🖥️ Telegram Remote PC Control Bot

Control your Windows PC remotely using a Telegram bot.
Run system commands, check status, get IP info, and even receive live screenshots — all from your phone.

🚀 Features

✅ Check if PC is online

🔒 Lock the computer

🔄 Restart the system

🛑 Shut down the system

🌐 View local and public IP address

📸 Capture and receive live screenshots

🔁 Auto-recovers after internet disconnection

🧠 Prevents duplicate command execution

💾 Remembers last processed message after restart

🔐 Only responds to your Telegram account

🧩 Commands List
Command	Description
/status	Shows PC name and confirms it’s online
/shutdown	Shuts down the PC after 5 seconds
/restart	Restarts the PC
/lock	Locks the Windows session
/ip	Shows local & public IP address
/screenshot	Sends a screenshot of the current screen
⚙️ Requirements

Windows OS

Python 3.8+

Telegram account

Python Libraries

Install dependencies:

pip install requests pyautogui pillow

🤖 Create Your Telegram Bot

Open Telegram

Search for @BotFather

Send /start

Send /newbot and follow instructions

Copy the Bot Token

🆔 Get Your Chat ID

Message your bot once

Open in browser:

https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates


Find "chat":{"id":XXXXXXXX}

That number is your CHAT_ID

🛠️ Setup the Script

Edit these lines in the script:

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

▶️ Run the Bot
python bot.py


You should receive:

🤖 Remote control system is now ACTIVE

🔁 Run Automatically on Startup (Recommended)

Use Windows Task Scheduler:

Press Win + R → type taskschd.msc

Click Create Task

Trigger → At startup

Action → Start program

Program: path to python.exe

Arguments: "C:\path\to\bot.py"

Enable:

Run whether user logged in or not

Run with highest privileges

Now the bot runs in the background every time the PC boots.

⚠️ Important Notes

🔒 Never share your bot token

If leaked, regenerate it using BotFather

Screenshot does not work on Windows lock screen

This project is for personal remote control use only

📌 How It Works

The script uses Telegram Bot API long polling to receive commands and execute system-level actions on the PC. It includes protection against:

Internet disconnections

Duplicate message processing

Unauthorized users

💡 Future Improvements

🎙 Microphone recording command

📂 File download from PC

📊 System uptime and resource monitoring

🖱 Remote mouse/keyboard control

📜 License

This project is for educational and personal use. Use responsibly.
