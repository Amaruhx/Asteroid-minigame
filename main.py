# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player


# Define the RGB color for black
BLACK = (0, 0, 0)
def main():
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    
    # Initialize the game 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    # Create a player object
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
   # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        
        # Call the draw method on the player instance
        player_instance.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
    #Quit the game when the user closes the window
    pygame.quit()
    

if __name__ == "__main__":
    main()