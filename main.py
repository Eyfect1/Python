# 🌲🌊🚁🟩🔥🏬💛🧺⛅️⚡️🏆

from pynput import keyboard
from clouds import Clouds
from map import Map
import time
import os
import json
from helicopter import Helicopter as Aircraft

TICK_INTERVAL = 0.2
TREE_FREQUENCY = 50
CLOUDS_FREQUENCY = 100
FIRE_FREQUENCY = 75
MAP_WIDTH, MAP_HEIGHT = 20, 10

game_map = Map(MAP_WIDTH, MAP_HEIGHT)
cloud_cover = Clouds(MAP_WIDTH, MAP_HEIGHT)
helicopter = Aircraft(MAP_WIDTH, MAP_HEIGHT)
current_tick = 1

CONTROL_SCHEME = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def handle_key_event(key):
    global helicopter, current_tick, cloud_cover, game_map
    try:
        key_pressed = key.char.lower()
    except AttributeError:
        return

    if key_pressed in CONTROL_SCHEME:
        dx, dy = CONTROL_SCHEME[key_pressed]
        helicopter.move_helicopter(dx, dy)

    # Сохранение
    
    elif key_pressed == 'f':
        data = {
            "helicopter": helicopter.get_state(),
            "clouds": cloud_cover.get_state(),
            "map": game_map.get_state(),
            "tick": current_tick
        }
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)

    # Загрузка

    elif key_pressed == 'g':
        with open("level.json", "r") as lvl:
            loaded_state = json.load(lvl)
        current_tick = loaded_state.get("tick", 1)
        helicopter.set_state(loaded_state["helicopter"])
        game_map.set_state(loaded_state["map"])
        cloud_cover.set_state(loaded_state["clouds"])

# Обработчик клавиатуры

keyboard_handler = keyboard.Listener(on_press=handle_key_event)
keyboard_handler.start()

def clear_screen():
    print("\033[H\033[J", end="")

while True:
    clear_screen()
    
    game_map.process_aircraft(helicopter, cloud_cover)
    
    game_output = [
        helicopter.show_status(),
        game_map.display(helicopter, cloud_cover),
        f"TICK {current_tick}"
    ]
    
    print("\n".join(game_output))
    
    current_tick += 1
    time.sleep(TICK_INTERVAL)
    
    if current_tick % TREE_FREQUENCY == 0:
        game_map.add_tree()
    if current_tick % FIRE_FREQUENCY == 0:
        game_map.update_fires()
    if current_tick % CLOUDS_FREQUENCY == 0:
        cloud_cover.refresh_clouds()