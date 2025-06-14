import pygame, simpleGE, random



class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("apple.jpg")
        self.setSize(25, 25)
        self.minSpeed = 2
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x is random 0 - screen width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Horse(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("diesel.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

class Obstacle(simpleGE):
    def __init__(self, x, y):
        super().__init__(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
        self.BadApple.jpj

    def update(self):
        self.move(0, OBSTACLE_SPEED)

 def check_collisions(self):
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                print("Game Over!")
                self.quit()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("TC.jpg")
        
        self.sndApple = simpleGE.Sound("apple-crunch-215258.mp3")
        self.numApple = 10
        self.score = 0
        self.lblScore = LblScore()

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        
        self.horse = Horse(self)
        
        self.coins = []
        for i in range(self.numDebris):
            self.apple.append(Apple(self))
            
        self.sprites = [self.tc, 
                        self.Apple,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for apple in self.apple:        
            if apple.collidesWith(self.horse):
                apple.reset()
                self.sndApple.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()

        self.prevScore = prevScore

        self.setImage("TC.jpg")
        self.response = "Quit"
        
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "You are the horse", 
        "Move with left and right arrow keys.",
        "Catch as many apples as possible",
        "",
        "Have fun"]
        
        self.directions.center = (320, 200)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)        
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320, 400)
        
        self.lblScore.text = f"Last score: {self.prevScore}"

        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()


def main():
    
    keepGoing = True
    lastScore = 0

    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":    
            game = Game()
            game.start()
            lastScore = game.score
            
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()
