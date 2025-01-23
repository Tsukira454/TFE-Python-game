# Code by ELvin Mouyart
# UTF-08
# main.py
# 23-01-2025
# Fichié principale du jeux

# +--- Imports ---+
from ursina import *


# +--- Fonctions ---+
def update():
    cube.rotation_x = cube_rotation_x + 0.25
    cube.rotation_y = cube_rotation_y + 0.5


# +--- Codes ---+
if __name__ == "__main__":
    app = Ursina()
    cube = Entity(model="cube", color=color.red, texture="white_cube", scale=2)
    app.run()
    
    