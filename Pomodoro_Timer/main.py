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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
     global reps
     reps = 0
     window.after_cancel(timer)
     canvas.itemconfig(count_down_text, text="00:00")
     timer_label.config(text='Timer', fg=GREEN)
     click_label.config(text="")
     

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
     global reps
     reps += 1
     work_sec = WORK_MIN * 60
     short_break = SHORT_BREAK_MIN * 60
     long_break = LONG_BREAK_MIN * 60

     if reps % 8 == 0:
          count_down(long_break)
          timer_label.config(text='Break', font=("Arial", 50, "bold"), fg=PINK, bg=YELLOW,  highlightthickness=0 )
     elif reps % 2 == 0:
          count_down(short_break)
          timer_label.config(text='Break', font=("Arial", 50, "bold"), fg=RED, bg=YELLOW,  highlightthickness=0 )
     else:
          timer_label.config(text='Timer', font=("Arial", 50, "bold"), fg=GREEN, bg=YELLOW,  highlightthickness=0 )
          count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60 )
    count_second = count % 60
    if count_second == 0:
         count_second = "00"
    elif count_second <= 9:
         count_second = f"0{count_second}"
         
    canvas.itemconfig(count_down_text, text = f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count-1)
    else:
         start_timer()
         marks = ""
         work_session = math.floor(reps/2)
         for _ in range(work_session):
              marks += "✔"
         click_label.config(text=marks)
        
              
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
count_down_text = canvas.create_text(100, 130, text='00:00', fill='white',
                   font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)



timer_label = Label(text='Timer', font=("Arial", 50, "bold"),
                    fg=GREEN, bg=YELLOW,  highlightthickness=0)
timer_label.grid(row=0, column=1)

click_label = Label(font=("Arial", 25, "bold"),
                    fg=GREEN, bg=YELLOW, highlightthickness=0)
click_label.grid(row=2, column=1)

button_start = Button(text='start', command=start_timer)
button_start.grid(row=2, column=0)
button_reset = Button(text='reset', command=reset)
button_reset.grid(row=2, column=2)


window.mainloop()