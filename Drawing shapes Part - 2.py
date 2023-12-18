from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Drawing Shapes Part - 2")
root.geometry("1300x1300")

note = Label(root, text = "Note - To draw Circle / Rectangle / Line, press - c / r / i, respectively.")
note.place(relx = 0.1, rely = 0.9)

canvas = Canvas(root, height=510, width = 1300, bg = "white", highlightbackground="lightgrey")
canvas.pack()

label = Label(root, text = "Choose Colour")
label.place(relx = 0.7, rely = 0.8, anchor = CENTER)

Color_list = ["blue", "yellow", "red", "green"]
DropDown = ttk.Combobox(root, state="readonly", values = Color_list, width = 15)
DropDown.place(relx = 0.8, rely = 0.8, anchor = CENTER)

coordinates_values = [ 10, 50, 100, 200, 300, 400, 500, 600, 800, 900]

startx = Label(root, text = "StartX")
startx.place(relx = 0.1, rely = 0.7099, anchor = CENTER)

Drop_Cordinates_x = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 15)
Drop_Cordinates_x.place(relx = 0.2, rely = 0.7099, anchor = CENTER)

endx = Label(root, text = "EndX")
endx.place(relx = 0.5, rely = 0.7099, anchor = CENTER)

Drop_Cordinates_x_end = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 15)
Drop_Cordinates_x_end.place(relx = 0.6, rely = 0.7099, anchor = CENTER)

starty = Label(root, text = "StartY")
starty.place(relx = 0.3, rely = 0.7099, anchor = CENTER)

Drop_Cordinates_y = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 15)
Drop_Cordinates_y.place(relx = 0.4, rely = 0.7099, anchor = CENTER)

endy = Label(root, text = "EndY")
endy.place(relx = 0.7, rely = 0.7099, anchor = CENTER)

Drop_Cordinates_y_end = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 15)
Drop_Cordinates_y_end.place(relx = 0.8, rely = 0.7099, anchor = CENTER)

def circle(event):
    oldx = Drop_Cordinates_x.get()
    oldy = Drop_Cordinates_y.get()
    newx = Drop_Cordinates_x_end.get()
    newy = Drop_Cordinates_y_end.get()
    
    keypress = "c"
    draw(keypress, oldx ,oldy, newx, newy)
    
def rectangle(event):
    oldx = Drop_Cordinates_x.get()
    oldy = Drop_Cordinates_y.get()
    newx = Drop_Cordinates_x_end.get()
    newy = Drop_Cordinates_y_end.get()

    keypress = "r"
    draw(keypress, oldx ,oldy, newx, newy)

def line(event):
    oldx = Drop_Cordinates_x.get()
    oldy = Drop_Cordinates_y.get()
    newx = Drop_Cordinates_x_end.get()
    newy = Drop_Cordinates_y_end.get()
    
    keypress = "i"
    draw(keypress, oldx ,oldy, newx, newy)
    
def draw(keypress, oldx ,oldy, newx, newy):
    color = DropDown.get()
    if(keypress == 'c'):
        draw_circle = canvas.create_oval(oldx, oldy, newx, newy, fill = color)
        
    if(keypress == 'r'):
        draw_rectangle = canvas.create_rectangle(oldx, oldy, newx, newy, fill = color)
        
    if(keypress == 'i'):
        draw_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = color)
        
root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<i>", line)    

root.mainloop()