import pyautogui
import time


message = f"Watch GenV Episode 1"

# Set the number of times you want to send the message
num_messages = 10  # Change this number if needed

# Loop to send messages
for i in range(num_messages):
    # Click on the WhatsApp icon or the chat where you want to send the message
    # Adjust the coordinates based on your screen resolution
    pyautogui.click(x=1499, y=972)  # Change the coordinates as per your screen

    # Type the birthday message and send it
    pyautogui.write(i)
    pyautogui.press('enter')

    # # Wait for 5 minutes
    # time.sleep(1)  # 300 seconds = 5 minutes
