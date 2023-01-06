from tkinter import *
import os
root=Tk()
root.title("Shutdown App")
root.geometry("400x580")

def restarttime():
    os.system("shutdown /r /t 30")

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def logoff():
    os.system("shutdown -l") 

#first button
restart_time_button=PhotoImage(file="restart time.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2",command=restarttime)
first_button.place(x=10,y=10)

#second button
close_button=PhotoImage(file="close.png")
second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2",command=root.destroy)
second_button.place(x=200,y=10)

#third button
restart_button=PhotoImage(file="restart.png")
third_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2",command=restart)
third_button.place(x=10,y=200)

#fourth button
shutdown_button=PhotoImage(file="shutdown.png")
fourth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2",command=shutdown)
fourth_button.place(x=200,y=200)

#fifth button
logoff_button=PhotoImage(file="logoff.png")
fifth_button=Button(root,image=logoff_button,borderwidth=0,cursor="hand2",command=logoff)
fifth_button.place(x=200,y=10)

root.mainloop()