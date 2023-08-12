#Last-Updated-26-10-2022
#Designed-and-Developed-By-IshuGupta
#Pdf-locker-Suite-2022

#import functions from modules
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import messagebox
import os 

#Windows_size,Title,Resizable
root=Tk()
root.title("PDF File Locker Suite")
root.geometry("580x510+300+100")
root.resizable(False,False)

#function_to_browse_files
def browse():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select PDF File",
                                            filetype=(('PDF FIle','*.pdf'),('all files','*.*')))
        entry1.insert(END,filename)

#function_to_encrypt_pdf_file
def protect():
    mainfile=source.get()
    protectfile=target.get()
    code=password.get()

    if mainfile=="" and protectfile=="" and password.get()=="":
        messagebox.showerror("Invalid Entries","All Entries Are Empty!!")

    elif mainfile=="":
        messagebox.showerror("Invalid Source","Please Type or Select a Soure PDF FIle")

    elif protectfile=="":
        messagebox.showerror("Invalid New File Name","Please Type New Name of Protected PDF File")

    elif password.get() =="":
        messagebox.showerror("Invalid Password","Please Type Password!")

    else:
        try:
            out=PdfFileWriter()
            file = PdfFileReader(filename)
            num = file.numPages
            for idx in range(num):
                page=file.getPage(idx)
                out.addPage(page)
                
                out.encrypt(code)
                with open(protectfile, "wb") as f:
                    out.write(f)

                source.set("")
                target.set("")
                password.set("")

                messagebox.showinfo("Completed","PDF file has been successfully protected")
                
        except:
            messagebox.showerror("Invalid","Invalid Entry!")


#Title_image,Banner_image
image_icon=PhotoImage(file="C:/PdfLocker/image/logo.png")
root.iconphoto(False,image_icon)
Top_image=PhotoImage(file="C:/PdfLocker/image/banner.png")
Label(root,image=Top_image).pack()

#First_frame
frame=Frame(root,width=560,height=180,bd=4,relief=GROOVE)
frame.place(x=10,y=130)

#First_frame_source_label
source=StringVar()
Label(frame,text="Select PDF File",font="arial 10 bold",fg="#4c4542").place(x=20,y=10)

#First_frame_source_input
entry1=Entry(frame,width=35,textvariable=source,font="arial 15",bd=1)
entry1.place(x=20,y=45)

#First_frame_upload_button_and_its_image
Button_icon=PhotoImage(file="C:/PdfLocker/image/browse.png")
Button(frame,image=Button_icon,width=70,height=25,bd=2,relief=GROOVE,bg="#e4eefc",command=browse).place(x=420,y=44)

#First_frame_target_label
target=StringVar()
Label(frame,text="Create New PDF File Name (Include .pdf)",font="arial 10 bold",fg="#4c4542").place(x=20,y=85)

#First_frame_target_input
entry2=Entry(frame,width=30,textvariable=target,font="arial 15",bd=1)
entry2.place(x=20,y=115)

#Second_frame
frame=Frame(root,width=560,height=120,bd=4,relief=GROOVE)
frame.place(x=10,y=320)

#Second_frame_password_input
password=StringVar()
Label(frame,text="Set PDF Password",font="arial 10 bold",fg="#4c4542").place(x=20,y=10)
entry3=Entry(frame,width=30,textvariable=password,font="arial 15",bd=1)
entry3.place(x=20,y=45)

#footer_frame
frame=Frame(root,width=560,height=50)
frame.place(x=10,y=450)

#footer
footer1=StringVar()
Label(frame,text="PDF File Locker Suite 2022",font="arial 8 bold",fg="#4c4542").place(x=5,y=5)

footer2=StringVar()
Label(frame,text="Software is Designed and Developed By Ishu Gupta.",font="arial 8 bold",fg="#4c4542").place(x=5,y=20)

#Proceed_button
button_icon=PhotoImage(file="C:/PdfLocker/image/btn.png")
Protect=Button(root,text="Proceed To Set Password",compound=LEFT,image=button_icon,width=210,height=35,bd=2,relief=GROOVE,bg="#e4eefc",font="arial 9 bold",command=protect)
Protect.pack(side=BOTTOM,padx=5,pady=5)
Protect.place(x=340,y=450)


#program_ends.
root.mainloop()
