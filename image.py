from tkinter import*
import tkinter as tk
from tkinter import filedialog



def browsefunc(root):
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select image file", filetypes=(
        ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    """if len(filename) == 0:
        #import tkinter
        root.messagebox.showinfo('Error', 'Please select an actual file...?')
    else:
        root.messagebox.showinfo('Success!', 'The image has been uploaded Succesfully...')"""


class image:

    def __init__(self, root):
        self.root = root
        #global button_flag
        frame = Frame(root, width=1800, height=1400)
        frame.pack(side=TOP, fill=X)
        root.geometry("1000x600")
        root.title("Image ")

        self.capture = tk.PhotoImage(file='capturecam.png')
        self.captureimg_button = Button(frame, width=300, height=300, text="capture", font='Helvetica 18 bold',
                                   image=self.capture, bg="skyblue", fg='red', compound=TOP)
        self.captureimg_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.captureimg_button.image = self.capture


        self.browse_image = tk.PhotoImage(file='select.png')
        self.browse_button = Button(frame, width=300,height=300, text='Browse',  font='Helvetica 18 bold',image=self.browse_image, bg='skyblue', fg='red', compound=TOP, command=lambda :browsefunc(root))
        self.browse_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.browse_button.image = self.browse_image


        self.textit_button = Button(root,text = "Text it..",font='Helvetica 18 bold',bg="skyblue",fg='red',compound=TOP)
        self.textit_button.place(relx=0.3,rely=0.7,anchor=CENTER)



'''root = Tk()
img = image(root)

root.mainloop()'''