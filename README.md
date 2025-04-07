# Monday Motivation Emailer ✉️💪

This Python script sends a **random motivational quote** to your email inbox every Monday using Gmail's SMTP server.

## 📌 Features

- Sends an email with a motivational quote
- Automatically triggers only on Mondays
- Securely sends emails using Gmail App Password

---

## 🔧 Requirements

- Python 3.6+
- Internet connection
- `quotes.txt` file containing motivational quotes (one per line)

---

## 📥 Setup Instructions

### 1. Create Gmail & Yahoo Accounts

- Create a [Gmail account](https://accounts.google.com/signup) if you don't already have one.
- Create a [Yahoo account](https://login.yahoo.com/account/create) if you're testing on a Yahoo receiver.

---

### 2. Enable 2-Step Verification in Gmail

1. Go to [Google My Account](https://myaccount.google.com/)
2. Click on **Security**
3. Under **"How you sign in to Google"**, enable **2-Step Verification**

---

### 3. Create an App Password

1. Go to the [App Passwords page](https://myaccount.google.com/apppasswords) (after enabling 2FA)
2. Select **Mail** as the app and **Windows Computer** as the device (or anything)
3. Click **Generate**
4. Copy the **16-character password** shown. It will look like this:  
   `abcd efgh ijkl mnop`
5. Replace the `password` variable in `main.py` with this app password (without spaces)

---

### 4. Email Server Info

Use the appropriate SMTP server address for your provider:

| Email Provider | SMTP Server              | Port |
|----------------|--------------------------|------|
| Gmail          | smtp.gmail.com           | 587  |
| Yahoo          | smtp.mail.yahoo.com      | 587  |
| Hotmail        | smtp.live.com            | 587  |
| Outlook        | outlook.office365.com    | 587  |

---

## 📄 quotes.txt Format

Make sure your `quotes.txt` file contains quotes like:

"Push yourself, because no one else is going to do it for you." “Your limitation—it’s only your imagination.” – Unknown "Great things never come from comfort zones.
