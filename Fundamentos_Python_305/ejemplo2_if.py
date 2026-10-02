#programa beca san jose sin hambre
#evaluando si el almno tiene una calificacion mayor a 8
#y menor a 10
calificacion=float (input("introce tu calificacion"))
nombre=input("introduce tu nombre")
if calificacion<=10 and calificacion>=8:
     print("felicidades"+nombre+"ganaste una beca de 1000")
# evaluando si el alumno tiene una calificacion mayor a 6
#y menor a 8
elif calificacion<8 and calificacion>6:
    print("felicidades"+nombre+"ganaste una beca de 500")
else:
    print(""+nombre+"no fuiste feneficiado")
