import tkinter as tk

window = tk.Tk()


window.title("My Black Screen")

window.geometry("800x600")

window.configure(bg="black")




white_box = tk.Button(window, bg="white", width="20", height="20")

white_box.place(relx=0.9, rely=0.9, anchor="center")

grid_coords = {}

myboxes = []

box_coordinates = []

grid_dad = tk.Frame(window, bg="black")

grid_dad.pack(pady=100, padx=20)

gridbutton_coords = {}

row_ammount = 10
column_ammount = 10

x_Offset = 10


y_Offset = 50


for column in range(column_ammount):
    for row in range(row_ammount):
        box = tk.Frame(grid_dad, bg="white", width="20", height="20")

        box.grid_propagate = False


        box.grid(row=row, column=column, padx=2, pady=2)

        button = tk.Button(box, bg="white", width="20", height="20")

        button.place(relheight=1, relwidth=1)
        y = row
        x = column

        gridbutton_coords[(x, y)] = button


        grid_coords[(x, y)] = box

gridbutton_coords[(3, 1)].configure(bg="blue")
grid_coords[(2, 2)].configure(bg="red")
grid_coords[(3, 2)].configure(bg="yellow")




window.mainloop()
