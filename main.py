from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    check = "✓"
    if reps % 8 == 0:
        count_down( LONG_BREAK_MIN*60 )
        title_label.config(text="Breaaaak", font=(FONT_NAME, 42, "bold"), fg=RED)
    elif reps % 2 == 0:
        count_down( SHORT_BREAK_MIN*60 )
        title_label.config(text="Break",  font=(FONT_NAME, 40, "bold"), fg=PINK)
    else:
        count_down( WORK_MIN*60 )
        title_label.config(text="WORK",  font=(FONT_NAME, 38, "bold"), fg=GREEN)
        for i in range(math.floor(reps/2)):
            check += "✓"
        checkmark.config(text=check)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def double_digit(digit):
    if digit < 10:
        return f"0{digit}"
    else:
        return digit

def count_down(count):
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f"{double_digit(math.floor(count/60))}:{double_digit(count % 60)}")
    else:
        playsound("alert.mp3")
        start_timer()

def start_handle_click():
    start_button["state"] = DISABLED
    start_timer()

def stop_handle_click():
    start_button["state"] = NORMAL
    timer_reset()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=300, height= 250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 125, image=tomato_img)
timer_text = canvas.create_text(150, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

title_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)

checkmark = Label(text="", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)

start_button = Button(text="Start", font=(FONT_NAME, 15), command=start_handle_click)
stop_button = Button(text="Stop", font=(FONT_NAME, 15), command=stop_handle_click)


title_label.grid(column="1", row="0")
canvas.grid(column="1", row="1")
start_button.grid(column="0", row="2")
stop_button.grid(column="2", row="2")
checkmark.grid(column="1", row="2")


window.mainloop()