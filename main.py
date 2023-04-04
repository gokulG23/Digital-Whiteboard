# Ideas
# Create option to change background color

from tkinter import *
# from tkinter.colorchooser import askcolor
# from tkinter import ttk
# import tkinter as tk

whiteboard  = Tk()

# creating the whiteboard window
whiteboard.title("Whiteboard")
whiteboard.geometry("1050x570+150+50")
whiteboard.configure(bg="#ffffff") # ffffff -> hexadecimal to white color

# locking the sizes dimensions of the whiteboard
whiteboard.resizable(False, False) # Width and Height

# icon
whiteboard.iconbitmap(default="icon/whiteboard.ico")
#board_icon = PhotoImage(file="icon/whiteboard.ico")

# image
color_sidebar_image = PhotoImage(file="images/color_sidebar.png")

# label
color_sidebar_label = Label(whiteboard, image=color_sidebar_image, bg="#ffffff")

# Placing label
color_sidebar_label.place(x=10, y=15)

whiteboard.mainloop()