# Code by ELvin Mouyart
# UTF-08
# main.py
# 23-01-2025
# Fichié principale du jeu

# +--- Imports ---+
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import math

# +--- Fonctions ---+

def generate_world(seed, size=50, max_height=10):
    """
    Génère un monde de taille donnée avec des variations de hauteur.
    - seed : graine pour la génération aléatoire
    - size : taille de la carte (size x size)
    - max_height : hauteur maximale du terrain
    """
    texture_base = [
        "textures/block/granite.png",  # Herbe (pour le sommet)
        "textures/block/dirt.png",         # Terre (en dessous)
        "textures/block/stone.png"         # Pierre (plus en profondeur)
    ]

    random.seed(seed)  # Initialiser la graine pour garantir la reproductibilité

    for z in range(size):
        for x in range(size):
            # Générer la hauteur avec une fonction de bruit procédural
            height = int((math.sin(x * 0.1 + seed) + math.cos(z * 0.1 - seed)) * max_height / 2 + max_height / 2)

            for y in range(height + 1):
                # Choisir la texture en fonction de la hauteur
                if y == height:
                    texture = texture_base[0]  # Herbe
                elif height - y < 3:
                    texture = texture_base[1]  # Terre
                else:
                    texture = texture_base[2]  # Pierre

                # Placer le cube
                Entity(model='cube', position=(x, y, z), texture=texture)

# +--- Codes ---+
if __name__ == "__main__":
    app = Ursina()

    # Générer un monde avec une seed spécifique
    generate_world(seed=42, size=50, max_height=15)

    # Ajouter le joueur avec une vue à la première personne
    player = FirstPersonController()
    player.y = 20  # Position initiale au-dessus du terrain

    app.run()
