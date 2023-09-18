
import pyautogui
import keyboard
import time

DELAY_BETWEEN_CLICKS = 0.01 # In seconds

def main():
    is_running = False
    print("Script started. Press 'q' to stop/start the clicking.")

    try:
        while True:
            if is_running:
                pyautogui.click()
                time.sleep(DELAY_BETWEEN_CLICKS)
            
            if keyboard.is_pressed('q'):
                is_running = not is_running
                if is_running:
                    print("Clicking started.")
                else:
                    print("Clicking stopped.")
                time.sleep(1)  # To prevent multiple detections of the 'q' key press

    except KeyboardInterrupt:
        print("Script terminated.")

if __name__ == "__main__":
    main()