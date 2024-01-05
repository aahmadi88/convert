import tkinter as tk
import pandas as pd
from tkinter import filedialog
from geopy.geocoders import Nominatim

# Building the GUI
def convert():
   # Get Input File Path
   input_file_path = filedialog.askopenfilename()
   # Read CSV
   df = pd.read_csv(input_file_path)
   # Get Output File Path and Name
   output_file_name = input_file_path.split("/")[-1][:-4]
   output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=output_file_name)
   lat1 = list(df.lat)
   long2 = list(df.long)
   merged_list = [(lat1[i],long2[i]) for i in range(0, len(lat1))]
   res = []
   for i in range(len(merged_list)):
       geoLoc = Nominatim(user_agent="GetLoc")
       locname = geoLoc.reverse('' + str(merged_list[i][0]) + ',' + str(merged_list[i][1]) + '')
       res.append(locname.address)
       
       path_to_file = "/test9.txt"
    
   with open(path_to_file, 'w',encoding="utf-8") as file:
        file.writelines(line+'\n' for line in res)
   read_file = pd.read_csv (r'/test9.txt')
   read_file.to_excel(output_file_path, index=False,encoding="utf-8")

   #df.to_excel(output_file_path, index=False)

# Creating Main Window
root = tk.Tk()
root.title("تبدیل مختصات )")
root.geometry("400x100")
root.config(bg="#f0f0f0")

# Adding a Button to the Window
convert_button = tk.Button(root, text="فایل را وارد کنید و ذخیره کیند ", command=convert, font=("Helvetica", 14), bg="#4caf50", fg="#ffffff")
convert_button.pack(pady=20)


# Adding File Dialog
filedialog = tk.filedialog 

# Running the GUI
root.mainloop()