import requests
import time
import os
import socket
import pyautogui

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

UPDATE_FILE = "last_update.txt"
last_update_id = None
boot_notified = False


# ------------------ INTERNET CHECK ------------------
def internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


# ------------------ LOAD/SAVE UPDATE ID ------------------
def load_last_update():
    if os.path.exists(UPDATE_FILE):
        with open(UPDATE_FILE, "r") as f:
            return int(f.read().strip())
    return None


def save_last_update(update_id):
    with open(UPDATE_FILE, "w") as f:
        f.write(str(update_id))


last_update_id = load_last_update()


# ------------------ NETWORK INFO ------------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# ------------------ TELEGRAM FUNCTIONS ------------------
def send_message(text):
    if not internet_available():
        return
    try:
        requests.post(f"{BASE_URL}/sendMessage", data={
            "chat_id": CHAT_ID,
            "text": text
        }, timeout=10)
    except requests.exceptions.RequestException:
        pass


def send_photo(photo_path):
    if not internet_available():
        return
    try:
        with open(photo_path, "rb") as photo:
            requests.post(
                f"{BASE_URL}/sendPhoto",
                data={"chat_id": CHAT_ID},
                files={"photo": photo},
                timeout=20
            )
    except:
        pass


def get_updates():
    global last_update_id

    if not internet_available():
        time.sleep(10)
        return []

    params = {"timeout": 30}
    if last_update_id:
        params["offset"] = last_update_id + 1

    try:
        response = requests.get(f"{BASE_URL}/getUpdates", params=params, timeout=35).json()
        return response.get("result", [])
    except requests.exceptions.RequestException:
        time.sleep(5)
        return []


# ------------------ COMMAND HANDLER ------------------
def handle_command(command):
    command = command.lower()

    if command == "/status":
        pc_name = socket.gethostname()
        send_message(f"✅ PC is online\n💻 Name: {pc_name}")

    elif command == "/shutdown":
        send_message("🛑 Shutting down PC...")
        os.system("shutdown /s /t 5")

    elif command == "/restart":
        send_message("🔄 Restarting PC...")
        os.system("shutdown /r /t 5")

    elif command == "/lock":
        send_message("🔒 Locking PC...")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif command == "/ip":
        local_ip = get_local_ip()

        if internet_available():
            try:
                public_ip = requests.get("https://api.ipify.org", timeout=5).text
            except:
                public_ip = "Unavailable"
        else:
            public_ip = "No Internet"

        send_message(f"📍 Local IP: {local_ip}\n🌐 Public IP: {public_ip}")

    elif command == "/screenshot":
        send_message("📸 Taking screenshot...")
        path = "screenshot.png"
        try:
            img = pyautogui.screenshot()
            img.save(path)
            send_photo(path)
        finally:
            if os.path.exists(path):
                os.remove(path)

    else:
        send_message("❓ Unknown command")


# ------------------ MAIN LOOP ------------------
while True:
    try:
        if not internet_available():
            time.sleep(10)
            continue

        if not boot_notified:
            send_message("🤖 Remote control system is now ACTIVE")
            boot_notified = True

        updates = get_updates()

        for update in updates:
            update_id = update["update_id"]

            if last_update_id and update_id <= last_update_id:
                continue

            last_update_id = update_id
            save_last_update(last_update_id)

            message = update.get("message")
            if not message:
                continue

            chat_id = str(message["chat"]["id"])
            text = message.get("text", "")

            if chat_id != CHAT_ID:
                continue

            handle_command(text)

    except Exception:
        time.sleep(5)
