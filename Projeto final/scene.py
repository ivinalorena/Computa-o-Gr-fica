from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # chão 20,2
        n, s = 10, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
        
        #mesa 1,-1,1
        add(mesa(app,pos =(2,-1,1))) 
        add(estrutura(app,pos=(1,-1,-3)))
        #Quadros
        add(quadro1(app,pos=(1,-1,-2.6)))
        add(quadro2(app,pos=(3,-1,-2.6)))
        add(quadro3(app,pos=(5,-1,-2.6)))
        

    