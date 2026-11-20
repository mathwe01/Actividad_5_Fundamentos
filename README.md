# Gestor de contactos (Laboratorio Tema 5)

Este programa en Python es para practicar persistencia de datos con archivos.
Permite registrar contactos por consola y guardarlos en un archivo de
texto, y también exportarlos a un archivo binario.

## Cómo usarlo
```bash
python gestor_contactos.py
```

Desde el menú se puede:
- agregar un contacto (se guarda en `contactos.txt` sin borrar los anteriores)
- ver la lista de contactos
- buscar por nombre y contar cuántos hay
- exportar a `contactos.dat` y volver a leerlo

# Qué aprendí
Los archivos de texto se pueden abrir y leer fácilmente, mientras que
el binario guarda cada registro con un tamaño fijo y no se entiende si
se abre en un editor. También vi que el modo de apertura importa: con
`"a"` se agregan datos y con `"w"` se borra lo anterior.

*Curso: Fundamentos de Programación*