import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.jpg')
    
        self.textures['mesa'] = self.get_texture(path='objects/mesadebilhar/10523_Pool_Table_v1_Diffuse.jpg')
        self.textures['estrutura'] = self.get_texture(path='textures/parede(3).jpg')
        self.textures['quadro1'] = self.get_texture(path='textures/quadro(1).jpg')
        self.textures['quadro2'] = self.get_texture(path='textures/quadro(2).jpg')
        self.textures['quadro3'] = self.get_texture(path='textures/quadro(1).jpg')
        self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture
    

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]