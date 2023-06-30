import pyautogui
import time
delay = float(input("Enter delay time (0.1 second) : "))
op = input("What key do you want repeat? : ")
delay = delay/10
while True:
  pyautogui.press(op)
  time.sleep(delay)