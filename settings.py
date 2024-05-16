class Settings:
    """A class to store all the setting of alien invasion game."""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5