# se pide el sueldo
sueldo=float(input)("introduce el sueldo del empleado:")
if sueldo>5000:
    aumento=sueldo*0.05
elif sueldo>2000 and sueldo < 5000:
    aumento=sueldo*0.10
else:
        aumento=0
 print("el aumento  del sueldo es de:",aumento)
 print("el nuevo sueldoes:",sueldo+aumento)

































 