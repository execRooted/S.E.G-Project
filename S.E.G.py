import tkinter as tk
import os
from tkinter import simpledialog, scrolledtext
import requests, time, json, os, base64, hashlib, getpass, sys, threading
from cryptography.fernet import Fernet
import shutil
import requests
import random


os.system('title Secure Encrypted Gateway Program - by execRooted')

# === Terminal Colors ===
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# === CONFIGURATION ===
FIREBASE_URL = "yourFirebaseURL"
SALT = b"SEG-SALT-FIXED"
cipher = None
has_cleared_once = False
has_displayed_menu_once = False
has_displayed_messages_once = False




def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def typewriter_inline(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def prompt_shared_password():
    global cipher
    typewriter(f"{YELLOW}=== ENCRYPTION SETUP ==={RESET}", 0.04)
    for attempt in range(3):
        password = getpass.getpass("Enter shared password: ").strip()
        key = base64.urlsafe_b64encode(
            hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000, dklen=32)
        )
        try:
            test_cipher = Fernet(key)
            test_cipher.encrypt(b"test")
            cipher = test_cipher
            print(f"{GREEN}Shared password accepted.{RESET}\n")
            return True
        except Exception:
            print(f"{RED}Invalid shared password.{RESET}")
    print(f"{RED}Failed to verify shared password.{RESET}")
    exit()

def encode(msg):
    token = cipher.encrypt(msg.encode())
    return base64.urlsafe_b64encode(token).decode()

def decode(h):
    try:
        padded = h + ('=' * (-len(h) % 4))
        token = base64.urlsafe_b64decode(padded)
        return cipher.decrypt(token).decode()
    except Exception:
        return f"{RED}<Invalid, altered hash or not same shared password>{RESET}"

def progress_bar(task="Verifying", duration=1.5):
    sys.stdout.write(f"{CYAN}{task}: [")
    sys.stdout.flush()
    for _ in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / 20)
    sys.stdout.write(f"]{RESET}\n")

def login():
    correct_user = "admin"
    correct_pass = "admin"
    typewriter(f"{YELLOW}=== S.E.G. LOGIN ==={RESET}", delay=0.04)
    for attempt in range(3):
        user = input("Username: ").strip()
        pw = getpass.getpass("Password: ").strip()
        print()
        progress_bar("Verifying", duration=1.2)
        if user == correct_user and pw == correct_pass:
            print(f"{GREEN}Access Granted.{RESET}\n")
            return True
        print(f"{RED}Invalid credentials.{RESET}\n")
    print(f"{RED}Too many failed attempts.{RESET}")
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{YELLOW}Exiting in {i}...{RESET}")
        sys.stdout.flush()
        time.sleep(1)
    print()
    exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(f"""{BLUE}
   \\     /  
    \\   /   
     \\ /    
      |     
      |     
      |     
      |     
   _________
  |   SEG   |
  |_________|
{RESET}""")

def exit_countdown():
    print(f"{CYAN}Session ended. Goodbye!{RESET}")
    for i in range(5, 0, -1):
        sys.stdout.write(f"{RED}Exiting in {i}...{RESET}\r")
        sys.stdout.flush()
        time.sleep(1)
    print()

def encode_msg(message):
    return cipher.encrypt(message.encode()).decode()

def decode_msg(token):
    try:
        return cipher.decrypt(token.encode()).decode()
    except Exception:
        return "<Not the same shared password>"

def send_message(sender, recipient, message):
    payload = {
        "to": recipient,
        "from": sender,
        "content": encode_msg(message),
        "timestamp": time.time()
    }
    r = requests.post(FIREBASE_URL, json=payload)
    return r.ok

def get_messages(username):
    try:
        r = requests.get(FIREBASE_URL)
        if r.status_code != 200:
            return []
        all_messages = r.json()
        if not isinstance(all_messages, dict):
            return []
        return [(msg_id, msg) for msg_id, msg in all_messages.items() if msg.get("to") == username]
    except Exception:
        return []

def delete_message(msg_id):
    url = FIREBASE_URL.replace(".json", f"/{msg_id}.json")
    requests.delete(url)










def terminal_chat():
    user = input("Your username: ").strip()
    while True:
        print(f"\n{CYAN}[1]{RESET} Send Message")
        print(f"{CYAN}[2]{RESET} Check Inbox")
        print(f"{CYAN}[3]{RESET} Delete All Inbox Messages")
        print(f"{CYAN}[4]{RESET} Exit Messaging")
        choice = input(f"{YELLOW}Choice: {RESET}").strip()
        if choice == "1":
            to = input("To: ").strip()
            msg = input("Message: ").strip()
            if send_message(user, to, msg):
                print(f"{GREEN}[+] Message sent successfully{RESET}")
            else:
                print(f"{RED}[!] Failed to send message{RESET}")
        elif choice == "2":
            msgs = get_messages(user)
            if not msgs:
                print(f"{CYAN}[i] No new messages.{RESET}")
                continue
            for msg_id, msg in msgs:
                print(f"{BLUE}From: {msg.get('from')}{RESET}")
                print(f"{CYAN}{decode_msg(msg.get('content'))}{RESET}\n")
                delete_message(msg_id)
        elif choice == "3":
            msgs = get_messages(user)
            for msg_id, _ in msgs:
                delete_message(msg_id)
            print(f"{RED}[!] All messages deleted.{RESET}")
        elif choice == "4":
            break
        else:
            print(f"{RED}Invalid choice{RESET}")



def file_encryption():
    while True:
        print(f"{CYAN}File Encryption/Decryption{RESET}")

      
        typewriter(f"{GREEN}[1]{RESET} Encrypt a file", delay=0.04)
        typewriter(f"{GREEN}[2]{RESET} Decrypt a file", delay=0.04)
        typewriter(f"{GREEN}[3]{RESET} Back", delay=0.04)

        choice = input(f"{YELLOW}Choice: {RESET}").strip()

        if choice == "1":
            
            filepath = input(f"{YELLOW}Enter file path to encrypt: {RESET}").strip()
            if not os.path.exists(filepath):
                print(f"{RED}File does not exist. Please try again.{RESET}")
                continue
            
           
            with open(filepath, 'rb') as file:
                file_data = file.read()
            
            encrypted_data = cipher.encrypt(file_data)
            
          
            encrypted_filepath = f"{os.path.splitext(filepath)[0]}.enc"  
            
            with open(encrypted_filepath, 'wb') as enc_file:
                enc_file.write(encrypted_data)
            
           
            os.remove(filepath)
            
            
            typewriter(f"{GREEN}File encrypted successfully: {encrypted_filepath}{RESET}", delay=0.04)
            typewriter(f"{CYAN}Original file has been deleted.{RESET}", delay=0.04)
            break  # Exit the loop after success

        elif choice == "2":
            
            filepath = input(f"{YELLOW}Enter file path to decrypt: {RESET}").strip()
            if not os.path.exists(filepath):
                print(f"{RED}File does not exist. Please try again.{RESET}")
                continue 
            
           
            if not filepath.endswith(".enc"):
                print(f"{RED}File does not have the correct '.enc' extension. Please try again.{RESET}")
                continue  
            
            
            with open(filepath, 'rb') as file:
                file_data = file.read()
            
            try:
                decrypted_data = cipher.decrypt(file_data)
                
                decrypted_filepath = f"{os.path.splitext(filepath)[0]}.dec" 
                
                with open(decrypted_filepath, 'wb') as dec_file:
                    dec_file.write(decrypted_data)
                
                
                os.remove(filepath)
                
               
                typewriter(f"{GREEN}File decrypted successfully: {decrypted_filepath}{RESET}", delay=0.04)
                typewriter(f"{CYAN}Encrypted file (.enc) has been deleted.{RESET}", delay=0.04)
                break 
            except Exception:
                print(f"{RED}Failed to decrypt the file. Incorrect password? Please try again.{RESET}")
                continue  

        elif choice == "3":
            
            return  
        
        else:
            print(f"{RED}Invalid option. Please select a valid option.{RESET}")
            continue  



def gui_chat():
    global cipher
    if cipher is None:
        prompt_shared_password()

    root = tk.Tk()
    root.withdraw()
    sender = simpledialog.askstring("Username", "Enter your username:")
    if not sender:
        return
    recipient = simpledialog.askstring("Recipient", "Send message to:")
    if not recipient:
        return


    chat = tk.Toplevel()
    chat.title(f"Chat with {recipient}")
    chat.configure(bg="#e6f0ff")
    chat.geometry("400x500")
    chat.resizable(False, False)

    txt_area = scrolledtext.ScrolledText(chat, bg="#f0f8ff", state="disabled", wrap=tk.WORD)
    txt_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(chat, width=50)
    entry.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)

    shown_message_ids = set()


    def refresh():
        while True:
            msgs = get_messages(sender)
            if msgs:
                txt_area.configure(state="normal")
                for msg_id, msg in msgs:
                    if msg_id in shown_message_ids:
                        continue
                    frm = msg.get("from", "Unknown")
                    decoded = decode_msg(msg["content"])
                    txt_area.insert(tk.END, f"{frm}: {decoded}\n")
                    shown_message_ids.add(msg_id)
                    delete_message(msg_id)
                txt_area.configure(state="disabled")
                txt_area.see(tk.END)
            time.sleep(2)


    def send():
        msg = entry.get().strip()
        if msg:
            if send_message(sender, recipient, msg):
                txt_area.configure(state="normal")
                txt_area.insert(tk.END, f"{sender}: {msg}\n")
                txt_area.configure(state="disabled")
                txt_area.see(tk.END)
                entry.delete(0, tk.END)

    entry.bind("<Return>", lambda event: send())

    threading.Thread(target=refresh, daemon=True).start()
    chat.mainloop()




def display_help():
    clear()

    help_text = """
    
   # Secure Encrypted Gateway (S.E.G)

*This is a self-contained project, made 100% in Python. It includes a list of features, including:*

---

## **1. Login**

- The program requires you to log in using a username and password (default: **admin admin**).
- If you do not see the password as you type, don't worry — it behaves like Linux terminals where input is hidden.
- You have **3 attempts** to enter the correct credentials. After that, the program will shut down.

---

## **2. Shared Password for Encryption**

- After logging in, you'll be prompted to enter a **shared password**.
- This password is used to **encrypt and decrypt** messages and files.
- All users must enter the **same shared password** to exchange messages and files successfully.

---

## **3. Main Menu**

After login and encryption setup, the main menu offers the following options:

- **[1] Encode Message** – Encrypt a message using the shared password.
- **[2] Decode Message** – Decrypt an encrypted message using the shared password.
- **[3] Clear Console** – Clears the screen and re-displays the logo.
- **[4] Messages** – Access the encrypted messaging system (supports both terminal and GUI).
- **[5] File Encryption/Decryption** – Encrypt or decrypt files.
- **[6] Help** – Display this help section.
- **[7] Exit** – Exit the program.

---

## **4. Encrypted Messaging System**

- Send and receive **encrypted messages** to/from other users.
- Choose a recipient, type your message, and ensure all parties are using the **same shared password**.
- You can also check your inbox and delete messages securely.

---

## **5. File Encryption/Decryption**

- Encrypt files to generate a `.enc` version.
- Decrypt files to generate a `.dec` version.
- To restore the original file, change the extension of the `.dec` file back to its original format.

---

## **6. Platform**

- This program is developed **specifically for Windows**.
- You need a **Firebase Realtime Database URL** – paste it into the `FIREBASE_URL` variable in the script.
- To modify the default `admin`/`admin` login, change the values of the `correct_user` and `correct_pass` variables.

---

## **7. Making an Executable (EXE)**

You can convert the script into an executable using **PyInstaller**:

1. Open **CMD as Administrator**
2. Run: `pip install PyInstaller`
3. Build: `python -m PyInstaller --onefile path/to/S.E.G.py`
4. Go to the `dist` folder – your `.exe` file will be there.
5. Done!

---

## **8. Firebase Setup Instructions**

To enable encrypted messaging and file storage features, you need to configure a Firebase Realtime Database:

### **Step 1: Create a Firebase Project**

- Visit: [https://console.firebase.google.com](https://console.firebase.google.com)
- Click **"Add Project"** and follow the setup steps.
- Once created, go to your project dashboard.

### **Step 2: Enable Realtime Database**

- Go to **Build > Realtime Database**
- Click **"Create Database"**
- Choose a location and select **Start in test mode**
- Click **"Enable"**

### **Step 3: Set the Firebase URL**

- After enabling, copy your database URL, e.g.:

```
https://your-project-id.firebaseio.com/
```

- Set it in your Python code like this:

```python
FIREBASE_URL = "https://your-project-id.firebaseio.com/messages.json"
```

*Make sure to include `/messages.json` at the end.*

### **Step 4: (Optional) Open Access Rules for Testing**

For easy testing, go to the **Rules** tab and replace with:

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

*Warning: These rules make your database public. Do not use in production.*

---

**Enjoy using the Secure Encrypted Gateway Program. Keep your shared password safe and secure.**

**Made by execRooted**

    """
    print(help_text)

    
    input(f"{YELLOW}Press Enter to continue...{RESET}")

    
    clear()
    logo()

    




def main():
    global has_cleared_once, has_displayed_menu_once, has_displayed_messages_once
    clear()
    logo()
    login()
    prompt_shared_password()

    typewriter(f"{YELLOW}=== S.E.G. PROGRAM SYSTEM ==={RESET}\n", delay=0.04)

    while True:
        if not has_displayed_menu_once and not has_cleared_once:
            typewriter(f"{CYAN}Select Mode:{RESET}", delay=0.04)
            typewriter(f"{GREEN}[1]{RESET} Encode Message", delay=0.04)
            typewriter(f"{GREEN}[2]{RESET} Decode Message", delay=0.04)
            typewriter(f"{GREEN}[3]{RESET} Clear Console", delay=0.04)
            typewriter(f"{GREEN}[4]{RESET} Messages", delay=0.04)
            typewriter(f"{GREEN}[5]{RESET} File Encryption/Decryption", delay=0.04)
            typewriter(f"{GREEN}[6]{RESET} Help", delay=0.04)
            typewriter(f"{GREEN}[7]{RESET} Exit", delay=0.04)
            has_displayed_menu_once = True
        else:
            print(f"{CYAN}Select Mode:{RESET}")
            print(f"{GREEN}[1]{RESET} Encode Message")
            print(f"{GREEN}[2]{RESET} Decode Message")
            print(f"{GREEN}[3]{RESET} Clear Console")
            print(f"{GREEN}[4]{RESET} Messages")
            print(f"{GREEN}[5]{RESET} File Encryption/Decryption")
            print(f"{GREEN}[6]{RESET} Help")
            print(f"{GREEN}[7]{RESET} Exit")
            


        choice = input(f"{YELLOW}Choice: {RESET}").strip()

        if choice == "1":
            msg = input("Enter message: ").strip()
            if msg:
                print(f"{GREEN}Encoded: {CYAN}{encode(msg)}{RESET}\n")
        elif choice == "2":
            h = input("Enter encoded message: ").strip()
            print(f"{GREEN}Decoded: {CYAN}{decode(h)}{RESET}\n")
        elif choice == "3":
            clear()
            logo()
            has_cleared_once = True
        elif choice == "4":
            if not has_displayed_messages_once and not has_cleared_once:
                typewriter(f"\n{CYAN}[1]{RESET} Terminal Messaging", delay=0.04)
                typewriter(f"{CYAN}[2]{RESET} GUI Messaging", delay=0.04)
                typewriter(f"{CYAN}[3]{RESET} Back", delay=0.04)
                has_displayed_messages_once = True
            else:
                print(f"\n{CYAN}[1]{RESET} Terminal Messaging")
                print(f"{CYAN}[2]{RESET} GUI Messaging")
                print(f"{CYAN}[3]{RESET} Back")


            sub = input(f"{YELLOW}Choice: {RESET}").strip()
            if sub == "1":
                terminal_chat()
            elif sub == "2":
                gui_chat()
            elif sub == "3":
                continue
            else:
                print(f"{RED}Invalid option.{RESET}")
        elif choice == "6":
            display_help()
        elif choice == "7":
            exit_countdown()
            break
        elif choice == "5":
            file_encryption()
        else:

            print(f"{RED}Invalid choice{RESET}")
            
            


if __name__ == "__main__":
    main()
