import matplotlib.pyplot as plt
import timeit

# instalar entorno virtual con python -m venv venv
# activar el entorno virtual con ./venv/Scripts/activate
# instalar las dependencias con python install -r requirements.txt


# Comparación de funciones que suman los primeros n números
def sumar_n(n):
    resultado = 0           # 1
    for i in range(n + 1):  # n
        resultado += i      # 2
    return resultado        # 1
# T(n) = 1 + 2 * n + 1 => T(n) = 2n + 2

# Suma de Gauss
def suma_gauss(n):
    return n * (n + 1) // 2
# T(n) = 1 + 1 + 1 + 1 => T(n) = 4


def graficar_comparación(func1, func2):
    # Valores de entrada
    valores_n = list(range(1, 1001, 100))

    # Medición de tiempos
    tiempos_func1 = []
    tiempos_func2 = []

    for n in valores_n:
        tiempo_1 = timeit.timeit(lambda: func1(n), number=10)
        tiempo_2 = timeit.timeit(lambda: func2(n), number=10)
        tiempos_func1.append(tiempo_1)
        tiempos_func2.append(tiempo_2)

    # Gráfico de resultados
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tiempos_func1, label="sumar n", color='blue')
    plt.plot(valores_n, tiempos_func2, label="suma gauss", color='red')
    plt.xlabel("n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    plt.show()

graficar_comparación(sumar_n, suma_gauss)

# Se puede observar que en el gráfico de comparación, la funcion suma_gauss es constante ya que su funcion temporal traducida en notación Big-O es O(1) mientras que sumar_n aumenta su tiempo de ejecución a medida que aumentan los datos de entrada ya que, en notación Big-O se traduce como O(n)
