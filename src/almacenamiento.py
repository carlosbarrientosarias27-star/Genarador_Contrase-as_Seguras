import datetime

def guardar_contrasena_en_archivo(password, fortaleza):
    """
    Pregunta al usuario si desea guardar la contraseña y la escribe
    en contrasenas.txt con metadatos.
    """
    # 1. Preguntar al usuario
    confirmacion = input("\n¿Deseas guardar esta contraseña en el archivo? (s/n): ").lower()
    
    if confirmacion == 's':
        try:
            # 2. Preparar los datos (fecha y hora)
            ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 3. Abrir en modo append ('a') y escribir
            with open("contrasenas.txt", "a", encoding="utf-8") as archivo:
                linea = f"[{ahora}] Pass: {password} | Fortaleza: {fortaleza}\n"
                archivo.write(linea)
            
            # 4. Confirmar al usuario
            print("✅ ¡Éxito! La contraseña se ha guardado correctamente en contrasenas.txt.")
            
        except Exception as e:
            print(f"❌ Error al intentar guardar el archivo: {e}")
    else:
        print("Operación cancelada. La contraseña no fue guardada.")

# Ejemplo de uso:
# guardar_contrasena_en_archivo("A1b2C3d4!", "Alta")