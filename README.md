# Secure Encrypted Gateway (S.E.G)

A self-contained secure communication project built entirely in Python, designed to encrypt messages and files on windows using a shared password. Only users with the same password and the program can access the data.

---

## 🔧 Requirements & Setup

### Download & Install

1. Download the repository (ZIP or Git).
2. Open a CMD window in the project folder.
3. Run:
   ```
   pip install -r requirements.txt
   ```
4. Launch the app with:
   ```
   python S.E.G.py
   ```

> You must have **Python 3** installed!

---

## 🔐 Features

### 1. Login

- Default credentials: `admin admin`
- Password input is hidden for security.
- 3 incorrect attempts will shut down the app.

---

### 2. Shared Password Encryption

- Prompted after login.
- Used for both encryption and decryption of messages and files.
- All users must use the **same shared password**.

---

### 3. Main Menu Options

- `[1] Encode Message` – Encrypt a text message.
- `[2] Decode Message` – Decrypt a text message.
- `[3] Clear Console` – Clears the screen.
- `[4] Messages` – Encrypted messaging system (CLI + GUI).
- `[5] File Encryption/Decryption` – Encrypt or decrypt files.
- `[6] Help` – Display help instructions.
- `[7] Exit` – Close the application.

---

### 4. Encrypted Messaging System

- Send encrypted messages using Firebase.
- Securely view inbox and delete messages.
- Works only if sender and receiver use the same shared password.

---

### 5. File Encryption/Decryption

- Encrypts files into `.enc` format.
- Decrypts to `.dec` format.
- To restore, rename `.dec` file to its original extension.

---

### 6. Platform

- Built specifically for **Windows**.
- Requires a **Firebase Realtime Database** (see below).
- Default login credentials (`admin/admin`) can be changed in the script.

---

### 7. Convert to EXE

To make a standalone Windows executable:

1. Open CMD as Administrator.
2. Run:
   ```
   pip install pyinstaller
   ```
3. Build:
   ```
   python -m PyInstaller --onefile S.E.G.py
   ```
4. Find the EXE in the `dist` folder.

---

## 🔧 Firebase Setup Instructions

### Step 1: Create Firebase Project

- Visit: https://console.firebase.google.com
- Create a new project.

### Step 2: Enable Realtime Database

- Navigate to **Build > Realtime Database**
- Click "Create Database", choose a location, and select **test mode**.
- Click **Enable**.

### Step 3: Copy Database URL

- Use a URL like:
  ```
  https://your-project-id.firebaseio.com/
  ```
- Set it in your script:
  ```python
  FIREBASE_URL = "https://your-project-id.firebaseio.com/messages.json"
  ```

### Step 4 (Optional): Open Rules for Testing

In the Rules tab, replace with:

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

> ⚠️ This makes your database public — do not use in production.

---

## ✅ Summary

- Encrypt & decrypt messages and files.
- Use Firebase as a secure cloud message board.
- Share passwords safely to ensure end-to-end encryption.

---

**Made by execRooted**
