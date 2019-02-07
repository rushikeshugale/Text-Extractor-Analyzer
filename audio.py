import speech_recognition as sr
from tkinter import*
import tkinter as tk
from tkinter import filedialog

def browsefunc(root):
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select image file", filetypes=(
        ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))

    return filename
    """if len(filename) == 0:
        #import tkinter
        root.messagebox.showinfo('Error', 'Please select an actual file...?')
    else:
        root.messagebox.showinfo('Success!', 'The image has been uploaded Succesfully...')"""


def audioToText(filename):
    r = sr.Recognizer()
    audio_file = filename
    print(audio_file)
    with sr.AudioFile(audio_file) as source:
        audio_file = r.listen(source)

        try:
            text = r.Recognize_google(audio_file)
            print("You said : {}", format(text))
        except exception as e:
            print(e)


class audio:

    def __init__(self, root):
        self.root = root
        #global button_flag
        frame = Frame(root, width=1800, height=1400)
        frame.pack(side=TOP, fill=X)
        root.geometry("1000x600")
        root.title("Audio ")

        self.record = tk.PhotoImage(file='audio.png')
        self.record_button = Button(frame, width=300, height=300, text="Record", font='Helvetica 18 bold',
                                   image=self.record, bg="skyblue", fg='red', compound=TOP)
        self.record_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.record_button.image = self.record


        self.browse_audio = tk.PhotoImage(file='select.png')
        self.browse_button = Button(frame, width=300,height=300, text='Browse',  font='Helvetica 18 bold',image=self.browse_audio, bg='skyblue', fg='red', compound=TOP, command=lambda :browsefunc(root))
        self.browse_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.browse_button.image = self.browse_audio


        self.textit_button = Button(root,text = "Text it..",font='Helvetica 18 bold',bg="skyblue",fg='red',compound=TOP, command= lambda:audioToText(filename))
        self.textit_button.place(relx=0.3,rely=0.7,anchor=CENTER)
