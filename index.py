import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#2827CC")

engine = pyttsx3.init()
def speaknow():
    text = text_area.get(1.0, END)
    gender= gender_combobox.get()
    speed= speech_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if (gender == "Male"):
            engine.setProperty("voice", voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed == "Fast"):
            engine.setProperty("rate",250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty("rate",150)
            setvoice()
        else:
            engine.setProperty("rate",60)
            setvoice()

def downloadNow():
    text = text_area.get(1.0, END)
    gender= gender_combobox.get()
    speed= speech_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if (gender == "Male"):
            engine.setProperty("voice", voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
    if(text):
        if(speed == "Fast"):
            engine.setProperty("rate",250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty("rate",150)
            setvoice()
        else:
            engine.setProperty("rate",60)
            setvoice()


## icon
image_icon = PhotoImage(file="icon1.png")
root.iconphoto(False,image_icon)

## Header 
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

# Resize the image
logo_image = Image.open("header.png")
new_width = 150
new_height = 100
resized_logo = logo_image.resize((new_width, new_height), Image.ANTIALIAS)

# Convert the resized image to Tkinter-compatible format
tk_logo = ImageTk.PhotoImage(resized_logo)

Label(Top_frame, image=tk_logo, bg="white").place(x=10, y=5)
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white", fg="black").place(x=130,y=30)

text_area = Text(root,font="Robote 20", bg="white", relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#2827CC",fg="white").place(x=550,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#2827CC",fg="white").place(x=750,y=160)

## Gender
gender_combobox = Combobox(root,values=['Male',"Female"],font="arial 14",state="r",width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Female")

speech_combobox = Combobox(root,values=['Fast',"Normal","Slow"],font="arial 14",state="r",width=10)
speech_combobox.place(x=750,y=200)
speech_combobox.set("Normal")

## bUTTON
# Resize the image
image_icon1 = Image.open("icon1.png")
new_width = 100
new_height = 30
re_image = image_icon1.resize((new_width, new_height), Image.ANTIALIAS)

# Convert the resized image to Tkinter-compatible format
tk_icon = ImageTk.PhotoImage(re_image)
btn = Button(root,text="Speak",compound=LEFT,image=tk_icon,width=200,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=300)

image_save = Image.open("save_image.png")
new_width = 70
new_height = 25
image_save1 = image_save.resize((new_width, new_height), Image.ANTIALIAS)

# Convert the resized image to Tkinter-compatible format
tk_save = ImageTk.PhotoImage(image_save1)
btn = Button(root,text="Save",compound=LEFT,image=tk_save,width=200,bg="#39c790",font="arial 14 bold",command=downloadNow)
btn.place(x=550,y=360)

root.mainloop()
