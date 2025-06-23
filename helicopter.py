from utils import get_random_cell
import os   

class Helicopter:
    def __init__(self, width, height):
        start_cell = get_random_cell(width, height)
        self.x_coord, self.y_coord = start_cell[0], start_cell[1]
        self.width = width
        self.height = height
        self.water_tank = 0
        self.max_tank = 1
        self.score = 0
        self.lives = 20

    def move_helicopter(self, delta_x, delta_y):
        new_x, new_y = delta_x + self.x_coord, delta_y + self.y_coord
        if 0 <= new_x < self.height and 0 <= new_y < self.width:
            self.x_coord, self.y_coord = new_x, new_y

    def show_status(self):
        return f"🧺{self.water_tank}/{self.max_tank} | 🏆{self.score} | 💛{self.lives}"

    def terminate_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                    X")
        print(f"X   GAME OVER,   YOUR SCORE IS {self.score}  X")
        print("X                                    X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        os._exit(0)

    def get_state(self):
        return {
            "score": self.score,
            "lives": self.lives,
            "x": self.x_coord, "y": self.y_coord,
            "water": self.water_tank, "capacity": self.max_tank
        }
    
    def set_state(self, state_data):
        self.x_coord = state_data.get("x", 0)
        self.y_coord = state_data.get("y", 0)
        self.water_tank = state_data.get("water", 0)
        self.max_tank = state_data.get("capacity", 1)
        self.lives = state_data.get("lives", 3)
        self.score = state_data.get("score", 0)