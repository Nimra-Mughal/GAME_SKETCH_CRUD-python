from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title('TechVidvan Text from image project')

# newline= Label(root)
uploaded_img=Label(root)
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )





def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        # show_extract_button(path)
    except:
        pass

uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
# newline.configure(text='\n')
# newline.pack()
uploaded_img.pack()

root.mainloop()