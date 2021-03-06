class Settings():
    """A class store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # ship settings
        self.ship_limit = 2
        
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 200
        
        # alien settings
        self.fleet_drop_speed = 10
        
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        
        # how quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        # scoring
        self.alien_points = 50
        
        # fire consecutively
        self.fire = False
        
        self.loop_number=0
        
    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
