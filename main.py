from tkinter import*
#from PIL import Image
import tkinter as tk
from image import *
from audio import *

class mainGui:

    def __init__(self, root):
        self.root = root

        frame = Frame(root, width=1800, height=1400)
        frame.pack(side=TOP, fill=X)
        root.geometry("1000x600")
        root.title("Text Extractor & Analyzer ")

        self.image_photo = tk.PhotoImage(file='Image.png')
        self.image_button = Button(frame,width = 300, height =300,text = "Image",font='Helvetica 18 bold',image=self.image_photo,bg="skyblue",fg='red',compound=TOP, command= lambda:image(root))
        self.image_button.pack(side =tk.LEFT,padx=2,pady=2)
        self.image_button.image = self.image_photo


        self.audio_photo = tk.PhotoImage(file='audio.png')
        self.audio_button = Button(frame,width = 300, height =300,text = "Audio",font='Helvetica 18 bold',image=self.audio_photo,bg="skyblue",fg='red',compound=TOP, command= lambda:audio(root))
        self.audio_button.pack(side =tk.LEFT,padx=2,pady=2)
        self.audio_button.image = self.audio_photo


        self.video_photo = tk.PhotoImage(file='video.png')
        self.video_button = Button(frame,width = 300, height =300,text = "Video",font='Helvetica 18 bold',image=self.video_photo,bg="skyblue",fg='red',compound=TOP)
        self.video_button.pack(side =tk.LEFT,padx=2,pady=2)
        self.video_button.image = self.video_photo




root = Tk()

mainGui(root)


root.mainloop()