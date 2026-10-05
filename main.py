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

# import tkinter as tk

# root = tk.Tk()
# root.title("House")
# root.geometry("650x550")

# canvas = tk.Canvas(root, width=600, height=500, bg="white")
# canvas.pack()

# # House wall
# canvas.create_rectangle(
#     150, 200, 450, 420,
#     fill="#F5E6B8",
#     outline="#333333",
#     width=3
# )

# # Wall design - horizontal lines
# canvas.create_line(150, 240, 450, 240, fill="#D4B66A", width=2)
# canvas.create_line(150, 390, 450, 390, fill="#D4B66A", width=2)

# # Wall design - small decorative rectangles
# canvas.create_rectangle(165, 215, 190, 230, fill="#E2C878", outline="")
# canvas.create_rectangle(410, 215, 435, 230, fill="#E2C878", outline="")

# canvas.create_rectangle(165, 350, 190, 375, fill="#E2C878", outline="")
# canvas.create_rectangle(410, 350, 435, 375, fill="#E2C878", outline="")

# # Green roof
# canvas.create_polygon(
#     120, 200,
#     300, 70,
#     480, 200,
#     fill="#2E7D32",
#     outline="#1B3D1F",
#     width=4
# )

# # Roof edge
# canvas.create_line(
#     120, 200, 480, 200,
#     fill="#1B3D1F",
#     width=7
# )

# # Left window
# canvas.create_rectangle(
#     175, 260, 245, 325,
#     fill="#5BC0EB",
#     outline="#333333",
#     width=3
# )

# # Left window design
# canvas.create_line(210, 260, 210, 325, fill="white", width=3)
# canvas.create_line(175, 292, 245, 292, fill="white", width=3)

# # Right window
# canvas.create_rectangle(
#     355, 260, 425, 325,
#     fill="#5BC0EB",
#     outline="#333333",
#     width=3
# )

# # Right window design
# canvas.create_line(390, 260, 390, 325, fill="white", width=3)
# canvas.create_line(355, 292, 425, 292, fill="white", width=3)

# # Door
# canvas.create_rectangle(
#     270, 300, 350, 420,
#     fill="#8B4513",
#     outline="#333333",
#     width=3
# )

# # Door panels
# canvas.create_rectangle(
#     282, 315, 338, 360,
#     fill="#A0522D",
#     outline="#5C2E16",
#     width=2
# )

# canvas.create_rectangle(
#     282, 370, 338, 405,
#     fill="#A0522D",
#     outline="#5C2E16",
#     width=2
# )

# # Door knob
# canvas.create_oval(
#     325, 360, 335, 370,
#     fill="#FFD700",
#     outline="#333333"
# )

# root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("My House")
root.geometry("700x550")

canvas = tk.Canvas(root, width=650, height=500, bg="skyblue")
canvas.pack()

# Sun
canvas.create_oval(
    520, 50, 590, 120,
    fill="yellow",
    outline="orange",
    width=3
)

# Grass
canvas.create_rectangle(
    0, 400, 650, 500,
    fill="green",
    outline="green"
)

# House body
canvas.create_rectangle(
    180, 220, 500, 400,
    fill="lightyellow",
    outline="black",
    width=3
)

# Roof
canvas.create_polygon(
    150, 220,
    340, 80,
    530, 220,
    fill="red",
    outline="black",
    width=3
)

# Door
canvas.create_rectangle(
    300, 300, 380, 400,
    fill="brown",
    outline="black",
    width=3
)

# Door knob
canvas.create_oval(
    360, 345, 370, 355,
    fill="yellow"
)

# Left window
canvas.create_rectangle(
    210, 260, 275, 325,
    fill="lightblue",
    outline="black",
    width=3
)

# Cross on left window
canvas.create_line(
    242, 260, 242, 325,
    fill="black",
    width=2
)

canvas.create_line(
    210, 292, 275, 292,
    fill="black",
    width=2
)

# Right window
canvas.create_rectangle(
    405, 260, 470, 325,
    fill="lightblue",
    outline="black",
    width=3
)

# Cross on right window
canvas.create_line(
    437, 260, 437, 325,
    fill="black",
    width=2
)

canvas.create_line(
    405, 292, 470, 292,
    fill="black",
    width=2
)

# Chimney
canvas.create_rectangle(
    420, 130, 465, 200,
    fill="gray",
    outline="black",
    width=3
)

# Path to door
canvas.create_polygon(
    300, 400,
    380, 400,
    430, 500,
    250, 500,
    fill="lightgray",
    outline="black"
)

# -------------------------
# DOG HOUSE
# -------------------------

# Dog house body
canvas.create_rectangle(
    70, 350, 190, 440,
    fill="orange",
    outline="black",
    width=3
)

# Dog house roof
canvas.create_polygon(
    55, 350,
    130, 290,
    205, 350,
    fill="brown",
    outline="black",
    width=3
)

# Dog house entrance
canvas.create_oval(
    105, 370, 155, 430,
    fill="black",
    outline="black"
)

# -------------------------
# DOG
# -------------------------

# Dog body
canvas.create_oval(
    70, 420, 150, 465,
    fill="saddlebrown",
    outline="black",
    width=2
)

# Dog head
canvas.create_oval(
    45, 390, 105, 445,
    fill="saddlebrown",
    outline="black",
    width=2
)

# Dog ear
canvas.create_oval(
    40, 395, 60, 425,
    fill="brown",
    outline="black"
)

# Dog eye
canvas.create_oval(
    80, 405, 87, 412,
    fill="black"
)

# Dog nose
canvas.create_oval(
    45, 420, 55, 428,
    fill="black"
)

# Dog legs
canvas.create_rectangle(
    85, 445, 100, 480,
    fill="saddlebrown",
    outline="black"
)

canvas.create_rectangle(
    125, 445, 140, 480,
    fill="saddlebrown",
    outline="black"
)

# Dog tail
canvas.create_line(
    145, 425,
    170, 405,
    180, 420,
    fill="saddlebrown",
    width=8,
    smooth=True
)

# House label
canvas.create_text(
    340, 470,
    text="My House",
    font=("Arial", 20, "bold"),
    fill="black"
)

root.mainloop()