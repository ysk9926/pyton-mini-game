from tkinter import*
import subprocess

class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("Mini Game")

        self.width = 250
        self.canvas = Canvas(window, bg = "white",
        width = self.width, height = 50)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btResume = Button(frame, text ="Ball Race",
        command = click1)
        btResume.pack(side = LEFT)
        btFaster = Button(frame, text = "PingPing",
        command = click2)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "Snake",
        command = click3)
        btSlower.pack(side=LEFT)

        self.x = 0
        self.sleepTime = 100
        self.canvas.create_text(self.x,30,text = "Mini Game", tags = "text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop()
        
    def click1():
        subprocess.run(["python", "race.py"])
    def click2():
        subprocess.run(["python", "pingpong.py"])
    def click3():
        subprocess.run(["python", "snake.py"])


    def animate(self):
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0)
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            if self.x < self.width:
                self.x += self.dx
            else:
                self.x = 0
                self.canvas.delete("text")
                self.canvas.create_text(self.x,30,text = "Message moving?", tags = "Text")

ControlAnimation()