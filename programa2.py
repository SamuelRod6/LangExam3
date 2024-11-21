# Programa de la pregunta 1.b.ii

# Creamos un tipo ConjuntoPersonas que tiene un constructor que inicializa una lista vacía
class ConjuntoPersonas:
    # Creamos el tipo Persona con un constructor que recibe un nombre y una edad
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
    
    def __init__(self):
        self.personas = [] 

    def agregar_persona(self, nombre, edad):
        self.personas.append(self.Persona(nombre, edad))

    def cantidad_personas(self):
        return len(self.personas)

    def mayores_de_edad(self):
        return [persona.nombre for persona in self.personas if persona.edad >= 18]

    def nombre_mas_comun(self):
        from collections import Counter
        nombres = [persona.nombre for persona in self.personas]
        contador = Counter(nombres)
        return contador.most_common(1)[0][0]
    

# PRUEBAS
conjunto = ConjuntoPersonas()
conjunto.agregar_persona("Juan", 20)
conjunto.agregar_persona("Pedro", 15)
conjunto.agregar_persona("Juan", 25)
conjunto.agregar_persona("Ana", 20)
conjunto.agregar_persona("Pedro", 16)
conjunto.agregar_persona("Ana", 15)
conjunto.agregar_persona("Ana", 20)
conjunto.agregar_persona("Juan", 20)

print(f"Cantidad de personas: {conjunto.cantidad_personas()}")
print(f"Personas mayores de edad: {conjunto.mayores_de_edad()}")
print(f"Nombre más común: {conjunto.nombre_mas_comun()}")