import pygame 
import random
from enum import Enum 
# from module import class   

from  collections import namedtuple # assigns meaning to each position in the tuple ,more readible code


pygame.init()   

# This enum here is a set of symbolic names ,that are bound to unique values,
class Direction(Enum) : # we inherit from this enum , and then we define our enums
    RIGHT  =1 
    LEFT = 2 # these are constants
    UP = 3   # BY CONVENTION we use upper case 
    DOWN =4  # we can only have one of those 4 , we cant have down ,'1' ,'d'

Point = namedtuple('Point','x','y')  # this is basically a lightweight class ,but we don't have to 
                                        #-implement whole class classname thing

# Beacuse our snake will be bigger than just a single pixel so ,lets create a constant here
BLOCK_SIZE = 20

class SnakeGame :
    def __init__(self,w=680,h=480) : 
        self.w=w
        self.h=h

# INIT DISPLAY
    
        self.display= pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Snake') # not needed , but its good if our screen has a caption
        self.clock =pygame.time.Clock()  # for the speed of our game


# INITIAL GAME STATE
        # init game state : place the initial snake ,initial direction , and initial food
        # self.direction="right" # this is not a good way , it can cause typo error (USE ENUM CLASS)
        
        self.direction = Direction.RIGHT # initializing direction
        self.head = Point(self.w/2 ,self.h/2)# using list  # initialize snake ,by storing position of head
        #coordinates             x       y 
        self.snake = [self.head,Point(self.head.x-BLOCK_SIZE,self.head.y),# move one blocksize to left
                       Point(self.head.x-(2*BLOCK_SIZE),self.head.y) ] 
        
        self.score = 0
        self.food = None
        
        # initially we want to randomly place the food : so create a helper function

        def __place__food(self): # this will give random position on screan ,at multiples of block size
        # we want to randomly have a coordinate inside  def __init__ self.w=w self.h=h
            x = random.randint(0,(self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            y = random.randint(0,(self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            self.food = Point(x,y)
            if self.food in  self.snake:
                self.__place__food()  # call this function recursively

   
        def play_step(self):
            # 1. collect the user input 

            # 2. move our snake

            # 3. check if game over 

            # 4. place new food(if we hit the food) or just move the snake 

            # 5. update the pygame ui and clock 

            # 6 . return game over and score 

if __name__=='__main__': 
    game = SnakeGame()

    # Game Loop
    while True:
        game.play_step()

        # break  if game over 
          
    pygame.quit()