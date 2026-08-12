import tkinter as tk

window = tk.Tk()


window.title("My Black Screen")

window.geometry("800x600")

window.configure(bg="black")




white_box = tk.Frame(window, bg="white", width="20", height="20")

white_box.place(relx=0.1, rely=0.1, anchor="center")

for i in range(4):
    print()
    


window.mainloop()
