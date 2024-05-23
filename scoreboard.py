from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}    High score: {self.high_score}", False, ALIGNMENT, FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)
    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.show_score()

