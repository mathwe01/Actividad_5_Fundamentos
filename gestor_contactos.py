import os
import struct

ARCHIVOS_TXT = "contactos.txt"
ARCHIVOS_BIN = "contactos.dat"
FORMATO = "i30s15s"
TAM_REGISTRO = struct.calcsize(FORMATO)

def menu():
    while True:
        print("=== GESTOR DE CONTACTOS ===")
        print("0. Salir")
        opcion = input("Opción ").strip()
        
        if opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida")
            
if __name__ == "__main__":
    menu()
    



