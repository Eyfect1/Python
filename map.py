from utils import probability_check, get_random_cell, get_adjacent_cell

TERRAIN_SYMBOLS = "🟩🌲🌊🏥🏬🔥"

REWARD_FOR_TREE = 100
COST_FOR_UPGRADE = 5000
COST_FOR_LIFE = 10000

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.terrain = [[0 for _ in range(width)] for _ in range(height)]
        self.generate_vegetation(5, 10)
        self.generate_water_path(10)
        self.generate_water_path(10)
        self.place_upgrade_center()
        self.place_medical_facility()

    def is_inside_bounds(self, x_coord, y_coord):
        return 0 <= x_coord < self.height and 0 <= y_coord < self.width

    def display(self, aircraft, clouds):
        border = "⬛" * (self.width + 2) + "\n"
        for row_num in range(self.height):
            border += "⬛"
            for col_num in range(self.width):
                cell_value = self.terrain[row_num][col_num]
                if clouds.sky_grid[row_num][col_num] == 1:
                    border += "⚪️"
                elif clouds.sky_grid[row_num][col_num] == 2:
                    border += "⚡️"
                elif aircraft.x_coord == row_num and aircraft.y_coord == col_num:
                    border += "🚁"
                elif 0 <= cell_value < len(TERRAIN_SYMBOLS):
                    border += TERRAIN_SYMBOLS[cell_value]
            border += "⬛\n"
        border += "⬛" * (self.width + 2)
        return border
  
    def generate_water_path(self, path_length):
        start_cell = get_random_cell(self.width, self.height)
        current_x, current_y = start_cell[0], start_cell[1]
        self.terrain[current_x][current_y] = 2
        while path_length > 0:
            next_cell = get_adjacent_cell(current_x, current_y)
            next_x, next_y = next_cell[0], next_cell[1]
            if self.is_inside_bounds(next_x, next_y):
                self.terrain[next_x][next_y] = 2
                current_x, current_y = next_x, next_y
                path_length -= 1

    def generate_vegetation(self, density, max_density):
        for row in range(self.height):
            for col in range(self.width):
                if probability_check(density, max_density):
                    self.terrain[row][col] = 1

    def add_tree(self):
        new_cell = get_random_cell(self.width, self.height)
        x, y = new_cell[0], new_cell[1]
        if self.terrain[x][y] == 0:
            self.terrain[x][y] = 1

    def place_upgrade_center(self):
        center_cell = get_random_cell(self.width, self.height)
        x, y = center_cell[0], center_cell[1]
        self.terrain[x][y] = 4

    def place_medical_facility(self):
        facility_cell = get_random_cell(self.width, self.height)
        x, y = facility_cell[0], facility_cell[1]
        if self.terrain[x][y] != 4:
            self.terrain[x][y] = 3
        else:
            self.place_medical_facility()

    def ignite_fire(self):
        fire_cell = get_random_cell(self.width, self.height)
        x, y = fire_cell[0], fire_cell[1]
        if self.terrain[x][y] == 1:
            self.terrain[x][y] = 5

    def update_fires(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.terrain[row][col] == 5:
                    self.terrain[row][col] = 0
        for _ in range(10):
            self.ignite_fire()

    def process_aircraft(self, aircraft, clouds):
        current_cell = self.terrain[aircraft.x_coord][aircraft.y_coord]
        weather_cell = clouds.sky_grid[aircraft.x_coord][aircraft.y_coord]

        if current_cell == 2:
            aircraft.water_tank = aircraft.max_tank
        if current_cell == 5 and aircraft.water_tank > 0:
            aircraft.water_tank -= 1
            aircraft.score += REWARD_FOR_TREE
            self.terrain[aircraft.x_coord][aircraft.y_coord] = 1
        if current_cell == 4 and aircraft.score >= COST_FOR_UPGRADE:
            aircraft.max_tank += 1
            aircraft.score -= COST_FOR_UPGRADE
        if current_cell == 3 and aircraft.score >= COST_FOR_LIFE:
            aircraft.lives += 10
            aircraft.score -= COST_FOR_LIFE
        if weather_cell == 2:
            aircraft.lives -= 1
            if aircraft.lives == 0:
                aircraft.terminate_game()

    def get_state(self):
        return {"terrain_data": self.terrain}
    
    def set_state(self, state_data):
        self.terrain = state_data.get("terrain_data", [[0 for _ in range(self.width)] for _ in range(self.height)])