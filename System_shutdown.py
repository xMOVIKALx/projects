import os
def app() :
    op = input("what do you want to do?\n"
           "1-Shutdown\n"
           "2-restart : ")
    if op == "1" :
        ok = input("are you sure? (y/n) : ")
        if ok == "y" :
            os.system("shutdown /s /t 1")
        elif ok == "n" :
            print("ok, if you want use this program again, restart the code.")
        else :
            print("invalid input")
    else :
        print("invalid input")
app()