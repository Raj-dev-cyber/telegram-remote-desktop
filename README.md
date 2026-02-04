# Telegram Remote PC Control Bot 🖥️🤖

Remote-control your Windows PC using a Telegram bot. Execute system commands, get status and IP info, receive live screenshots, and more — all securely from your Telegram account.

---

## Table of Contents
- [Features](#features)
- [Commands](#commands)
- [Requirements](#requirements)
- [Installation](#installation)
- [Create Your Telegram Bot](#create-your-telegram-bot)
- [Get Your Chat ID](#get-your-chat-id)
- [Configure the Script](#configure-the-script)
- [Run the Bot](#run-the-bot)
- [Run Automatically on Startup (Recommended)](#run-automatically-on-startup-recommended)
- [Important Notes & Troubleshooting](#important-notes--troubleshooting)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features
- ✅ Check if PC is online
- 🔒 Lock the computer
- 🔄 Restart the system
- 🛑 Shut down the system
- 🌐 View local and public IP addresses
- 📸 Capture and send live screenshots
- 🔁 Auto-reconnect / recovers after internet disconnection
- 🧠 Prevents duplicate command execution
- 💾 Persists last processed message across restarts
- 🔐 Only responds to your configured Telegram account

---

## Commands
| Command | Description |
|---|---|
| `/status` | Shows PC name and confirms it’s online |
| `/shutdown` | Shuts down the PC after 5 seconds |
| `/restart` | Restarts the PC |
| `/lock` | Locks the Windows session |
| `/ip` | Shows local & public IP addresses |
| `/screenshot` | Sends a screenshot of the current screen |

---

## Requirements
- Windows OS
- Python 3.8+
- Telegram account
- Python packages:
```bash
pip install requests pyautogui pillow
```

---

## Installation
1. Clone or download this repository.
2. Install the Python dependencies (see above).
3. Edit the script settings (see Configure the Script).

---

## Create Your Telegram Bot
1. Open Telegram and search for `@BotFather`.
2. Send `/start`.
3. Send `/newbot` and follow the prompts.
4. Copy the provided Bot Token.

---

## Get Your Chat ID
1. Send a message to your newly created bot.
2. Open in browser (replace `YOUR_BOT_TOKEN`):
```
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```
3. Look for `"chat":{"id":XXXXXXXX}` in the JSON response — that number is your `CHAT_ID`.

---

## Configure the Script
Open `bot.py` (or the main script) and set:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

Ensure the values are correct before running.

---

## Run the Bot
Start the bot from a command prompt:
```bash
python bot.py
```
You should see a message (in console or via Telegram) indicating the bot is active, e.g.:
> 🤖 Remote control system is now ACTIVE

---

## Run Automatically on Startup (Recommended)
Use Windows Task Scheduler:

1. Press Win + R → type `taskschd.msc` → Enter.
2. Click **Create Task**.
3. In **General**:
   - Name the task (e.g. "Telegram Remote PC Bot")
   - Select **Run whether user is logged on or not**
   - Check **Run with highest privileges**
4. In **Triggers**:
   - New → Begin the task: **At startup**
5. In **Actions**:
   - New → Action: **Start a program**
   - Program/script: path to your `python.exe` (e.g. `C:\Python38\python.exe`)
   - Add arguments: full path to `bot.py` (e.g. `C:\path\to\bot.py`)
6. Save the task. The bot will now run in the background each time the PC boots.

---

## Important Notes & Troubleshooting
- 🔒 Never share your bot token. If it is leaked, regenerate it via BotFather immediately.
- 📸 Screenshots cannot be captured while Windows is locked (lock screen limitation).
- If the bot stops responding after network changes, confirm the machine has internet and the script’s auto-reconnect logic is enabled.
- If commands appear duplicated, verify the bot’s message-processing persistence file is writable and the script user has correct permissions.

---

## How It Works
The script uses the Telegram Bot API long polling to receive commands and executes system-level actions on the PC. It includes protections for:
- Handling intermittent internet disconnections
- Avoiding duplicate processing of messages
- Restricting responses to the configured Telegram user only

---

## Future Improvements
- 🎙 Microphone recording command
- 📂 File download from PC
- 📊 System uptime and resource monitoring
- 🖱 Remote mouse/keyboard control

---

## Contributing
This project is intended for personal and educational use. If you want to contribute improvements:
1. Fork the repo
2. Create a branch with your feature/fix
3. Open a pull request describing your changes

---

## License
This project is for educational and personal use. Use responsibly.

---
If you’d like, I can also:
- Add badges (build/status/security) or a short GIF demo,
- Provide a minimal example of `bot.py` showing how BOT_TOKEN/CHAT_ID are used,
- Or create a ready-made Task Scheduler XML for import.
Which would you prefer next?
