class Auto:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.ano)


auto1 = Auto("Toyota", "Corolla", 2022)
auto2 = Auto("Ford", "Mustang", 2024)

auto1.mostrar_informacion()
print("")
auto2.mostrar_informacion()