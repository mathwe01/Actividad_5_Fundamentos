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
    
def leer_contactos():
    contactos = []
    try:
        with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",") 
                if len(partes) == 3:
                    contactos.append((int(partes[0]), partes[1], partes[2]))
    except FileNotFoundError:
        pass
    return contactos

def mostrar_contactos():
    contactos = leer_contactos()
    if not contactos:
        print("No hay contactos registrados.")
        return
    print(f"\n{'ID':<5}{'Nombre':<25}{'Teléfono':<15}")
    print("-" * 45)
    for id_, nombre, tel in contactos:
        print(f"{id_:<5}{nombre:<25}{tel:<15}")
    print()
    
def buscar_contacto():
    texto = input("Nombre a buscar: ").strip().lower()
    encontrados = [c for c in leer_contactos() if texto in c[1].lower()]
    if encontrados:
        for id_, nombre, tel in encontrados:
            print(f" ID {id_} | {nombre} | {tel}")
    else:
        print("No se encontraron coincidencias.")
            
def contar_contactos():
    print("Total de contactos:", len(leer_contactos()))
    
def exportar_a_binario():
    contactos = leer_contactos()
    with open(ARCHIVO_BIN, "wb") as f:
        for id_, nombre, tel in contactos:
            f.write(struct.pack(FORMATO, id_, nombre.encode("utf-8"), tel.encode("utf-8")))
    print(f"{len(contactos)} contactos guardados en {ARCHIVO_BIN} "
                  f"({os.path.getsize(ARCHIVO_BIN)} bytes)")
            
def leer_binario():
    if not os.path.exists(ARCHIVO_BIN):
        print("Aún no existe el archivo binario. Use la opción de exportar.")
        return
    print(f"\n{'ID':<5}{'Nombre':<25}{'Telefono':<15}")
    print("-" * 45)
    with open(ARCHIVO_BIN, "rb") as f:
        while True:
            bloque = f.read(TAM_REGISTRO)
            if len(bloque) < TAM_REGISTRO:
                break
            id_, nombre, tel = struct.unpack(FORMATO, bloque)
            nombre = nombre.rstrip(b"\x00").decode("utf-8")
            tel = tel.rstrip(b"\x00").decode("utf-8")
            print(f"{id_:<5}{nombre:<25}{tel:<15}")
    print()
        
                
def menu():
    while True:
        print("=== GESTOR DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Mostrar contactos (texto)")
        print("3. Buscar contacto")
        print("4. Contar contactos")
        print("5. Exportar a archivo binario")
        print("6. Leer archivo binario")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            contacto = ingresar_contacto()
            if contacto:
                guardar_texto(contacto)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            contar_contactos()
        elif opcion == "5":
            exportar_a_binario()
        elif opcion == "6":
            leer_binario()
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    menu()
    



