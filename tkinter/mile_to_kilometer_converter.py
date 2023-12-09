from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Convert Miles to KM")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# make something to accept user input of miles
miles_input = Entry()
miles_input.grid(column=1, row=1)


# Calculate the corresponding km

def on_click():
    result = (float(miles_input.get()) * 1.609)
    km_output.config(text=f"{result}")


calculate_button = Button(text="calculate", command=on_click)
calculate_button.grid(column=3, row=4)

# Show the output
km_output = Label(text="0")
km_output.grid(column=1, row=2)
unit_label = Label(text="KM")
unit_label.grid(column=1, row=3)

window.mainloop()
