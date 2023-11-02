import img2pdf
import os
from datetime import datetime
try :
    def convert_images_to_pdf(folder_path, output_filename):
    
        images = os.listdir(folder_path)
        bytes_images = []
        for image in images:
            with open(os.path.join(folder_path, image), "rb") as image_file:
                bytes_images.append(image_file.read())
    
        pdf_data = img2pdf.convert(bytes_images)
        # Note : becareful you write correct output path folder.
        with open(os.path.join("<<<Your output folder path here>>>", output_filename), "wb") as output_file:
            output_file.write(pdf_data)

    # Your images folder path
    folder_path = input("Enter folder path : ")

    nowtime = datetime.now()
    nowtime = str(nowtime)[0:19]
    nowtime = nowtime.split(":")
    nowtime = ".".join(nowtime)
    nowtime = nowtime.split()
    nowtime = " ".join(nowtime)

    # If you want set date and time on the last of your file you cab enter "y". if not you can enter "n"
    timeop = input("Set Time in the last? (y/n) : ")
    
    if timeop == "y" :
        
        # This entry for your file path name. like : MyPDF 2023-2-11 12.13.14.pdf
        output_filename = input("Set OutPut name : ") + " " + nowtime + ".pdf"
        
    elif timeop == "n" :
        
        # This entry for your file path name with out date and time. like : MyPDF.pdf
        output_filename = input("Set OutPut name : ") + ".pdf"
        
    else :
        print("Please Enter something valid.\n")
        input("<Press Enter to continue>")
    
    convert_images_to_pdf(folder_path, output_filename)
    print("Convert finished.\n")
    input("<Press Enter to continue>")
except Exception as e :
    print("Something went wrong.\n"
          f"Error{e}\n")
    input("<Press Enter to continue>")
    
