from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
checkmarks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    global checkmarks
    checkmarks = ""
    checkmark_label.config(text=checkmarks)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # if it's the 1st, 3rd, 5th, 7th rep -> work min
    # if it's the 2nd, 4th , 6th rep -> short break
    # if it's the 8th rep -> long break
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global checkmarks
    global timer
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            checkmarks += CHECKMARK
            checkmark_label.config(text=checkmarks)
            window.attributes('-topmost', 1)
            window.attributes('-topmost', 0)
            window.bell()
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label: Timer, checkmark
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=0)
checkmark_label = Label(text=checkmarks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=3)

# Start Button and Reset Button
Button(text="start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer).grid(column=0, row=2)
Button(text="reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer).grid(column=2, row=2)

window.mainloop()
