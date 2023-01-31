# Restauracion-de-estado-de-ejecucion

#### BARAJAS GOMEZ JUAN MANUEL | 216557005 | COMPUTACION TOLERANTE A FALLAS | 24/01/2023

## Objetivo:
Generar un programa que sea capaz de restaurar el estado de ejecución
(Application checkpointing)
Checkpointing is a technique that provides fault tolerance for computing systems. 

## Desarollo:
Para poder desarrollar el programa a ejemplar sera necesario utilizar la libreria "Pickle".
"Pickle" es una biblioteca de Python que permite serializar objetos de Python en un formato binario, 
que puede ser guardado en disco o transmitido a través de una red. 
Esto permite guardar estructuras de datos complejas (por ejemplo, listas, diccionarios, clases personalizadas) 
en un archivo y posteriormente cargar los datos en la memoria y recrear los objetos originales. 
"Pickle" se puede utilizar para la persistencia de datos, intercambio de datos entre procesos de Python 
y para crear formatos personalizados para el almacenamiento y transferencia de datos.

## Código:
```python
import pickle

# Crear un objeto
class Persona:
    def __init__(self, nombre, edad, escuela):
        self.nombre = nombre
        self.edad = edad
        self.escuela = escuela

print("Recuperacion de datos con 'Pickle'")
print("Simulacion de restauracion de estado de ejecucion...\n")

# Solicitar datos de una persona al usuario
print("-Datos del alumno-")
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
escuela = input("Ingrese la escuela: ")

persona = Persona(nombre, edad, escuela)

# Guardar los elementos del objeto en un archivo
with open('estados.pickle', 'wb') as f:
    pickle.dump(persona, f)

# Leer y restaurar los elementos del objeto desde un archivo
with open('estados.pickle', 'rb') as f:
    persona_restaurada = pickle.load(f)

# Mostrar los datos restaurados en pantalla
print("\nRecuperando datos... ")
print("\nDatos de alumno recuperados: ")
print("Nombre:", persona_restaurada.nombre)
print("Edad:", persona_restaurada.edad)
print("Escuela:", persona_restaurada.escuela)
```
## Conclusión:
En resumen, "pickle" es una herramienta útil en Python para restaurar el estado de un objeto o conjunto de objetos. 
Al serializar los objetos y guardarlos en un archivo o enviarlos a través de una red, puedes recuperar el estado exacto 
de una sesión previa de trabajo o compartirlo con otros procesos.
Ademas, la restauración de estado es una técnica que permite recuperar el estado de un sistema o aplicación a un momento anterior. 
Esto puede ser útil en casos en los que un sistema o aplicación falla, para permitir una recuperación rápida y sin pérdida de datos. 

Aplicando este sencillo ejemplo con codigo puede funcionar correctamente para evadir la perdida de codigo fuente de un sistema.

## Referencias:
_pickle — Python object serialization. (s. f.). Python documentation. https://docs.python.org/3/library/pickle.html_
