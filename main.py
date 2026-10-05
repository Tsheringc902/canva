# import tkinter as tk

# root = tk.Tk()
# root.title("My First Canvas")
# root.geometry("600x450")

# canvas = tk.Canvas(root, width=550, height=360, bg="white")
# canvas.pack()

# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(280, 50, 440, 190, fill="lightblue")
# canvas.create_line(50, 250, 500, 250, width=4)
# canvas.create_text(275, 310, text="Hello Canvas", font=("Arial", 20))

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("House")
root.geometry("650x550")

canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

# House wall
canvas.create_rectangle(
    150, 200, 450, 420,
    fill="#F5E6B8",
    outline="#333333",
    width=3
)

# Wall design - horizontal lines
canvas.create_line(150, 240, 450, 240, fill="#D4B66A", width=2)
canvas.create_line(150, 390, 450, 390, fill="#D4B66A", width=2)

# Wall design - small decorative rectangles
canvas.create_rectangle(165, 215, 190, 230, fill="#E2C878", outline="")
canvas.create_rectangle(410, 215, 435, 230, fill="#E2C878", outline="")

canvas.create_rectangle(165, 350, 190, 375, fill="#E2C878", outline="")
canvas.create_rectangle(410, 350, 435, 375, fill="#E2C878", outline="")

# Green roof
canvas.create_polygon(
    120, 200,
    300, 70,
    480, 200,
    fill="#2E7D32",
    outline="#1B3D1F",
    width=4
)

# Roof edge
canvas.create_line(
    120, 200, 480, 200,
    fill="#1B3D1F",
    width=7
)

# Left window
canvas.create_rectangle(
    175, 260, 245, 325,
    fill="#5BC0EB",
    outline="#333333",
    width=3
)

# Left window design
canvas.create_line(210, 260, 210, 325, fill="white", width=3)
canvas.create_line(175, 292, 245, 292, fill="white", width=3)

# Right window
canvas.create_rectangle(
    355, 260, 425, 325,
    fill="#5BC0EB",
    outline="#333333",
    width=3
)

# Right window design
canvas.create_line(390, 260, 390, 325, fill="white", width=3)
canvas.create_line(355, 292, 425, 292, fill="white", width=3)

# Door
canvas.create_rectangle(
    270, 300, 350, 420,
    fill="#8B4513",
    outline="#333333",
    width=3
)

# Door panels
canvas.create_rectangle(
    282, 315, 338, 360,
    fill="#A0522D",
    outline="#5C2E16",
    width=2
)

canvas.create_rectangle(
    282, 370, 338, 405,
    fill="#A0522D",
    outline="#5C2E16",
    width=2
)

# Door knob
canvas.create_oval(
    325, 360, 335, 370,
    fill="#FFD700",
    outline="#333333"
)

root.mainloop()