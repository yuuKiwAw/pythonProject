import barcode

from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import *
from barcode.writer import ImageWriter

def main():
    window = Tk()
    window_Width = window.winfo_screenwidth()
    window_Height = window.winfo_screenheight()
    window.title("barcode")
    ww = 400
    wh = 180
    x = (window_Width-ww)/2
    y = (window_Height-wh)/2
    window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
    
    
    code_Number = input("enter the barcode number:")   #获取用户输入的值
    
    def toImage():      #转成png图片格式 
        code_128 =  barcode.get('code128',code_Number,writer=ImageWriter())
        file_name = code_128.save('code') 
    
    toImage()

    window.mainloop()


if __name__ == "__main__":
    main()