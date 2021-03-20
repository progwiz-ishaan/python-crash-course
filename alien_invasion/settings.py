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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right while the other represents left.
        self.fleet_direction = 1

        # How quicly the game speeds up.
        self.speedup_rate = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings theat can be changed during the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increse_speed_settings(self):
        """Increse speed settings."""
        self.ship_speed *= self.speedup_rate
        self.bullet_speed *= self.speedup_rate
        self.alien_speed *= self.speedup_rate