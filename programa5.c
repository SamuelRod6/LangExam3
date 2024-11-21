// Programa de la pregunta 4

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void suma_filas(int **matriz, int N, int M)
{
    long long suma = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            suma += matriz[i][j];
        }
    }
}

void suma_columnas(int **matriz, int N, int M)
{
    long long suma = 0;
    for (int j = 0; j < M; j++)
    {
        for (int i = 0; i < N; i++)
        {
            suma += matriz[i][j];
        }
    }
}

int main()
{
    int tamanos[] = {1e2, 1e3, 1e4, 1e5, 1e6};
    int num_tamanos = sizeof(tamanos) / sizeof(tamanos[0]);
    int repeticiones = 3;

    for (int s1 = 0; s1 < num_tamanos; s1++)
    {
        for (int s2 = 0; s2 < num_tamanos; s2++)
        {
            int N = tamanos[s1];
            int M = tamanos[s2];

            // Intentamos asignar memoria para la matriz
            int **matriz = (int **)malloc(N * sizeof(int *));
            if (matriz == NULL)
            {
                printf("No se pudo asignar memoria para la matriz de tamaño N=%d, M=%d\n", N, M);
                continue;
            }

            int error = 0;
            for (int i = 0; i < N; i++)
            {
                matriz[i] = (int *)malloc(M * sizeof(int));
                if (matriz[i] == NULL)
                {
                    printf("No se pudo asignar memoria para la matriz de tamaño N=%d, M=%d\n", N, M);
                    error = 1;
                    break;
                }
            }

            // Si hubo un error, liberamos la memoria y continuamos con el siguiente tamaño
            if (error)
            {
                for (int i = 0; i < N; i++)
                {
                    if (matriz[i] != NULL)
                    {
                        free(matriz[i]);
                    }
                }
                free(matriz);
                continue;
            }

            // Medimos el tiempo para suma_filas
            for (int r = 0; r < repeticiones; r++)
            {
                clock_t inicio = clock();
                suma_filas(matriz, N, M);
                clock_t fin = clock();
                double tiempo_tomado = ((double)(fin - inicio)) / CLOCKS_PER_SEC;
                printf("suma_filas: N=%d, M=%d, repeticion=%d, tiempo=%.6f segundos\n", N, M, r + 1, tiempo_tomado);
            }

            // Medimos el tiempo para suma_columnas
            for (int r = 0; r < repeticiones; r++)
            {
                clock_t inicio = clock();
                suma_columnas(matriz, N, M);
                clock_t fin = clock();
                double tiempo_tomado = ((double)(fin - inicio)) / CLOCKS_PER_SEC;
                printf("suma_columnas: N=%d, M=%d, repeticion=%d, tiempo=%.6f segundos\n", N, M, r + 1, tiempo_tomado);
            }

            // Liberamos la memoria asignada
            for (int i = 0; i < N; i++)
            {
                free(matriz[i]);
            }
            free(matriz);
        }
    }

    return 0;
}
