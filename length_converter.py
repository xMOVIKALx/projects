print("Welcome to lenght converter ! ")
def lengh_converter() :
    value = input("\n1-millimeter\n"
                  "2-centimeter\n"
                  "3-decimeter\n"
                  "4-meter\n"
                  "5-kilometer\n"
                  "\nselect : ")
    if value == "1" or "2" or "3" or "4" or "5" :
        try :
            if value == "1" :
                def millimeter() :
                    amount = float(input("Enter value ( millimeter ) : "))
                    mile = amount * 0.00000062137
                    yard = amount * 0.0010936133
                    foot = amount * 0.0032808399
                    inch = amount * 0.03937007874
                    print(
                        f"{amount} millimeter = {mile} mile \n"
                        f"{amount} millimeter = {yard} yard \n"
                        f"{amount} millimeter = {foot} foot \n"
                        f"{amount} millimeter = {inch} inch")
                millimeter()
            if value == "2" :
                def centimeter() :
                    amount = float(input("Enter value ( centimeter ) : "))
                    mile = amount * 0.0000062137
                    yard = amount * 0.010936133
                    foot = amount * 0.032808399
                    inch = amount * 0.3937007874
                    print(
                        f"{amount} centimeter = {mile} mile \n"
                        f"{amount} centimeter = {yard} yard \n"
                        f"{amount} centimeter = {foot} foot \n"
                        f"{amount} centimeter = {inch} inch")
                centimeter()
            if value == "3" :
                def decimeter() :
                    amount = float(input("Enter value ( decimeter ) : "))
                    mile = amount * 0.000062137
                    yard = amount * 0.10936133
                    foot = amount * 0.32808399
                    inch = amount * 3.937007874
                    print(
                        f"{amount} decimeter = {mile} mile \n"
                        f"{amount} decimeter = {yard} yard \n"
                        f"{amount} decimeter = {foot} foot \n"
                        f"{amount} decimeter = {inch} inch")
                decimeter()
            if value == "4" :
                def meter() :
                    amount = float(input("Enter value ( meter ) : "))
                    mile = amount * 0.00062137
                    yard = amount * 1.0936133
                    foot = amount * 3.2808399
                    inch = amount * 39.37007874
                    print(f"{amount} meter = {mile} mile \n"
                          f"{amount} meter = {yard} yard \n"
                          f"{amount} meter = {foot} foot \n"
                          f"{amount} meter = {inch} inch")
                meter()
            if value == "5" :
                def kilometer() :
                    amount = float(input("Enter value ( kilometer ) : "))
                    mile = amount * 0000.62137
                    yard = amount * 1093.6133
                    foot = amount * 3280.8399
                    inch = amount * 39370.07874
                    print(
                        f"{amount} kilometer = {mile} mile \n"
                        f"{amount} kilometer = {yard} yard \n"
                        f"{amount} kilometer = {foot} foot \n"
                        f"{amount} kilometer = {inch} inch")
                kilometer()

        except :
            print("\ninvalid input ! try again.")
            lengh_converter()
    else :
        print("\ninvalid input ! try again.")
        lengh_converter()
lengh_converter()
again = input("\ndo you want convert again ? (y/n) :")
if again == "y" :
    lengh_converter()
elif again == "n" :
    print("\nhave a good day !")
else :
    print("\ninvalid input !")
    lengh_converter()