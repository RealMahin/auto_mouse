import pyautogui
from sys import argv

# DO NOT CHANGE FAILSAFE!! When the cursor stops moving...
# Move your mouse to the upper left corner of the screen to abort.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

script, task_counter = argv
task_number = int(task_counter)


# minimum is 0.1
cursor_speed = 0.2

# Game Time
for i in range(task_number):
    if (task_number <= 100):
        # 1: clicks the "Actions" button
        pyautogui.moveTo(1799, 544, cursor_speed)
        pyautogui.click()
        print("click Actions")

        # 2: moves to and clicks the "Close Job" button
        pyautogui.moveTo(1745, 602, cursor_speed)
        pyautogui.click()
        print("click Close Job")

        # 3: moves to and clicks the "Yes, close it!" button
        pyautogui.moveTo(842, 670, cursor_speed)
        pyautogui.click()
        print("click Yes, close it")
    else:
        print("The maximum is 100")
        break