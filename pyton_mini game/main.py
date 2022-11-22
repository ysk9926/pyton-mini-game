from tkinter import *
import subprocess

                
def click1():
    
    subprocess.run(["python", "race.py"])
def click2():
    subprocess.run(["python", "pingpong.py"])
def click3():
    subprocess.run(["python", "snake.py"])

main = Tk()

main.title('Mini Game')
main.geometry("350x250+100+100")
main.resizable(False, False)


frame1 = Frame(main)
frame1.pack()
frame1.place(relx = 0.5, rely = 0.5, anchor = "center")

Button(frame1, text ="ball race", command=click1, width=10, height=2).grid(row = 0, column = 0)
Button(frame1, text ="pingpong", command=click2, width=10, height=2).grid(row= 0, column = 1)
Button(frame1, text ="snake", command=click3, width=10, height=2).grid(row= 0, column = 2)


main.mainloop()

