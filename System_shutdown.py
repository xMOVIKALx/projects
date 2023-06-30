import os
def app() :
    op = input("what do you want to do?\n"
               "Hibernate and sleep just for now. you can't timing for them.\n"
           "1-Shutdown\n"
               "2-Restrat\n"
               "3-sleep\n"
               "4-Hibernate : "
               )
    daghighe = int(input("How many more minutes? : "))
    if op == "1" :
        zaman = daghighe * 60
        ok = input("are you sure? (y/n) : ")
        if ok == "y" :
            os.system(f"shutdown /s /t {zaman}")
        elif ok == "n" :
            print("ok, if you want use this program again, restart the code.")
        else :
            print("invalid input.")
    elif op == "2" :
        zaman = daghighe * 60
        ok = input("are you sure? (y/n) : ")
        if ok == "y":
            os.system(f"shutdown /r /t {zaman}")
        elif ok == "n":
            print("ok, if you want use this program again, restart the code.")
        else:
            print("invalid input.")
    elif op == "3" :
        zaman = daghighe * 60
        ok = input("are you sure? (y/n) : ")
        if ok == "y" :
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif ok == "n" :
            print("ok, if you want use this program again, restart the code.")
        else :
            print("invalid input.")
    elif op == "4" :
        zaman = daghighe * 60
        ok = input("are you sure? (y/n) : ")
        if ok == "y" :
            os.system(f"shutdown /h")
        elif ok == "n" :
            print("ok, if you want use this program again, restart the code.")
        else :
            print("invalid input.")
    else :
        print("invalid input.")
app()
