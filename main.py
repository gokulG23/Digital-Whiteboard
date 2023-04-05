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
whiteboard.configure(bg="#f9f9f9") # f8f8f8 -> hexadecimal to a shade of white color

# locking the sizes dimensions of the whiteboard
whiteboard.resizable(False, False) # Width and Height

# icon
whiteboard.iconbitmap(default="icon/whiteboard.ico")

# images
color_sidebar_image = PhotoImage(file="images/color_sidebar.png")
eraser_image = PhotoImage(file="images/eraser.png")

# label
color_sidebar_label = Label(whiteboard, image=color_sidebar_image, bg="#f8f8f8")
color_sidebar_label.place(x=10, y=15)

# Canvas
colour_palette = Canvas(whiteboard, bg="#ffffff", width=50, height=290, bd=0)
colour_palette.place(x=20, y=40)

#buttons
eraser_button = Button(whiteboard, image=eraser_image, bg="#f2f3f5")
eraser_button.place(x=20, y=340)


whiteboard.mainloop()