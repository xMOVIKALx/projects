from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active
sheet["B1"] = "Name :"
sheet["C1"] = "Title :"
sheet["D1"] = "Price :"
sheet["E1"] = "Wanted Time :"
sheet["F1"] = "Sheets :"
value = 2

print("Welcome")
def Excel() :
    member = input("1-person1\n"
          "2-person2 : ")
    if member ==  "1" :
        sheet[f"A{value}"] = "person1"
    elif member == "2" :
        sheet[f"A{value}"] = "person2"
    else :
        print("Invalid input.")
        Excel()
    name = input("Enter name : ")
    title = input("Enter title : ")
    price = input("Enter price : ")
    wanted_time = input("Enter wanted time(s) : ")
    sheets = input("Enter sheet(s) : ")
    sheet[f"B{value}"] = f"{name}"
    sheet[f"C{value}"] = f"{title}"
    sheet[f"D{value}"] = f"{price}"
    sheet[f"E{value}"] = f"{wanted_time}"
    sheet[f"F{value}"] = f"{sheets}"
Excel()

print(value)
workbook.save(filename="Excel_work.xlsx")