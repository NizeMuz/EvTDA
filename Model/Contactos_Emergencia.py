class ContactosEmergencia:
    def __init__(self, nombre="", relacion="", telefono=""):
        self.nombre = nombre
        self.relacion = relacion
        self.telefono = telefono

    def get_nombre(self):
        return self.nombre

    def get_relacion(self):
        return self.relacion

    def get_telefono(self):
        return self.telefono

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_relacion(self, relacion):
        self.relacion = relacion

    def set_telefono(self, telefono):
        self.telefono = telefono

    def __str__(self):
        return f"""Nombre: {self.nombre}
        Relación: {self.relacion}
        Teléfono: {self.telefono}
        """
 