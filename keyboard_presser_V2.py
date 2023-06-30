import keyboard
op = input("What key do you want repeat? : ")
while True :
    keyboard.press(op)
    keyboard.release(op)