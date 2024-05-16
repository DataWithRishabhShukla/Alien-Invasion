import sys
#sys.path.insert(0,'/Users/rishabhshukla/git_projects/Alien-Invasion/')
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
        
    
    def _check_keydown_events(self,event):
        """Respond to key press"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """Respond to key relaese"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """ Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            # Watch for keyboard and mouse events.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
          
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    
    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
    
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # get rid of old bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
