import random
try :
    def dice() :
        op = int(input("How many dice do you want? : "))
        for i in range(1,op+1) :
            print("dice",i,"=",random.randint(1,6))
        restart()
except :
    print("invalid input, pls try again.")
try :
    def restart() :
        restart = input("do you want dice again ? (y/n) : ")
        if restart == "y" :
            dice()
        elif restart == "n" :
            print("Good bye.")
        else :
            print("invalid input. try again.")
except :
    print("invalid input. try again.")
dice()