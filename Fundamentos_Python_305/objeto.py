#1.Definimos la clase
class perro:

    def __init__(self,nombre,raza,comecroquetas):
        #Definicion de los atributos
        self.nombre=nombre
        self.raza=raza
    #Metodo del comportamiento
    def ladrar(self):
        def comer(self):
            return f"{self.nombre} come croquetas"
        return f"{self.nombre}dise:¡Guau"
    #2. Creamos los objetos (instancias de la clase)
mi_perro=perro("firulais","labrador")
otro_perro=perro("solovino","electrico")
#.3Usar objetos
print(mi_perro.nombre)#Acceder al atributo nombre
print(otro_perro.ladrar())#Acceder al metodo
print(mi_perro.comecroquetas())
