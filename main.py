from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from tkinter import font as tkFont
from tkinter import messagebox
import onetimepad
from stegano import exifHeader as aaa
import os


main = Tk()
main.title('Enc & Dec Panel ')
main.geometry('1920x795+-8+-3')
fontl = tkFont.Font(family='Algerian', size=32)

global image1
image1 = ImageTk.PhotoImage((Image.open("img/i3.png")))
#
# im = Image.open(fileopen)
# imm = im.resize((400, 200))
# imagee = ImageTk.PhotoImage(imm)

label1 = Label(main, image=image1)
label1.pack()

def changeOnHover(button, colorOnHover, colorOnLeave,text_color_hover,text_color_leave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,foreground=text_color_hover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave,foreground= text_color_leave))

def encode():
    main.withdraw()
    enc = Toplevel()
    enc.geometry('1920x795+-8+-3')
    fontl = tkFont.Font(enc,family='Algerian', size=32)
    enc.title('Enc Panel ')

    global image2
    image2 = ImageTk.PhotoImage(Image.open("img/bg2.jpg"))
    label2 = Label(enc, text="lalal", image=image2)
    label2.pack()

    LabelTitle = Label(enc,text="ENCODE", bg="black", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.3, rely=0.1)

    def openfile():
        global fileopen
        global imagee

        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg,png files", "*jpg *png"), ("all files", "*.*")))

        im=Image.open(fileopen)

        # compressor

        myHeight, myWidth = im.size
        im = im.resize((myHeight, myWidth),Image.ANTIALIAS)

        imm=im.resize((400,200))
        imagee = ImageTk.PhotoImage(imm)
        # imagee = ImageTk.PhotoImage(Image.open(fileopen))

        Labelpath = Label(enc,text=fileopen)
        Labelpath.place(x=520, rely=0.25, height=21, width=450)

        Labelimg = Label(enc,image=imagee)
        Labelimg.place(relx=0.42, rely=0.3, height=200, width=200)

    Button2 = Button(enc,text="Open file", background="white",command=openfile,font=('Algerian',12))
    Button2.place(x=690, rely=0.2, height=31, width=94)

    # secimg = StringVar()
    # radio1 = Radiobutton(enc,text='jpeg', value='jpeg', variable=secimg)
    # radio1.place(relx=0.465, rely=0.57)

    secimg = StringVar()
    radio1 = Radiobutton(enc,text='jpeg', value='jpeg',background="white", variable=secimg)
    radio1.place(relx=0.465, rely=0.57)
    secimg="jpeg"
    # radio2 = Radiobutton(enc,text='png', value='png', variable=secimg)
    # radio2.place(relx=0.8, rely=0.57)

    f1 = ("Comic Sans MS", 13)

    Label1 = Label(enc,text="Enter message",background="white",font=f1)
    Label1.place(relx=0.30, rely=0.64, height=30, width=125)
    entrysecmes = Entry(enc,font=(12))
    entrysecmes.place(relx=0.39, rely=0.62, relheight=0.07, relwidth=0.200)

    Label2 = Label(enc,text="Enter key",background="white",font=f1)
    Label2.place(relx=0.30, rely=0.72, height=30, width=125)

    entrykey = Entry(enc,font=(12))
    entrykey.place(relx=0.39, rely=0.71, relheight=0.06, relwidth=0.200)

    Label3 = Label(enc,text="File name",background="white",font=(10))
    Label3.place(relx=0.3, rely=0.8, height=27, width=125)

    entrysave = Entry(enc,font=(10))
    entrysave.place(relx=0.39, rely=0.79, relheight=0.05, relwidth=0.200)

    # e2.insert(0, ct)
    def encode():
        pt = entrysecmes.get()
        kt = entrykey.get()
        ct = onetimepad.encrypt(pt, kt)
        print("ct " + ct)
        # entrysave.insert(0, ct)
        # print("hellobaher")
        if secimg == "jpeg":
            # print("hello")
            inimage = fileopen
            response = messagebox.askyesno("popup", "Do you want to encode")
            if response == 1:
                aaa.hide(inimage, entrysave.get() + '.jpg', ct)
                messagebox.showinfo("popup", "successfully encode" + entrysave.get() + ".jpeg")


            else:
                messagebox.showwarning("popup", "unsuccessful")


    def hide():
        enc.withdraw()
        main.deiconify()

    # closebutton = Button(enc,text='EXIT', fg="white", bg="red",width=20, command=hide)
    # closebutton['font'] = fontl
    # closebutton.place(relx=0.3, rely=0.8)

    Buttonenc = Button(enc,text="ENCODE",background="honeydew", command=encode,font=('Algerian',16))
    Buttonenc.place(relx=0.7, rely=0.8, height=31, width=94)

    Buttonback = Button(enc,text="Back", command=hide,font=('Algerian',16))
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    changeOnHover(Button2, "LightCyan3", "white", "black", "black")
    changeOnHover(Buttonenc, "LightCyan3", "white", "black", "black")
    changeOnHover(Buttonback, "LightCyan3", "white", "black", "black")

    enc.mainloop()

def decode():
    main.withdraw()
    dec = Toplevel()
    dec.geometry('1920x795+-8+-3')
    fontl = tkFont.Font(dec, family='Algerian', size=32)
    dec.title('Dec Panel ')

    global image2
    image2 = ImageTk.PhotoImage(Image.open("img/61764.jpg").resize((1920, 1080)))
    # image2 = ImageTk.PhotoImage(Image.open("imp/vector_2602.jpg"))
    label2 = Label(dec, text="lalal", image=image2)
    label2.pack()


    LabelTitle = Label(dec,text="DECODE", bg="black", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.3, rely=0.1)

    def openfile():
        global fileopen
        global imagee
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files, png file", "*jpg *png"), ("all files", "*.*")))
        #
        im = Image.open(fileopen)
        imm = im.resize((400, 200))
        imagee = ImageTk.PhotoImage(imm)

        # imagee = ImageTk.PhotoImage(Image.open(fileopen))
        Labelpath = Label(dec,text=fileopen)
        Labelpath.place(x=520, rely=0.25, height=21, width=450)

        Labelimg = Label(dec,image=imagee)
        Labelimg.place(relx=0.42, rely=0.3, height=200, width=200)


    Button3 = Button(dec,text="Openfile", command=openfile,background="white",font=('Algerian',12))
    Button3.place(x=690, rely=0.2, height=31, width=94)

    secimg = StringVar()
    radio1 = Radiobutton(dec,text='jpeg', value='jpeg', variable=secimg)
    radio1.place(relx=0.465, rely=0.57)
    secimg="jpeg"
    f1 = ("Comic Sans MS", 13)

    Label2 = Label(dec, text="Enter key", font=f1)
    Label2.place(relx = 0.30, rely = 0.63, height = 30, width = 125)

    entrykey = Entry(dec, font=(12))
    entrykey.place(relx=0.39, rely=0.62, relheight=0.06, relwidth=0.200)

    Label1 = Label(dec,text="message",font=f1)
    Label1.place(relx=0.30, rely=0.72, height=30, width=125)
    fentrysecmes = Entry(dec,font=(12))
    # fentrysecmes.place(relx=0.69, rely=0.71, relheight=0.07, relwidth=0.200)
    # entrysecmes.place(relx = 0.39, rely = 0.71, relheight = 0.07, relwidth = 0.200)
    entrysecmes = Entry(dec,font=(12))
    entrysecmes.place(relx = 0.39, rely = 0.71, relheight = 0.07, relwidth = 0.200)
    def deimg():

        if secimg== "jpeg":
            messag = aaa.reveal(fileopen)
            # print("messag ",messag)
            # print(str(messag))
            fentrysecmes.delete(0,END)
            fentrysecmes.insert(0, messag)
            # print("messag2", messag)

            p=fentrysecmes.get()
            # print(p)
            # pt = entrysecmes.get()
            kt = entrykey.get()
            # print("p ",p)
            # print("kt ",kt)
            ct = onetimepad.decrypt(p, kt)
            # print("ct ",ct)
            # Label2 = Label(dec,text=messag)
            # Label2.place(relx=0.3, rely=0.7, height=21, width=204)
            entrysecmes.delete(0, END)
            entrysecmes.insert(0, ct)

    Button2 = Button(dec,text="DECODE", command=deimg,background="white",font=('Algerian',16))
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)

    def clear():
        entrykey.delete(0,END)
        entrysecmes.delete(0,END)

    Buttonback1 = Button(dec,text="CLEAR", command=clear,background="white",font=('Algerian',16))
    Buttonback1.place(relx=0.7, rely=0.85, height=31, width=94)

    def hide():
        dec.withdraw()
        main.deiconify()

    Buttonback2 = Button(dec,text="Back", command=hide,background="white",font=('Algerian',16))
    Buttonback2.place(relx=0.7, rely=0.9, height=31, width=94)
    changeOnHover(Button3, "LightCyan3", "white", "black", "black")
    changeOnHover(Button2, "LightCyan3", "white", "black", "black")
    changeOnHover(Buttonback1, "LightCyan3", "white", "black", "black")
    changeOnHover(Buttonback2, "LightCyan3", "white", "black", "black")
    dec.mainloop()
def exit():
    main.destroy()


encbutton = Button(text='Encode', fg="white", bg="black", width=20, command=encode)
encbutton['font'] = fontl
encbutton.place(relx=0.3, rely=0.3)

changeOnHover(encbutton, "SlateGray2", "black","black","white")

# encbutton.pack()
decbutton = Button(text='Decode', fg="white", bg="black", width=20, command=decode)
decbutton['font'] = fontl
decbutton.place(relx=0.3, rely=0.5)

changeOnHover(decbutton, "SlateGray2", "black","black","white")

closebutton = Button(text='EXIT', fg="black", bg="white", width=20, command=exit)
closebutton['font'] = fontl
closebutton.place(relx=0.3, rely=0.7)

changeOnHover(closebutton, "SlateGray2", "white","white","black")

main.mainloop()