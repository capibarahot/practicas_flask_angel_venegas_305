#1.Creando la clase
class vehiculo:
    #creando mi metodo constructor
    def __init__(self,modelo,color,marca,ano):
        #inicialisando los atributos
        self.modelo=modelo
        self.color=color
        self.marca=marca
        self.ano=ano
        #creando los metodos
    def acelerar(self):
            return f"{self.modelo} runnn"
    def frenar(self):
            return f"{self.marca} iiiii"
    #crear los objetos o las instancias
carro1=vehiculo("Tatoma","Negra","Toyota","2026")
carro2=vehiculo("Versa","Rojo","Nissan","2018")
print(carro1.marca)
print(carrro1.modelo)
print(carro2.frenar())
