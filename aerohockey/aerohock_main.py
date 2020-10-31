from tkinter import *
window = Tk()
def roll():
    global ball_x
    global ball_y
    global dx
    global dy
    global pad_x
    global pad_y
    global ball
    ball_x = ball_x + dx
    ball_y = ball_y + dy
    if ball_x > 900 or ball_x < 10:
       dx = - dx
    if ball_x < 10 and (ball_y > 160 or ball_y < 370):
        canvas.delete(ball)
    if ball_x > 905 and (ball_y > 160 or ball_y < 370):
        canvas.delete(ball)
    if ball_y > 450 or ball_y < 30:
        dy = - dy
    canvas.coords(ball, ball_x, ball_y, ball_x + 50, ball_y + 50)
    window.after(40, roll)
def pad_move_green(event):
    global pad_green
    global pad_yellow
    if event.keysym == 'Right':
        canvas.move(pad_green, 10, 0)
    if event.keysym == 'Left':
        canvas.move(pad_green, -10, 0 )
    if event.keysym == 'Up':
        canvas.move(pad_green, 0, -10)
    if event.keysym == 'Down':
        canvas.move(pad_green, 0, 10)
    if event.keysym == '6':
        canvas.move(pad_yellow, 10, 0)
    if event.keysym == '4':
        canvas.move(pad_yellow,-10,0)
    if event.keysym == '8':
        canvas.move(pad_yellow, 0, -10)
    if event.keysym == '2':
        canvas.move(pad_yellow, 0, 10)
canvas = Canvas(window, width=980, height=550, bg="black")
canvas.pack()

vertical_up_left_line = canvas.create_rectangle(30,30,20,160, fill = "white")
vertical_down_left_line = canvas.create_rectangle(30,370,20,520,fill = "white")
horizotlal_up_line = canvas.create_rectangle(950,20,30,30, fill = "white")
horizotlal_down_line = canvas.create_rectangle(950,520,30,530, fill = "white")
vertical_up_left_line = canvas.create_rectangle(950,30,960,160, fill = "white")
vertical_down_right_line = canvas.create_rectangle(950,520,960,370, fill = "white")
middle_line = canvas.create_rectangle(500,30,490,520, fill = "white")

dx = 10
dy = 10
ball_x = 500
ball_y = 250
pad_y_green = 275
pad_x_green = 880
pad_x_yellow = 30
pad_y_yellow = 275
ball = canvas.create_oval(ball_x,ball_y,ball_x+20,ball_y+20, fill = "blue")

pad_green = canvas.create_oval(pad_x_green,pad_y_green,pad_x_green + 50,pad_y_green + 50, fill = "green", outline = "white")
pad_yellow = canvas.create_oval(pad_x_yellow,pad_y_yellow,pad_x_yellow + 50,pad_y_yellow + 50,fill = "yellow", outline = "white")

window.after(0, roll)
window.bind('<Key>',pad_move_green)
window.mainloop()