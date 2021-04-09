from ursina import *
import random
from ursina.prefabs.first_person_controller import FirstPersonController
class grapling_hook(Entity):
        def __init__(self,scale=(1,1,1),rotation=(0,0,0),position=(0,0,0),texture='white_cube',model='cube'):
          super().__init__(
             parent=camera.ui,
             position = position,
             model=model,
             rotation=rotation,
             texture=texture,
             color= color.white,
             collider='none',
             scale=scale,
             target='none'
             )
        def input(self,key):
             if key == 'x':
                hit_info = raycast(player.position+(0,1,0), camera.forward , ignore=(self,), distance=20, debug=True)
                if hit_info.hit:
                        Entity(position=hit_info.world_point,model='cube',color=color.color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
                        self.target=hit_info.world_point
t=0 
def update():
        global t
        if grapp.target!='none':
                t += time.dt
                player.position += (grapp.target - player.position) / 50
                if t > 1:
                        grapp.target='none'
                        t=0
app = Ursina()
player=FirstPersonController(position=(0,50,0))
grapp=grapling_hook(position=(.5,-.5,0),rotation=(10,90,0),scale=(1,.5,.5))
floor=Entity(model='plane', scale=(20,0,20), color=color.red,collider='mesh')
box=Entity(model='cube',texture='white_cube',position=(6,10,5),collider='box')
app.run()
