from utils import probability_check

class Clouds:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sky_grid = [[0 for _ in range(width)] for _ in range(height)]

    def refresh_clouds(self, cloud_prob=1, max_cloud=20, lightning_prob=1, max_lightning=10):
        for row_idx in range(self.height):
            for col_idx in range(self.width):
                if probability_check(cloud_prob, max_cloud):
                    self.sky_grid[row_idx][col_idx] = 1
                    if probability_check(lightning_prob, max_lightning):
                        self.sky_grid[row_idx][col_idx] = 2
                else:
                    self.sky_grid[row_idx][col_idx] = 0

    def get_state(self):
        return {"sky_data": self.sky_grid}
    
    def set_state(self, state_data):
        self.sky_grid = state_data.get("sky_data", [[0 for _ in range(self.width)] for _ in range(self.height)])