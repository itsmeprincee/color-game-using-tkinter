from tkinter import *
import tkinter.font as font
import random

colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]
timer = 60
score = 0
displayed_word_color=""
# this function will be called when user clicks start button
def startgame():
    global displayed_word_color,timer
    timer = 60
    if timer == 60:
        startcountdown()
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors),fg = displayed_word_color)
        color_entry.bind('<Return>',displaynextword)
def resetgame():
    global timer,score,displayed_word_color
    timer = 60
    score = 0
    game_score.config(text="Your Score:"+str(score))
    time_left.config(text = "Your Game ends in : -")
    displayed_word_color = random.choice(colors).lower()
    display_words.config(text=random.choice(colors), fg=displayed_word_color)
    color_entry.delete(0,END)
def startcountdown():
    global timer
    if(timer >= 0):
        time_left.config(text = "Your Game Ends in :"+str(timer)+"s")
        timer -= 1
        time_left.after(1000,startcountdown)
        if(timer == -1):
            time_left.config(text="Game Over!!")
#this function is used to display random words
def displaynextword(event):
    global displayed_word_color,score
    if(timer>0):
        if(displayed_word_color == color_entry.get().lower()):
            score += 1
            game_score.config(text = "your score:"+str(score))
        color_entry.delete(0,END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors),fg = displayed_word_color)
def stopgame():
    global displayed_word_color,score,timer
    timer = 0
    displayed_word_color = ""
    score = 0
    display_words.config(text = "")
    color_entry.delete(0,END)
    time_left.config(text = "Your Game Ends in : -")
    game_score.config(text = "Your score:"+str(score))

mywindow = Tk()
mywindow.title("Color Game")
mywindow.geometry("500x350")
currentfont = font.Font(family="Helvetica",size= 12)
normalfont = font.Font(family="Helvetica")
game_desc = "Enter the color of the words displayed below"
game_description = Label(mywindow,text=game_desc,font=currentfont,fg="grey")
game_description.pack()
game_score = Label(mywindow,text="Your Score:"+str(score),font = (font.Font(size=16)),fg = "green")
game_score.pack()
display_words = Label(mywindow,font = (font.Font(size=28)),pady=10)
display_words.pack()
time_left = Label(mywindow,text="Your Game ends in : -",font=(font.Font(size=14)),fg ="green")
time_left.pack()
color_entry=Entry(mywindow,width=30)
color_entry.pack(pady=20)
btn_frame = Frame(mywindow,width=80,height=40,bg="red")
btn_frame.pack(side=BOTTOM)
start_button = Button(btn_frame,text = "Start",width=18,fg = "black",bg="white",bd = 0,padx = 20,pady = 20,command=startgame)
start_button.grid(row=0,column=0)
reset_button = Button(btn_frame,text ="Reset",width=18,fg = "black",bg="lightblue",bd =0,padx = 20,pady= 20,command=resetgame)
reset_button.grid(row = 0,column = 1)
stop_button = Button(btn_frame,text = "Stop",width= 18,fg = "black",bg="silver",bd=0,padx = 20,pady = 20,command=stopgame)
stop_button.grid(row=0,column = 2)
mywindow.mainloop()