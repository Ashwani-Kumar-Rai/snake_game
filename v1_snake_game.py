import pygame # library for creating video games
#  print(pygame.ver) # printing the version of the pygame
import random # place the food randomly in the map



# pygame.init() is a function in Pygame that initializes all the Pygame modules required for the
    #-program to run. When you call pygame.init(),

#  it sets up the Pygame environment and prepares it for use.
    #- This function must be called before any other Pygame functions are used.

# pygame.init() performs a number of tasks, such as initializing the display,
    #- setting up the sound system, and initializing the event system, among others.
    #- Once pygame.init() has been called, you can use the other Pygame functions to create a game,
    #- play sounds, draw graphics, and handle user input.

pygame.init() # To initialize all the modules correctly 



# This code defines a PYTHON CLASS CALLED SnakeGame.
    #-Within the class, there may be methods and attributes that define the behavior and characteristics
    #-of the game.

class SnakeGame :
    def __init__(self,w=680,h=480) : # width of our screan will be 680 pixels,heigh of our sceen will be 480
        self.w=w
        self.h=h

    # init display    
    # init game state

    def play_step(self):
        pass


# The if __name__ == '__main__' statement checks if the code is being run as the main program,
    #- rather than being imported as a module into another program.

# If the code is being run as the main program, the next line of code creates an instance
    #- of the SnakeGame class called game

#This is a common programming practice in Python,
    #- as it helps to ensure that code that is not meant to be executed when the module is imported
    #- is not run accidentally.

if __name__=='__main__': # IF we run our script ,if this is the main process
    game =SnakeGame()

    # Game Loop
    while True:
        game.play_step()

        # break  if game over 
          
    pygame.quit()

# pygame.quit() is a function in the Pygame library that uninitializes all Pygame modules that have
    #- previously been initialized using pygame.init().
    
# It should be called when your Pygame program is exiting or shutting down, 
    #- in order to properly release any resources or memory used by Pygame.

#  If you do not call pygame.quit() before exiting your program,
    #- it may result in unexpected behavior or resource leaks.