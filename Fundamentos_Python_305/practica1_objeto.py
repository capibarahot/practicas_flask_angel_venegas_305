class Producto:
    def __init__(self, nombre, precio, cantidad):
       self.nombre = nombre
       self.precio = precio
       self.cantidad = cantidad
    def calcular_total(self):
       return self.precio * self.cantidad

producto1 = Producto("Cuaderno", 35.50, 3)
print("Producto:", producto1.nombre)
print("Precio:", producto1.precio)
print("Cantidad:", producto1.cantidad)
print("Total:", producto1.calcular_total())