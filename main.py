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

        img3=Image.open(r"E:\FACE @\college_images\bg1.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1330,height=35)
        
        # main_frame=Frame(bg_img,bd=2)
        # main_frame.place(x=5,y=55,width=1450,height=600)

        #Student Button
        img4=Image.open(r"E:\FACE @\college_images\student-portal_1.jpg")
        img4=img4.resize((220,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=50,width=220,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=200,width=220,height=30)

        # Detection Button
        img5=Image.open(r"E:\FACE @\college_images\face_detector1.jpg")
        img5=img5.resize((220,150),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=420,y=50,width=220,height=150)

        b1_1=Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=420,y=200,width=220,height=30)


         # Attendance face Button
        img6=Image.open(r"E:\FACE @\college_images\Att.jpeg")
        img6=img6.resize((220,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=720,y=50,width=220,height=150)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=720,y=200,width=220,height=30)


        # Help Button
        img7=Image.open(r"E:\FACE @\college_images\help.jpg")
        img7=img7.resize((220,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1020,y=50,width=220,height=150)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1020,y=200,width=220,height=30)

        # Train Button
        img8=Image.open(r"E:\FACE @\college_images\Train.jpg")
        img8=img8.resize((220,150),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=120,y=300,width=220,height=150)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=450,width=220,height=30)

        # Photos Button
        img9=Image.open(r"E:\FACE @\college_images\face.jpg")
        img9=img9.resize((220,150),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=420,y=300,width=220,height=150)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=420,y=450,width=220,height=30)



