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
