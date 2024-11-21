# Programa de la pregunta 2

from math import floor

# Definimos los valores de X, Y y Z
X = 0
Y = 2
Z = 2

# Definimos las siguientes variables
L1 = min(X, Y)
L2 = min(X, Z)
L3 = min(Y, Z)
U1 = max(X, Y) + 1
U2 = max(X, Z) + 1
U3 = max(Y, Z) + 1
I = floor((L1 + U1) / 2)
J = floor((L2 + U2) / 2)
K = floor((L3 + U3) / 2)

# Tenemos que el tamaño del tipo es 4
size_of_T = 4

# Cálculo de la dirección en row-major

# Definimos los S
S3 = size_of_T
S2 = (U3 - L3 + 1) * S3
S1 = (U2 - L2 + 1) * S2

direccion_row_major = (I - L1) * S1 + (J - L2) * S2 + (K - L3) * S3 
print("Dirección en row-major:", direccion_row_major)

# Cálculo de la dirección en column-major

# Definimos los S
S1 = size_of_T
S2 = (U1 - L1 + 1) * S1
S3 = (U2 - L2 + 1) * S2

direccion_column_major = (I - L1) * S1 + (J - L2) * S2 + (K - L3) * S3
print("Dirección en column-major:", direccion_column_major)