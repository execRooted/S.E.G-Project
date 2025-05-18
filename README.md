 Welcome to the SEG Program! Here's how it works:

       *This is a self-dependable project, made 100% in Python. It includes a list of features, including:

    1. **Login**:
       - The program requires you to login with the username and password(default admin admin).
       - If you do not see the password, don't worry. It uses the same system like in Linux, so you can't see it, but it's beeing typed.
       - You'll have 3 attempts to enter the correct credentials, then the program will shut off.

    2. **Shared Password for Encryption**:
       - After logging in, you'll be prompted to enter a shared password. This password is used for encrypting and decrypting messages and files.
       - The shared password is verified before any encryption can happen.
       - The password should be the same across all users for successful encryption/decryption.

    3. **Main Menu**:
       - After logging in and setting up encryption, you'll see the main menu where you can:
         [1] Encode Message: Encrypt a message using the shared password.
         [2] Decode Message: Decrypt an encoded message using a shared password.
         [3] Clear Console: Clears the screen + logo.
         [4] Messages: Access the messaging system (both terminal-based and GUI-based).
         [5] File Encryption/Decryption: Encrypt or decrypt files using the shared password.
         [6] Help: Displays this help section.
         [7] Exit: Exit the program.

    4. **Messages**:
       - You can send and receive encrypted messages to/from other users with the same shared password.
       - To send a message, choose the recipient, the user, type the message and make sure the both of you(or more) have entered the same shared psw.
       - You can also check your inbox and delete messages.

    5. **File Encryption/Decryption**:
       - Encrypt and decrypt files by providing their file paths.
       - When encrypting a file, a `.enc` file will be created, and when decrypting, a `.dec` file will be generated. To take the file to its original state after decrypting,
         simply change the extension to what the file had before the encryption.

    * This program is made specificly for Windows.
    * You need a firebase URL. Just paste it in the FIREBASE_URL variable.!!!
    * To modify the default admin admin login, modify the correct_user and correct_pass variables.
    * To make this program a executable, I have only tested PyInstaller. This works fine. 
        List of commands to make it an exe:
             1. Open a cmd as a administartor;
             2. pip install PyInstaller
             3. python -m PyInstaller --onefile path/to/file/S.E.G.py
             4. Check inside the dist folder
             5. Done! Enjoy! :D
    
    Enjoy using the Secure Encrypted Gateway Program! Keep your shared password safe and secure.  
      
    
     *Made by execRooted*
