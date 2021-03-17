class Settings:
    """A class to store all the settings for alien_invasion.py."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5