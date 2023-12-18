import pywhatkit
import time
from datetime import datetime, timedelta
import random

# Replace 'friend's_name' with your friend's name as saved in your WhatsApp contacts
# friend_name = "friend's_name"

# Messages to be sent
messages = [
    "Watch...",
    "Did you know?...",
    "Here's a joke for you...",
    "Random fact of the day...",
    "Hope you're having a great day!"
]

# Function to send messages
def send_message():
    message = "Watch Gen V 1st episode"
    # Replace '+1234567890' with your friend's phone number
    pywhatkit.sendwhatmsg(f"+18625889147", message, datetime.now().hour, datetime.now().minute + 1)
    print(f"Message sent at {datetime.now().strftime('%H:%M:%S')}: {message}")

# Calculate the number of messages to send
num_of_messages = 100  # Change this number as desired

# Sending messages
for _ in range(num_of_messages):
    send_message()
