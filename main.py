from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # First Image
        img = Image.open(r"E:\FACE @\college_images\Stanford.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=400, height=130)

        # second Image
        img1 = Image.open(r"E:\FACE @\college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=500, height=130)

        # third Image
        img2 = Image.open(r"E:\FACE @\college_images\u.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=500, height=130)
