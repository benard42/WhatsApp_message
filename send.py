import pywhatkit

# Set the time for the message (hour, minute)
time = (10, 36)

# Set the message and recipient
message = "Hello collin. i have used a program for sending a message to you"
to = "+256 760 897653"

# Send the message
pywhatkit.sendwhatmsg(to, message, time[0], time[1])
