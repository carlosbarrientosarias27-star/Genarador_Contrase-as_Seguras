import datetime

def guardar_contrasena_en_archivo(password, fortaleza):
    """
    Pregunta al usuario si desea guardar la contraseña y la escribe
    en contrasenas.txt con metadatos.
    """
    confirmacion = input("\n¿Deseas guardar esta contraseña en el archivo? (s/n): ").lower()
    
    if confirmacion == 's':
        try:
            # Obtener fecha y hora actual
            ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Abrir archivo en modo 'a' (append) para añadir contenido al final
            with open("contrasenas.txt", "a", encoding="utf-8") as archivo:
                linea = f"[{ahora}] Pass: {password} | Fortaleza: {fortaleza}\n"
                archivo.write(linea)
            
            print("✅ ¡Éxito! La contraseña se ha guardado correctamente en contrasenas.txt.")
            
        except Exception as e:
            print(f"❌ Error al intentar guardar el archivo: {e}")
    else:
        print("Operación cancelada. La contraseña no fue guardada.")

# Ejemplo de uso:
# guardar_contrasena_en_archivo("A1b2C3d4!", "Alta")