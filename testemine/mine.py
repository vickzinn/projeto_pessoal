from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
textura_grama = 'Gemini_Generated_Image_oledwpoledwpoled.png'

for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j,0,i), texture=textura_grama, parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                             texture=textura_grama, parent=scene, origin_y=0.5)
                boxes.append(new)
                break 

            if key == 'right mouse down': 
                boxes.remove(box)
                destroy(box)
                break 

app.run()