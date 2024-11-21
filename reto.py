# Programa del reto
from math import log2, floor
from scipy.special import binom

# FUNCIONES

# Función de Narayana
def narayana(n, k):
    if k == 0 or k > n:
        return 0
    return (1.0 / n) * binom(n, k) * binom(n, k - 1)

# Función Tribonacci
def trib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    trib_values = [0, 1, 2]
    for i in range(3, n + 1):
        trib_values.append(trib_values[-1] + trib_values[-2] + trib_values[-3])
    return trib_values[n]

# Función maldad
def maldad(n):
    narayana_value = narayana(n, int(floor(log2(n))))
    if narayana_value == 0:
        return 0
    return trib(int(floor(log2(narayana_value))) + 1)

# MAIN
if __name__ == "__main__":
    n = int(input("Ingrese el valor de n: "))
    print(maldad(n))