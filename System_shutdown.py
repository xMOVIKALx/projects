import os
def app() :
    op = input("what do you want to do?\n"
           "1-Shutdown : ")
    time = int(input("How many more minutes? ( + I want shutdown now!) \n if you want shutdown now enter + : "))
    if time == "+" :
        ok = input("are you sure? (y/n) : ")
        if ok == "y":
            os.system("shutdown /s /t 1")
        elif ok == "n":
            print("ok, if you want use this program again, restart the code.")
        else:
            print("invalid input")

    else :
        time = time * 60
        ok = input("are you sure? (y/n) : ")
        if ok == "y" :
            os.system(f"shutdown /s /t {time}")
        elif ok == "n" :
            print("ok, if you want use this program again, restart the code.")
        else :
            print("invalid input")
app()
