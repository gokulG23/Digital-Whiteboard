# Ideas
# Create option to change background color

from tkinter import *
# from tkinter.colorchooser import askcolor
# from tkinter import ttk
# import tkinter as tk

whiteboard  = Tk()
whiteboard.title("Whiteboard")
whiteboard.geometry("1050x570+150+50")
whiteboard.configure(bg="#ffffff") # ffffff -> hexadecimal to white color
whiteboard.resizable(False, False) # Width and Height

whiteboard.mainloop()