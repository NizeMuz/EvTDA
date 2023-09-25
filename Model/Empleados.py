class Empleados:
    def __init__(self, nombre_completo="", rut="", sexo="", direccion="", telefono="", cargo="", fecha_ingreso="", area="", departamento=""):
        self.nombre_completo = nombre_completo
        self.rut = rut
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.fecha_ingreso = fecha_ingreso
        self.area = area
        self.departamento = departamento

    def getNombreCompleto(self):
        return self._nombre_completo

    def getRut(self):
        return self._rut

    def getSexo(self):
        return self._sexo

    def getDireccion(self):
        return self._direccion

    def getTelefono(self):
        return self._telefono

    def getCargo(self):
        return self._cargo

    def getFechaIngreso(self):
        return self._fecha_ingreso

    def getArea(self):
        return self._area

    def getDepartamento(self):
        return self._departamento

    def setNombreCompleto(self, nombre_completo):
        self._nombre_completo = nombre_completo

    def setRut(self, rut):
        self._rut = rut

    def setSexo(self, sexo):
        self._sexo = sexo

    def setDireccion(self, direccion):
        self._direccion = direccion

    def setTelefono(self, telefono):
        self._telefono = telefono

    def setCargo(self, cargo):
        self._cargo = cargo

    def setFechaIngreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    def setArea(self, area):
        self._area = area

    def setDepartamento(self, departamento):
        self._departamento = departamento

    def toString(self):
        return f"""Nombre completo: {self._nombre_completo}
        \nRUT: {self._rut}
        \nSexo: {self._sexo}
        \nDirección: {self._direccion}
        \nTeléfono: {self._telefono}
        \nCargo: {self._cargo}
        \nFecha de ingreso: {self._fecha_ingreso}
        \nÁrea: {self._area}
        \nDepartamento: {self._departamento}
        """
