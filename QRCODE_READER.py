#LIBRARIES USED
import qrcode
from tkinter import *
from tkinter import messagebox

#CREATING THE WINDOW
wn = Tk()
wn.title('QR CODE GENERATOR')
wn.geometry('700x700')
wn.config(bg = 'SteelBlue3')

#FUNCTIONS
def generateCode():
    #creating QR
    qr = qrcode.QRCode(version = size.get(),
                       box_size=10,
                       border=5)
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()
    fileDirec = loc.get()+'\\'+name.get()
    img.save(f'{fileDirec}.png')
    messagebox.showinfo("QR CODE GENERATED,","QR CODE SAVED SUCCESSFULLY")

#Labels
headingFrame = Frame(wn,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame,text="GENERATE QR CODE WITH THIS",bg='azure',font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

#TAKE INPUT IN FORM
Frame1 = Frame(wn,bg="SteelBlue3")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

label1= Label(Frame1,text="ENTER TEXT OR URL:  ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2,relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#GETTING INPUT OF QR SAVE LOCATION
Frame2 = Frame(wn,bg="SteelBlue3")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

label2 = Label(Frame2,text="Enter The Location To Save The QR",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label2.place(relx=0.05,rely=0.2,relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#GETTING INPUT QR CODE IMAGE NAME
Frame3 = Frame(wn,bg="SteelBlue3")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text="Enter The Name Of The QR CODE",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2,relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#Getting The Input FOR QR CODE SIZE
Frame4 = Frame(wn,bg="SteelBlue3")
Frame4.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)

label4 = Label(Frame4,text="Enter The Size From 1 to 40, With 1 being 21x21:  ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label4.place(relx=0.05,rely=0.2,relheight=0.2)

size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4,relwidth=0.5,relheight=0.2)

#Buttons TO GENERATE AND SAVE
button = Button(wn,text="Generate CODE",font=('Courier',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.9,relwidth=0.25,relheight=0.05)

#RUNS UNTIL CLOSED MANUALLY
wn.mainloop()

