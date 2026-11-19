import os
import struct

ARCHIVO_TXT = "contactos.txt"
ARCHIVO_BIN = "contactos.dat"
FORMATO = "i30s15s"
TAM_REGISTRO = struct.calcsize(FORMATO)

def siguiente_id():
    if not os.path.exists(ARCHIVO_TXT):
        return 1
    ultimo = 0
    with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if partes[0].isdigit():
                ultimo = max(ultimo, int(partes[0]))
    return ultimo + 1

def ingresar_contacto():
    nombre = input("Nombre ").strip()
    telefono = input("Telefono ").strip()
    if not nombre or not telefono:
        print("El nombre y el teléfono no pueden estar vacíos.")
        return None
    return siguiente_id(), nombre, telefono

def guardar_texto(contacto):
    with open(ARCHIVO_TXT, "a", encoding="utf-8") as f:
        f.write(f"{contacto[0]},{contacto[1]},{contacto[2]}\n")
    print("Contacto guardado en", ARCHIVO_TXT)
    
def menu():
    while True:
        print("=== GESTOR DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            contacto = ingresar_contacto()
            if contacto:
                guardar_texto(contacto)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    menu()
    



