import sys
#sys.path.insert(0,'/Users/rishabhshukla/git_projects/Alien-Invasion/')
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and add some resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
    
    def _check_events(self):
        """ Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            # Watch for keyboard and mouse events.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to right
                    self.ship.rect.x +=1
    
    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
    
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
