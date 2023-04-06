# Ideas
# Create option to change background color
# Create option to clear the whiteboard

from tkinter import *
# from tkinter.colorchooser import askcolor
# from tkinter import ttk
# import tkinter as tk

# function
def create_colour(position_y, c_opt):
    color = ''
    if c_opt == 1 :
        color = 'black'
    elif c_opt == 2 :
        color = 'red'
    elif c_opt == 3:
        color = 'brown'
    elif c_opt == 4:
        color = 'blue'
    elif c_opt == 5:
        color = 'yellow'
    elif c_opt == 6:
        color = 'green'
    elif c_opt == 7:
        color = 'white'
    id = colour_palette_canvas.create_rectangle((12,position_y,42,position_y+30), fill=color)

whiteboard  = Tk()

# creating the whiteboard window
whiteboard.title("Whiteboard")
whiteboard.geometry("1050x570+150+50")
whiteboard.configure(bg="#d3d3d3") # d3d3d3 -> hexadecimal to light gray color

# locking the sizes dimensions of the whiteboard
whiteboard.resizable(False, False) # Width and Height

# icon
whiteboard.iconbitmap(default="icon/whiteboard.ico")

# images
color_sidebar_image = PhotoImage(file="images/color_sidebar.png")
eraser_image = PhotoImage(file="images/eraser.png")

# label
color_sidebar_label = Label(whiteboard, image=color_sidebar_image, bg="#d3d3d3")
color_sidebar_label.place(x=10, y=15)

# Canvas
colour_palette_canvas = Canvas(whiteboard, bg="#ffffff", width=50, height=290, bd=0)
colour_palette_canvas.place(x=20, y=40)
whiteboard_canvas = Canvas(whiteboard, width=900, height=470, bg="#ffffff", cursor="hand2")
whiteboard_canvas.place(x=100, y=35)

#buttons
eraser_button = Button(whiteboard, image=eraser_image, bg="#f2f3f5")
eraser_button.place(x=20, y=340)

# collours of the colour_palette_canvas
c_opt = 1 # color option
position_y = 10
counter = 1
for counter in range(1, 8):
    create_colour(position_y, c_opt)
    c_opt += 1
    position_y += 40

whiteboard.mainloop()