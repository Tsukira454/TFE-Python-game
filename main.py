# Code by ELvin Mouyart
# UTF-08
# main.py
# 23-01-2025
# Fichié principale du jeux

# +--- Imports ---+
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from classe.TextureBox import *

# +--- Fonctions ---+
def update():
    ...


# +--- Codes ---+
if __name__ == "__main__":
    app = Ursina()
    for z in range(10):
        for x in range(10):
            Entity(
                model="cube", color=color.dark_gray, collider="box", ignore=True,
                position = (x, 0, z),
                parent=scene,
                origin_y = 0.5,
                texture = "white_cube"
            )

    TextureBox()
    player = FirstPersonController()
    app.run()
    
    