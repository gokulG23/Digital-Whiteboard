#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Ideas

# Create option to change background color
# Create option to clear the whiteboard
# Creat a change Thickness button
# Creat a save button
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Lybraries

from tkinter import *
# "tkinter" provides a robust, platform-independent windowing toolkit that is available to Python programmers
# read to learn more about tkinter library: https://docs.python.org/pt-br/3/library/tk.html
# "*" is used to import everything from the library

# Others importations that I may be used

# from tkinter.colorchooser import askcolor
# from tkinter import ttk
# import tkinter as tk
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Functions

# To define the color of what will be drawn
def set_color(new_color):
    global color, line_width, cursor_color

    color = new_color
    # cursor_color = new_color

    if color == '':
        line_width = 0

    if color == 'white':
        line_width = 50
    else:
        line_width = 5

# To locate the xy address of the point when you click with the mouse
def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

# To "erase" when you draw (in other words, to draw with the background color)
def eraser():
    set_color('white')

# To draw when you press the mouse button and moved the mouse
def draw(work):
    global current_x, current_y

    whiteboard_canvas.create_line((current_x, current_y, work.x, work.y), width=line_width, fill=color)
    current_x = work.x
    current_y = work.y

# To creat the colours of the colour palette
def create_colour(position_y, c_opt):

    color = ''
    # Choose the colour based on the option

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

    # Create a rectangle with that colour on the right position    
    id = colour_palette_canvas.create_rectangle((12,position_y,42,position_y+30), fill=color)
    colour_palette_canvas.tag_bind(id, '<Button-1>', lambda x: set_color(color))
    
# To clear all the canvas and rebuild it
def clear_all():
    c_opt = 1 # color option
    position_y = 10
    counter = 1

    whiteboard_canvas.delete('all')
    for counter in range(1, 8):
        create_colour(position_y, c_opt)
        c_opt += 1
        position_y += 40

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Main

#-------------------------------------------------------------------------------------------------------------------
# Creating the whiteboard window

whiteboard  = Tk()
# Instantiating the object Tk() of the class to the variable "whiteboard"
# So we can use all the functions of that object of the class through the variable "whiteboard"
# An object is a collection of variables and methods (functions).

# Defining whiteboard parameters

# Title
whiteboard.title("Whiteboard")
# Dimensions and Position
whiteboard.geometry("1050x570+150+50")
# Locking the dimensions of the whiteboard
whiteboard.resizable(False, False) # Width and Height
# Background colour
whiteboard.configure(bg="#d3d3d3") # d3d3d3 -> hexadecimal to light gray color

# Creating the items of the whiteboard

# Whiteboard icon
whiteboard.iconbitmap(default="icon/whiteboard.ico")
# images
color_sidebar_image = PhotoImage(file="images/color_sidebar.png")
eraser_image = PhotoImage(file="images/eraser.png")
garbage_image = PhotoImage(file="images/garbage.png")
# labels
color_sidebar_label = Label(whiteboard, image=color_sidebar_image, bg="#d3d3d3")
color_sidebar_label.place(x=10, y=15)
# Canvas
colour_palette_canvas = Canvas(whiteboard, bg="#ffffff", width=50, height=290, bd=0)
colour_palette_canvas.place(x=20, y=40)
whiteboard_canvas = Canvas(whiteboard, width=900, height=470, bg="#ffffff", cursor="dot blue")
whiteboard_canvas.place(x=100, y=35)
#buttons
eraser_button = Button(whiteboard, image=eraser_image, bg="#f2f3f5", command=eraser)
eraser_button.place(x=25, y=340)
garbage_button = Button(whiteboard, image=garbage_image, bg="#f2f3f5", command=clear_all)
garbage_button.place(x=25, y=395)
# collours of the colour_palette_canvas
c_opt = 1 # color option
position_y = 10
counter = 1
for counter in range(1, 8):
    create_colour(position_y, c_opt)
    c_opt += 1
    position_y += 40
#-------------------------------------------------------------------------------------------------------------------
set_color('')

whiteboard_canvas.bind('<Button-1>', locate_xy)
whiteboard_canvas.bind('<B1-Motion>', draw)

whiteboard.mainloop()

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
