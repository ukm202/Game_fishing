add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)



class Game:
    def __init__(self):
    
    
    
    
        self.Background = Background(0,0)
        self.river = River(0,350) 
        # self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        # self.background_sound.rewind()
        # self.background_sound.play()
        self.boat = Boat()   
        self.hook = Hook(self.boat.x,self.boat.y)
        
    def display(self):
        self.Background.show_background()
        self.river.move_river()
        self.boat.move_boat()
        self.hook.move()

        
class Background: 
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.img_num = 9  
    
    def show_background(self):
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1100,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1100,380)
        self.x -= 200
        if self.x <= -1100:
            self.x = 0
            self.img_num = random.randint(9,12)

class River:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # self.img_num = random.randint(0,7)
        self.img_num = 7
        # self.img_num1 = 7
        
 
        
    def move_river(self):
        
        self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        self.background_sound.rewind()
        self.background_sound.play()
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1100,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1100,380)
        
        self.x -= 100
        if self.x <= -1100:
            self.x = 0
            self.img_num = random.randint(0,7)
            

class Hook:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vy = 0    
        self.img = loadImage(path + "/images/hook.png")
        self.Hook_N = 0
        
    
    def move(self):  
        if self.vy == 0:
            if game.boat.vx >=0:
                image(self.img, game.boat.x+235, game.boat.y+12,100,100)
            if game.boat.vx <0:
                image(self.img,game.boat.x-40,game.boat.y+12,100,100)
                            
        if self.vy == 10 or self.vy == -10:
            self.y = self.y + self.vy
 
            self.Hook_N = int((self.y-208)//1)
            if game.boat.vx >0:
                image(self.img, game.boat.x+235, self.y+12,100,100)
                for a in range(self.Hook_N):
                    image(loadImage(path + "/images/hook_line.png"),game.boat.x+284,self.y-1*a+10,10,10)
            elif game.boat.vx < 0 :
                image(self.img,game.boat.x-58, self.y+12,100,100)
                for a in range(self.Hook_N):
                    image(loadImage(path + "/images/hook_line.png"),game.boat.x-10,self.y-1*a+1,10,10)
                
                
        if self.y == 580:
            self.vy = -10
        if self.y == 200:
            self.vy = 0
        

    
        
class Boat:
    def __init__(self):
        self.img = loadImage(path +"/images/fisherman.png")
        self.key_handler = {LEFT: False, RIGHT:True}
        self.vx = 10
        self.x = 400
        self.y = 200
        
    def move_boat(self):
        
        # Jeff added function 
        if game.hook.vy != 0: # STOP the boat when hook is deployed
            if self.vx > 0:
                image(self.img,self.x,self.y,300,250,800,0,0,800)
                self.vx = 0.01
            if self.vx < 0:
                image(self.img,self.x,self.y,200,150)
                self.vx =-0.01
            
        elif self.key_handler[LEFT]:
            self.vx = -10
            self.direction = LEFT
            image(self.img,self.x,self.y,200,150)
        elif self.key_handler[RIGHT]:
            self.vx = 10
            self.direction = RIGHT
            image(self.img,self.x,self.y,300,250,800,0,0,800)
        else:
            self.vx = 0
            
        
        self.x += self.vx
    

    
        
                
                        
                                        
        
# class Fish:
    
#     def __init__(self):
        
        
        
#     def move_fish(self):
    
    


game = Game()

def setup():
    size(1100, 700)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()

def keyPressed():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = True
    # elif keyCode == RIGHT:
        # game.boat.key_handler[RIGHT] = True
    if keyCode == DOWN:
        game.hook.vy = 10
    if keyCode == UP:
        game.hook.vy = -10 
        
def keyReleased():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = False
    # elif keyCode == RIGHT:
        # game.boat.key_handler[RIGHT] = False


                
 
        
        
        
        
        

    
