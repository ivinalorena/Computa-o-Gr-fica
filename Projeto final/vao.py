from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])

        # MESA vao
        self.vaos['mesa'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['mesa'])
        #paredes
        self.vaos['estrutura'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['estrutura'])
        #Quadro 1
        self.vaos['quadro1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['quadro1'])
        #Quadro 2
        self.vaos['quadro2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['quadro2'])
        #Quadro 3
        self.vaos['quadro3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['quadro3'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()