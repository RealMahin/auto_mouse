import pyautogui
from sys import argv

# DO NOT CHANGE FAILSAFE!! When the cursor stops moving...
# Move your mouse to the upper left corner of the screen to abort.
pyautogui.FAILSAFE = True

# Configure
script, task_counter = argv # determines what arguments are typed on the command line
task_number = int(task_counter) # converts tasks_counter from a string to an integer
position1_x, position1_y = 1799, 544
position2_x, position2_y = 1745, 602
position3_x, position3_y = 842, 670

# Options
pyautogui.PAUSE = 0.6 # how long the cursor stops at each coordinate
cursor_speed = 0.2 # minimum is 0.1
maximum_tasks = 100 # 100 is recommended


# Game Time
for i in range(task_number):
    if (task_number <= maximum_tasks):
        # 1: moves to 1st position and clicks
        pyautogui.moveTo(position1_x, position1_y, cursor_speed)
        pyautogui.click()
        print("1st Position")

        # 2: moves to 2nd position and clicks
        pyautogui.moveTo(position2_x, position2_y, cursor_speed)
        pyautogui.click()
        print("2nd Position")

        # 3: moves to 3rd position and clicks
        pyautogui.moveTo(position3_x, position3_y, cursor_speed)
        pyautogui.click()
        print("3rd Position")
    else:
        print("The maximum is 100")
        break