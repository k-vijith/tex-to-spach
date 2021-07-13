import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('TTS')
        self.root.configure(background="pink")
        self.root.resizable(0,0)
        self.label = tk.Label(self.root, text="Type Something", bg="pink", font="Arial 30 bold")
        self.label.pack()
        self.textbox = tk.Entry(self.root, width=35, font="Arial 25")
        self.textbox.pack()
        self.button = tk.Button(self.root, text= "SPEAK", bg="blue", font="Arial 25 bold", command=self.clicked)
        self.button.pack()
        self.root.mainloop()

    def clicked(self):
        text = self.textbox.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    temp = Widget()
