# levels.py

class Level:
    def __init__(self, number, knife_count, rotation_speed, preplaced_knives):
        self.number = number
        self.knife_count = knife_count
        self.rotation_speed = rotation_speed
        self.preplaced_knives = preplaced_knives

class Levels:
    def __init__(self):
        self.current_level = 1
        self.levels = {
            1: Level(1, 5, 1, 3),  # Level 1: 5 knives, rotation speed 1, 3 preplaced knives
            # Add more levels here
            2: Level(2, 6, 2, 4),  # Example: Level 2: 6 knives, rotation speed 2, 4 preplaced knives
            3: Level(3, 7, 3, 5),  # Example: Level 3: 7 knives, rotation speed 3, 5 preplaced knives
        }

    def get_current_level(self):
        return self.levels.get(self.current_level, None)

    def advance_level(self):
        if self.current_level < max(self.levels.keys()):
            self.current_level += 1
            return True
        return False

    def reset(self):
        self.current_level = 1
