def generar_correo(nombre, apellido, fecha):
    
    fecha = fecha [-2:]
    nombre = nombre [:2]
    apellido = apellido [-2:]
    
    correo = nombre + apellido + fecha + "@gmail.com"
    
    return correo

nombre = input("ingresa tu numbre: ").lower()
apellido = input("ingresa tu apellido: ").lower()
fecha = input("inggresa tu fecha de nacimiento (dd/mm/aaaa): ")

correo = generar_correo(nombre, apellido, fecha)
print("tu correo generado es: ", correo)

