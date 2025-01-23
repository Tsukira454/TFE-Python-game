from ursina import *
class cube(Button):
    def __init__(self, position=(5,2,4), texture="textures/block/no_texture.png"):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,1)
        )
        
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            if key == 'right mouse down':
                cube(self.position)