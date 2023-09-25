class CargaFamiliar:
    def __init__(self,id ,nombre="", parentesco="", sexo="", rut=""):
        self.id = id
        self.nombre = nombre
        self.parentesco = parentesco
        self.sexo = sexo
        self.rut = rut

    def get_nombre(self):
        return self.nombre

    def get_parentesco(self):
        return self.parentesco

    def get_sexo(self):
        return self.sexo

    def get_rut(self):
        return self.rut

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_parentesco(self, parentesco):
        self.parentesco = parentesco

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_rut(self, rut):
        self.rut = rut

    def __str__(self):
        return f"""Nombre: {self.nombre}
        Parentesco: {self.parentesco}
        Sexo: {self.sexo}
        Rut: {self.rut}
        """
