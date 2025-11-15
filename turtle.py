class Turtle:

    def __init__(self):
        self.lives = 3
        self.score = 0
    
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
        elif self.lives == 0:
            return True
        return False
    
    def gain_score(self, points):
        self.score += points