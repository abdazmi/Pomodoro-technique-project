from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=0
timer =None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canves.itemconfig(watch, text="00:00")
    timer_label.config(text="Timer",font=(FONT_NAME,35,"bold"),fg="#9bdeac", bg=YELLOW)
    check_label.config(text="")
    global REPS
    REPS =0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global REPS
    REPS += 1

    if REPS == 8:
        count_down(LONG_BREAK_MIN * 60)

        timer_label.config(text="Take a nap!", fg=PINK)

    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)

        timer_label.config(text="Take a rest", fg=RED)
    else:
        count_down(WORK_MIN * 60)

        timer_label.config(text="Work")





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min =  math.floor(count/60)
    sec = count % 60

    if min < 10:
        min =f"0{min}"

    if sec < 10:
        sec = f"0{sec}"

    canves.itemconfig(watch, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if min==f"0{0}" and sec==f"0{0}":
        start_count()
        mark=""
        num_session=math.floor(REPS/2)
        for _ in range(num_session):
            mark += "✓"
        check_label.config(text = mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady= 50, bg=YELLOW)
# -----------------------------------------
canves = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canves.create_image(100, 112, image=image)

watch = canves.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold") )

canves.grid(column= 1,row=1)
# ---------------------------------------

timer_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg="#9bdeac", bg=YELLOW)
timer_label.grid(row=0,column=1)

check_label = Label(font=(FONT_NAME,20,"bold"),fg="#9bdeac", bg=YELLOW)
check_label.grid(row=2, column=1)
check_label.config(pady=30)
# ----------------------------------------------

start_button = Button(text="Start", font=(FONT_NAME,10,"bold"),fg="black", bg=YELLOW, command=start_count)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", font=(FONT_NAME,10,"bold"),fg="black", bg=YELLOW, command=reset)
reset_button.grid(row=2,column=2)

window.mainloop()