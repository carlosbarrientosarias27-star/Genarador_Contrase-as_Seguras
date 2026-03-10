import os
from datetime import datetime

def guardar_en_archivo(passwords_con_fortaleza):
    """Guarda una lista de contraseñas y su fortaleza en un archivo de texto.

    Crea la carpeta de destino si no existe y añade las contraseñas al final 
    del archivo con una marca de tiempo.

    Args:
        passwords_con_fortaleza (list): Lista de tuplas (password, fortaleza).

    Returns:
        bool: True si la operación fue exitosa, False en caso contrario.
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # CORRECCIÓN: Usa guion bajo en lugar de punto en el nombre de la variable
    nombre_carpeta = "Contraseña"
    nombre_archivo = "Contraseñas.txt"  # El valor sí puede llevar punto porque es un texto
    
    # La ruta une la carpeta "contraseña" con el archivo "Contraseñas.txt"
    ruta_completa = os.path.join(nombre_carpeta, nombre_archivo)
    
    try:
        # Crear la carpeta si no existe para evitar errores de ruta
        if not os.path.exists(nombre_carpeta):
            os.makedirs(nombre_carpeta, exist_ok=True)
            
        with open(ruta_completa, "a", encoding="utf-8") as f:
            for pw, fort in passwords_con_fortaleza:
                f.write(f"[{ahora}] Pass: {pw} | Fortaleza: {fort}\n")
        
        print(f"\n✅ Guardado en: {ruta_completa}")
        return True
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return False