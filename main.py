from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
import tomato as tomato

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

LIGHT_YELLOW = "#D3ECA7"
LIGHT_GREEN = "#A1B57D"
LIGHT_RED = "#B33030"
DARK_BLUE = "#19282F"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minutes:02}:{count_seconds:02}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LIGHT_YELLOW)




status_label = Label(text="Timer")
status_label.config(font=(FONT_NAME, 50), bg=LIGHT_YELLOW, fg=LIGHT_GREEN)
status_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=LIGHT_YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start")
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)

check_marks = Label(text="✔")
check_marks.config(bg=LIGHT_YELLOW, fg=DARK_BLUE)
check_marks.grid(column=1, row=3)

reset_button = Button(text="Reset")
reset_button.config(command=start_timer)
reset_button.grid(column=2, row=2)




window.mainloop()
