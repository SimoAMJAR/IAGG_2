# levels.py

class Level:
    def __init__(self, number, knife_count, rotation_speed, preplaced_knives, direction="right"):
        self.number = number
        self.knife_count = knife_count
        self.rotation_speed = rotation_speed
        self.preplaced_knives = preplaced_knives
        self.direction = direction  # New parameter for rotation direction

class Levels:
    def __init__(self):
        self.current_level = 1
        self.levels = {
            1: Level(1, 5, 3, 0, "right"),  # Level 1: 5 knives, rotation speed 1, 3 preplaced knives, right direction
            2: Level(2, 5, 3, 2, "left"),   # Example with left direction
            3: Level(3, 7, 5, 0, "right"), 
            4: Level(4, 5, 5, 3, "left"), 
            5: Level(5, 7, 5, 3, "right"), 
            6: Level(6, 7, 6, 2, "left"), 
            7: Level(7, 3, 5, 8, "right"), 
            8: Level(8, 2, 5, 10, "left")
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
