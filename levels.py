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
            1: Level(1, 5, 4, 0),  # Level 1: 5 knives, rotation speed 1, 3 preplaced knives
            2: Level(2, 5, 4, 2),  
            3: Level(3, 7, 4, 2),  
            4: Level(4, 5, 4, 4),  
            5: Level(5, 5, 4, 2),  
            6: Level(6, 5, 4, 5),  
            7: Level(7, 5, 4, 8),  
            8: Level(8, 5, 4, 10)
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
