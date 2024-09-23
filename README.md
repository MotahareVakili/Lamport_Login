# Lamport One-Time Password Login System

This project is a login system that implements the Lamport One-Time Password (OTP) protocol using hash chains. The Lamport OTP protocol provides an additional layer of security for user authentication by employing a series of hashed passwords that can only be used once, preventing the reuse of passwords even if intercepted.

## Project Objective
The main goal is to implement a secure login system that follows the Lamport OTP protocol, ensuring that each login attempt uses a unique, hashed password from a chain of hashes. This approach prevents replay attacks and enhances the overall security of the login process.

## How It Works
1. **Signup Process:**
   - The user provides a username and password during signup.
   - The password is hashed 10 times using SHA-256 to create a chain of hash values, starting from the original password.
   - The final hash (10th iteration) is stored in the database along with the initial counter `n = 10`.

2. **Login Process:**
   - The user enters their username and password.
   - The server responds with the current value of `n`, indicating how many hashes are left in the chain.
   - On the client side, the password is hashed `n` times using SHA-256.
   - The client sends this hashed value to the server.
   - The server hashes the stored password once and compares it to the received hashed value. If they match, the user is authenticated.
   - The value of `n` is decremented by 1, and the server updates the stored password with the received value.

3. **Password Change:**
   - Users can change their password, which resets the hash chain to start from the new password hashed 10 times.

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, JavaScript (for client-side hashing using CryptoJS)
- **Database:** SQLite or any database supported by Django ORM
- **Hashing Algorithm:** SHA-256 (Python's `hashlib` library)

## Key Features
- **Lamport OTP Protocol:** Implements a one-time password system using hash chains, preventing replay attacks.
- **Hash Chain Verification:** Uses SHA-256 to ensure secure password handling.
- **Interactive User Interface:** Provides login, signup, and change password forms for easy interaction.


## Run Project
Go to project root and execute the following command in console to run the Project:
```bash
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```

## Access the Application
To access the application, open your browser (preferably Firefox) and enter the following address:
```bash
http://localhost:8000
