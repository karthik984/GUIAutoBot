import pyautogui

# Display the mouse position when moving it over the WhatsApp text box
print("Move your mouse over the WhatsApp text box and press Ctrl+C to exit.")
try:
    while True:
        current_position = pyautogui.position()
        print(current_position)
except KeyboardInterrupt:
    print("Script terminated.")
