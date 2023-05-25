P = 3.14
head = input("Enter shape for check module : "
             " 1-Parallelogram "
             " 2-Circle "
             " 3-Square "
             " 4-Rectangle "
             " 5-Triangle : ")
try :
    try:
        if head == "1" :
            def Parallelogram() :
                admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                if admin == "1" :
                    shorterside = float(input("Enter your shorter side : "))
                    longerside = float(input("Enter your longer side  : "))
                    if shorterside > longerside :
                        print("wrong size ! , longer side need to longer than shorter side !")
                    else :
                        perimeter = (shorterside + longerside)  * 2
                        print("your perimeter is :",perimeter)
                elif admin == "2" :
                    base = float(input("Enter your base : "))
                    height = float(input("Enter your height : "))
                    area = base * height
                    print("your area is :",area)
                else :
                    print("wrong input !")
        Parallelogram()
    except :
        pass
    try :
        if head == "2" :
            def Circle() :
                admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                if admin == "1" :
                    radius = float(input("Enter your radius : "))
                    perimeter = radius * 2 * P
                    print("your perimeter is :", perimeter)
                elif admin == "2" :
                    radius = float(input("Enter your radius : "))
                    area = radius * radius * P
                    print("your area is :",area)
                else :
                    print("wrong input !")
        Circle()
    except :
        pass
    try :
        if head == "3" :
            def Square() :
                admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                if admin == "1" :
                    side = float(input("Enter your side : "))
                    perimeter = side * 4
                    print("your perimeter is :", perimeter)
                elif admin == "2" :
                    side = float(input("Enter your side : "))
                    area = side * side
                    print("your area is :",area)
                else :
                    print("wrong input !")
        Square()
    except :
        pass
    try :
        if head == "4" :
            def Rectangle() :
                admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                if admin == "1" :
                    longerside = float(input("Enter your longer side : "))
                    shorterside = float(input("Enter your shorter side : "))
                    if shorterside > longerside :
                        print("wrong size ! , longer side need to longer than shorter side !")
                    else :
                        perimeter = (longerside + shorterside) * 2
                        print("your perimeter is :", perimeter)
                elif admin == "2" :
                    longerside = float(input("Enter your longer side : "))
                    shorterside = float(input("Enter your shorter side : "))
                    if shorterside > longerside :
                        print("wrong size ! , longer side need to longer than shorter side !")
                    else :
                        area = longerside * shorterside
                        print("your area is :",area)
                else :
                    print("wrong input !")
        Rectangle()
    except :
        pass
    try :
        if head == "5" :
            admin1 = input("which one is your Triangel ? : 1-Equilateral triangle , 2-Isosceles triangle , 3-Right triangle : ")
            if admin1 == "1" :
                def EquilateralTriangle() :
                    admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                    if admin == "1" :
                        side = float(input("Enter your side : "))
                        perimeter = side * 3
                        print("your perimeter is :", perimeter)
                    elif admin == "2" :
                        base = float(input("Enter your base : "))
                        height = float(input("Enter your height : "))
                        area = (base * height) / 2
                        print("your area is :",area)
                    else :
                        print("wrong input !")
        EquilateralTriangle()
    except :
        pass
    try :
        if head == "5" :
            if admin1 == "2" :
                def IsoscelesTriangle() :
                    admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                    if admin == "1" :
                        longerside = float(input("Enter your longer side : "))
                        shorterside = float(input("Enter your shorter side : "))
                        if shorterside > longerside :
                            print("wrong size ! , longer side need to longer than shorter side !")
                        else :
                            perimeter = (longerside * 2) + shorterside
                            print("your perimeter is :", perimeter)
                    elif admin == "2" :
                        base = float(input("Enter your base : "))
                        height = float(input("Enter your height : "))
                        area = (base * height) / 2
                        print("your area is :", area)
                    else :
                        print("wrong input !")
        IsoscelesTriangle()
    except :
        pass
    try :
        if head == "5" :
            if admin1 == "3" :
                def RightTriangle() :
                    admin = input("perimeter or area ? : 1-perimeter , 2-area : ")
                    if admin == "1":
                        longerside = float(input("Enter your longer side : "))
                        middleside = float(input("Enter your middle side : "))
                        shorterside = float(input("Enter your shorter side : "))
                        if longerside < middleside or middleside < shorterside or longerside < shorterside :
                            print("wrong size ! , longer side need to longer than middle side and middle side need to longer than shorter side !")
                        else:
                            perimeter = shorterside + longerside + middleside
                            print("your perimeter is :", perimeter)
                    elif admin == "2" :
                        base = float(input("Enter your base : "))
                        height = float(input("Enter your height : "))
                        area = (base * height) / 2
                        print("your area is :", area)
                    else:
                        print("wrong input !")
        RightTriangle()
    except :
        pass
except :
    pass