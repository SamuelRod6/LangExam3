# Programa de la pregunta 3

# CLASES
class Atomico:
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = int(representacion)
        self.alineacion = int(alineacion)

class Struct:
    def __init__(self, nombre, tipos):
        self.nombre = nombre
        self.tipos = tipos

class Union:
    def __init__(self, nombre, tipos):
        self.nombre = nombre
        self.tipos = tipos

class ManejadorTipos:
    def __init__(self):
        self.tipos = {}
        
        

    def agregar_atomico(self, nombre, representacion, alineacion):
        if nombre in self.tipos:
            print(f"Error: El tipo {nombre} ya existe.")
            return
        self.tipos[nombre] = Atomico(nombre, representacion, alineacion)

    def agregar_struct(self, nombre, tipos):
        if nombre in self.tipos:
            print(f"Error: El tipo {nombre} ya existe.")
            return
        for tipo in tipos:
            if tipo not in self.tipos:
                print(f"Error: El tipo {tipo} no está definido.")
                return
        self.tipos[nombre] = Struct(nombre, tipos)

    def agregar_union(self, nombre, tipos):
        if nombre in self.tipos:
            print(f"Error: El tipo {nombre} ya existe.")
            return
        for tipo in tipos:
            if tipo not in self.tipos:
                print(f"Error: El tipo {tipo} no está definido.")
                return
        self.tipos[nombre] = Union(nombre, tipos)

    def describir(self, nombre):
        if nombre not in self.tipos:
            print(f"Error: El tipo {nombre} no está definido.")
            return
        tipo = self.tipos[nombre]
        if isinstance(tipo, Atomico):
            print(f"Tipo atómico {nombre}: Tamaño {tipo.representacion} bytes. Alineación {tipo.alineacion} bytes.")
        elif isinstance(tipo, Struct):
            alineacion = self.tipos[tipo.tipos[0]].alineacion
            tamaño_sin_empaquetar = 0
            tamaño_empaquetado = 0
            # tamaño_reordenado = 0
            diferencia = 0
            desperdicio_sin_empaquetar = 0
            # desperdicio_reordenado = 0
            for t in tipo.tipos:
                tamaño_empaquetado += self.tipos[t].representacion
                # La diferencia es la cantidad de bytes que se desperdician por alineación del tipo
                diferencia = tamaño_sin_empaquetar % self.tipos[t].alineacion
                desperdicio_sin_empaquetar +=  diferencia
                tamaño_sin_empaquetar += self.tipos[t].representacion
                tamaño_sin_empaquetar += diferencia
            print(f"Struct {nombre}:")
            print(f"Alineación: {alineacion} bytes.")
            print(f"Tamaño sin empaquetar: {tamaño_sin_empaquetar} bytes. Desperdicio sin empaquetar: {desperdicio_sin_empaquetar} bytes.")
            print(f"Tamaño empaquetado: {tamaño_empaquetado} bytes. Desperdicio empaquetado: 0 bytes.")
            # print(f"Tamaño reordenado: {tamaño_reordenado} bytes. Desperdicio reordenado: {desperdicio_reordenado} bytes.")
        elif isinstance(tipo, Union):
            tamaño = max([self.tipos[t].representacion for t in tipo.tipos])
            alineacion = 1
            # Creo que no lo explicó en clases pero creería que el desperdicio de un Union
            # es a los sumo la diferencia entre la representación del tipo más grande y la representación del tipo más pequeño
            desperdicio = max([self.tipos[t].representacion for t in tipo.tipos]) - min([self.tipos[t].representacion for t in tipo.tipos])
            for t in tipo.tipos:
                alineacion = mcm(alineacion, self.tipos[t].alineacion)
            print(f"Union {nombre}:")
            print(f"Tamaño: {tamaño} bytes. Alineación: {alineacion} bytes.")
            print(f"Desperdicio: El desperdicio en cualquiera de las implementaciones es a lo sumo {desperdicio} bytes.")
                
# FUNCIONES AUXILIARES

# Calcula el mínimo común múltiplo de dos números
def mcm(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

# MAIN
def main():
    manejador = ManejadorTipos()
    while True:
        accion = input("Ingrese una acción: ").strip().split()
        if not accion:
            continue
        comando = accion[0].upper()
        if comando == "ATOMICO":
            if len(accion) != 4:
                print("Error: Formato incorrecto para ATOMICO.")
                continue
            _, nombre, representacion, alineacion = accion
            manejador.agregar_atomico(nombre, representacion, alineacion)
        elif comando == "STRUCT":
            if len(accion) < 3:
                print("Error: Formato incorrecto para STRUCT.")
                continue
            nombre = accion[1]
            tipos = accion[2:]
            manejador.agregar_struct(nombre, tipos)
        elif comando == "UNION":
            if len(accion) < 3:
                print("Error: Formato incorrecto para UNION.")
                continue
            nombre = accion[1]
            tipos = accion[2:]
            manejador.agregar_union(nombre, tipos)
        elif comando == "DESCRIBIR":
            if len(accion) != 2:
                print("Error: Formato incorrecto para DESCRIBIR.")
                continue
            nombre = accion[1]
            manejador.describir(nombre)
        elif comando == "AYUDA":
            print("Comandos disponibles:")
            print("  - ATOMICO <nombre> <representación> <alineación>: Agrega un tipo atómico.")
            print("  - STRUCT <nombre> <tipo1> <tipo2> ...: Agrega un tipo struct.")
            print("  - UNION <nombre> <tipo1> <tipo2> ...: Agrega un tipo union.")
            print("  - DESCRIBIR <nombre>: Muestra información sobre un tipo.")
            print("  - SALIR: Termina el programa.")
        elif comando == "SALIR":
            break
        else:
            print("Error: Comando no reconocido. (Escriba ayuda para ver los comandos disponibles)")

if __name__ == "__main__":
    main()

# Las pruebas se encuentran en el archivo test_programa4.py