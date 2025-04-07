import smtplib
import datetime as dt
import random
from email.message import EmailMessage

# Your Gmail credentials
myemail = "gokucodes247@gmail.com"
password = "xxxx xxxx xxxx xxxx"  # This is your 16-character App Password, not your regular Gmail password

# Get the current date and time
now = dt.datetime.now()

# Check if today is Monday (weekday() returns 0 for Monday)
if now.weekday() == 0:
    # Read quotes from the file using UTF-8 encoding to support special characters
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # Create an email message
    msg = EmailMessage()
    msg['Subject'] = "Monday Motivation 💪"
    msg['From'] = myemail
    msg['To'] = "gokucodes247@yahoo.com"
    msg.set_content(quote)

    # Send the email using Gmail SMTP server with port 587
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=myemail, password=password)
        connection.send_message(msg)
