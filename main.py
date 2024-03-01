while True:
    edad_input = input("Ingrese la edad: ")
    if edad_input.isdigit():
        edad = int(edad_input)
        if edad >= 0:
            break
        else:
            print("Error: La edad no puede ser negativa.")
    else:
        print("Error: Debe ingresar un número entero positivo.")

# Calcular la etapa de la vida según la edad ingresada
if edad <= 14:
    etapa = "niño"
elif edad <= 28:
    etapa = "joven"
elif edad <= 60:
    etapa = "adulto"
else:
    etapa = "adulto mayor"

print(f"La persona tiene {edad} años y está en la etapa de su vida {etapa}.")
