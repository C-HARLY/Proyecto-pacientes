import json
import os

#  Ruta del archivo donde guardaremos los pacientes
ARCHIVO_JSON = "pacientes.json"

#  Guardar pacientes en JSON
def guardar_pacientes(pacientes):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=4)
    print(" Datos guardados en JSON correctamente.")

# Cargar pacientes 
def cargar_pacientes():
    if not os.path.exists(ARCHIVO_JSON):
        return []  
    with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)
