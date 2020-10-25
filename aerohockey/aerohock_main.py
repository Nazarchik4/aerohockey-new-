from tkinter import *
window = Tk()
canvas = Canvas(window, width=1000, height=550, bg="black")
canvas.pack()

vertical_up_left_line = canvas.create_rectangle(30,30,20,200, fill = "white")
vertical_down_left_line = canvas.create_rectangle(30,350,20,520,fill = "white")
horizotlal_up_line = canvas.create_rectangle(950,20,30,30, fill = "white")
horizotlal_down_line = canvas.create_rectangle(950,520,30,530, fill = "white")
vertical_up_left_line = canvas.create_rectangle(950,30,960,200, fill = "white")
vertical_down_right_line = canvas.create_rectangle(950,520,960,350, fill = "white")
middle_line = canvas.create_rectangle(500,30,490,520, fill = "white")

window.mainloop()