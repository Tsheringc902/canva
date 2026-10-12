
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Animation")

# canvas = tk.Canvas(
#     root,
#     width=600,
#     height=350,
#     bg="white"
# )

# canvas.pack()

# # Draw a red ball
# ball = canvas.create_oval(
#     40, 40, 90, 90,
#     fill="orange",
#     outline=""
# )

# # Set the movement speed
# speed = 5

# def move_ball():
#     global speed

#     # Move the ball
#     canvas.move(ball, speed, 0)

#     # Get the ball's position
#     x1, y1, x2, y2 = canvas.coords(ball)

#     # Change direction at the boundaries
#     if x2 >= 600:
#         speed = -5
#     elif x1 <= 0:
#         speed = 5

#     # Repeat the movement
#     root.after(20, move_ball)

# move_ball()

# root.mainloop()



import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation")

canvas = tk.Canvas(
    root,
    width=600,
    height=350,
    bg="white"
)

canvas.pack()

# Draw an orange ball
ball = canvas.create_oval(
    40, 280, 90, 330,
    fill="orange",
    outline=""
)

# Set movement speeds
speed_x = 4
speed_y = 0
gravity = 0.4
bounce_strength = -5

def move_ball():
    global speed_y

    # Move the ball
    canvas.move(ball, speed_x, speed_y)

    # Apply gravity
    speed_y += gravity

    # Get the ball's position
    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce at the bottom
    if y2 >= 350:
        canvas.move(ball, 0, 350 - y2)
        speed_y = bounce_strength

    # Stop before reaching the right edge
    if x2 >= 450:
        return

    # Repeat the animation
    root.after(20, move_ball)

move_ball()

root.mainloop()

