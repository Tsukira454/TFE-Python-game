from ursina import *
class TextureBox(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="texture.jpg",
            color=color.color(0,0,1)
        )
        
        self.texture_choice = 0
        self.textures = ["textures/block/stone.png", "textures/block/stone_bricks.png", "textures/block/iron_ore.png"]
        
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.texture_choice += 1
                self.texture_choice %= len(self.textures)
                self.texture = self.textures[self.texture_choice]