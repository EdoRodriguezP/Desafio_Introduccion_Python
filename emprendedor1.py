

p = float(input("Ingresa el precio de suscripcion : ")) # Se realiza solicitud de ingreso de datos
u = float(input("Ingresa el numero de usuarios : "))
gt = float(input("Ingrsa el gasto total : "))

utilidades = p * u - gt                                # Se realiza operacion matematica

print(f"La utilidad obtenida es : {utilidades}")       # Se imprime resultado