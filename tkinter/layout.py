from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)

button = Button(text="Click Me")
button.grid(column=1, row=1)

textinput = Entry()
textinput.insert(index=END, string="Write something here")
textinput.grid(column=2, row=2)

window.mainloop()