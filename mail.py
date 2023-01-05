import smtplib

# Set the email server and login credentials
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("your_email@example.com", "your_password")

# Set the sender and recipient
sender = "your_email@example.com"
recipient = "recipient_email@example.com"

# Set the email subject and body
subject = "Test Message"
body = "Dear ... Please if you have received this mail."

# Set the message
message = f"Subject: {subject}\n\n{body}"

# Send the email
server.sendmail(sender, recipient, message)

# Close the server
server.quit()
