from tkinter import*
import subprocess

class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("Mini Game")

        self.width = 450
        self.canvas = Canvas(window, bg = "white",
        width = self.width, height = 200)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btResume = Button(frame, text ="Ball Race",fg ="white",font =("나눔고딕", 15, "bold"), width=10, height=2, bg="#225C73",
        command = self.click1)
        btResume.pack(side = LEFT, padx=10, pady=4)
        btFaster = Button(frame, text = "PingPing",fg ="white",font =("나눔고딕", 15, "bold"), width=10, height=2, bg="#4B8CA6",
        command = self.click2)
        btFaster.pack(side = LEFT, padx=10, pady=4)
        btSlower = Button(frame, text = "Snake",fg ="white", font =("나눔고딕", 15, "bold"), width=10, height=2, bg="#73B1BF",
        command = self.click3)
        btSlower.pack(side=LEFT, padx=10, pady=4)

        self.x = 0
        self.sleepTime = 10
        self.canvas.create_text(self.x,100,text = "Mini Game",font =("나눔고딕", 50, "bold"),tags = "text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop()
        
    def click1(self):
        subprocess.run(["python", "race.py"])
    def click2(self):
        subprocess.run(["python", "pingpong.py"])
    def click3(self):
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
                self.canvas.create_text(self.x,100,text = "Mini Game",font =("나눔고딕", 50, "bold"), tags = "text")

ControlAnimation()