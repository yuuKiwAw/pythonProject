import barcode

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import *
from barcode.writer import ImageWriter

def main():
    window = tk.Tk()
    window_Width = window.winfo_screenwidth()
    window_Height = window.winfo_screenheight()
    window.title("barcode")
    ww = 400
    wh = 400
    x = (window_Width-ww)/2
    y = (window_Height-wh)/2
    window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
    
   
    def toImage():      #转成png图片格式 
        var = code_Number_Label.get()
        code_128 =  barcode.get('code128',var,writer=ImageWriter())
        file_name = code_128.save('code') 

    ######################----GUI界面----######################
    code_creater_Button = Button(window,width=10,height=1,text="Create",command=toImage)
    code_creater_Button.place(relx=0.5,rely=0.2,anchor='center')
    code_Number_Label = Entry(window,width=30)
    code_Number_Label.place(relx=0.5,rely=0.1,anchor='center')
    ######################----GUI界面----######################
    
    window.mainloop()


if __name__ == "__main__":
    main()
