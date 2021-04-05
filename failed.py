import tkinter as tk
import time
import alphabet

# how long the program will pause at each letter
pause_time = 2

# create the screen where the letters appear
screen = tk.Tk()
screen.geometry("500x500")
screen.configure(bg="black")

canvas = tk.Canvas(bg="black")
canvas.config(width=500, height=500)

# bottom left corner coords --> x: 175 y: 350
# top right corner coords --> x: 325 y: 150

# time.sleep(pause_time)


# functions
# prb dont need
def display(letter):
    for index in range(len(letter)-1):
        canvas.create_line(letter[index].x, letter[index].y,
                           letter[index+1].x, letter[index+1].y,
                           fill="cyan", width=2)


# queue for connect the dots
display(alphabet.chars['A'])
screen.after(2000, canvas.delete("all"))
# screen.after(3000, display(alphabet.chars['B']))


canvas.pack()


screen.mainloop()





