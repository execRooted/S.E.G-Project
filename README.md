# Secure Encrypted Gateway (S.E.G)
*This is a self-contained project, made 100% in Python. *
---
**Download**

This project is specificly for Windows, so just download the zip, and in a cmd window paste this command:
`pip install -r requirements.txt`
After that, simply open the file with python3. 

*You need to have python3 installed!*
---

It includes a list of features, including:*

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
