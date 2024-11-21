# Programa de la pregunta 1.b.i

# Definimos la clase Church y sus subclases Zero y Suc
class Church:
    pass

# Definimos las subclases Zero y Suc, que son solo constructores de tipo
class Zero(Church):
    # Modificamos el método __repr__ para poder ver que imprime
    def __repr__(self):
        return "Cero"


class Suc(Church):
    def __init__(self, predecessor):
        self.predecessor = predecessor
    # Modificamos el método __repr__ para poder ver que imprime
    def __repr__(self):
        return f"Suc({repr(self.predecessor)})"


def suma(a, b):
    if isinstance(a, Zero):
        return b
    elif isinstance(a, Suc):
        return Suc(suma(a.predecessor, b))

def mult(a, b):
    if isinstance(a, Zero):
        return Zero()
    elif isinstance(a, Suc):
        return suma(b, mult(a.predecessor, b))
    
# De esta forma podemos aplicar suma y multiplicación de tipo con los numerales de Church
# unicamente representados por la contaste Zero y la función Suc

    
# PRUEBAS
a = Suc(Suc(Suc(Zero())))
b = Suc(Suc(Zero()))
print(f"a = {a}")
print(f"b = {b}")
print(f"Suma de a y b: {suma(a, b)}")
print(f"Multiplicación de a y b: {mult(a, b)}")
