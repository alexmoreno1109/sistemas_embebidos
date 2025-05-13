import array
import machine
import uctypes

def curva_bezier_4_puntos(p0, p1, p2, p3, n):
    """
    Calcula n+1 puntos de la curva de Bézier cúbica dados 4 puntos de control en R^2.
    Cada punto de control debe ser un array tipo 'l' (long) con 2 enteros: [x, y].
    Usa acceso directo a memoria por machine.mem32 y uctypes.
    """
    LR = []  # Lista que almacenará los puntos generados

    # Direcciones de memoria base de cada punto
    dir_p0 = uctypes.addressof(p0)
    dir_p1 = uctypes.addressof(p1)
    dir_p2 = uctypes.addressof(p2)
    dir_p3 = uctypes.addressof(p3)

    for i in range(n + 1):
        t = i / n  # Parámetro t de 0 a 1

        # Cálculo coordenada x usando la fórmula de Bézier cúbica
        Bx = ((1 - t) ** 3) * machine.mem32[dir_p0] + \
             3 * ((1 - t) ** 2) * t * machine.mem32[dir_p1] + \
             3 * (1 - t) * (t ** 2) * machine.mem32[dir_p2] + \
             (t ** 3) * machine.mem32[dir_p3]

        # Coordenada y (está en la dirección base + 4 bytes)
        By = ((1 - t) ** 3) * machine.mem32[dir_p0 + 4] + \
             3 * ((1 - t) ** 2) * t * machine.mem32[dir_p1 + 4] + \
             3 * (1 - t) * (t ** 2) * machine.mem32[dir_p2 + 4] + \
             (t ** 3) * machine.mem32[dir_p3 + 4]

        # Añadir punto a la lista
        LR.append([Bx, By])

    return LR

# Ejemplo de uso:
p0 = array.array("l", [0, 0])
p1 = array.array("l", [1, 2])
p2 = array.array("l", [3, 3])
p3 = array.array("l", [4, 0])
n = 4

resultado = curva_bezier_4_puntos(p0, p1, p2, p3, n)

# Mostrar resultados
print("Puntos de la curva Bézier:")
for punto in resultado:
    print(punto)
