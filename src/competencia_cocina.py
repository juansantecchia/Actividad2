def calcular_puntaje_ronda(puntajes_jueces):
    """
    Recibe un diccionario con los puntajes de los 3 jueces
    y retorna la suma total de la ronda.
    """
    total = 0

    for juez in puntajes_jueces:
        total += puntajes_jueces[juez]

    return total


def calcular_resultados_de_ronda(scores):
    """
    Calcula el puntaje total de cada participante en una ronda.
    Retorna un diccionario participante -> puntaje.
    """
    resultados = {}

    for participante in scores:
        puntaje = calcular_puntaje_ronda(scores[participante])
        resultados[participante] = puntaje

    return resultados


def obtener_participantes(rounds):
    """
    Obtiene la lista de participantes a partir de la primera ronda.
    """
    participantes = []

    for nombre in rounds[0]["scores"]:
        participantes.append(nombre)

    return participantes


def crear_estadisticas(participantes):
    """
    Crea un diccionario con las estadísticas iniciales de cada participante.
    """
    estadisticas = {}

    for nombre in participantes:
        estadisticas[nombre] = {
            "puntaje_total": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "rondas_jugadas": 0
        }

    return estadisticas


def buscar_ganadores_ronda(resultados_ronda):
    """
    Busca el o los ganadores de una ronda.
    Retorna una lista con los ganadores y el puntaje máximo.
    """
    maximo = None
    ganadores = []

    for participante in resultados_ronda:
        puntaje = resultados_ronda[participante]

        if maximo is None or puntaje > maximo:
            maximo = puntaje
            ganadores = [participante]
        elif puntaje == maximo:
            ganadores.append(participante)

    return ganadores, maximo


def actualizar_estadisticas(estadisticas, resultados_ronda, ganadores):
    """
    Actualiza puntaje total, rondas jugadas, mejor ronda y rondas ganadas.
    """
    for participante in resultados_ronda:
        puntaje = resultados_ronda[participante]

        estadisticas[participante]["puntaje_total"] += puntaje
        estadisticas[participante]["rondas_jugadas"] += 1

        if puntaje > estadisticas[participante]["mejor_ronda"]:
            estadisticas[participante]["mejor_ronda"] = puntaje

    for ganador in ganadores:
        estadisticas[ganador]["rondas_ganadas"] += 1


def construir_tabla(estadisticas):
    """
    Convierte el diccionario de estadísticas en una lista de diccionarios.
    """
    tabla = []

    for participante in estadisticas:
        datos = estadisticas[participante]
        promedio = datos["puntaje_total"] / datos["rondas_jugadas"]

        fila = {
            "nombre": participante,
            "puntaje_total": datos["puntaje_total"],
            "rondas_ganadas": datos["rondas_ganadas"],
            "mejor_ronda": datos["mejor_ronda"],
            "promedio": promedio
        }

        tabla.append(fila)

    return tabla


def ordenar_tabla_por_puntaje(tabla):
    """
    Ordena la tabla de mayor a menor por puntaje total.
    """
    n = len(tabla)

    for i in range(n):
        for j in range(i + 1, n):
            if tabla[j]["puntaje_total"] > tabla[i]["puntaje_total"]:
                auxiliar = tabla[i]
                tabla[i] = tabla[j]
                tabla[j] = auxiliar


def imprimir_tabla(tabla):
    """
    Imprime una tabla de posiciones.
    """
    print("Cocinero       Puntaje   Rondas ganadas   Mejor ronda   Promedio")
    print("-------------------------------------------------------------")

    for fila in tabla:
        nombre = fila["nombre"]
        puntaje = fila["puntaje_total"]
        ganadas = fila["rondas_ganadas"]
        mejor = fila["mejor_ronda"]
        promedio = fila["promedio"]

        print(f"{nombre:<14} {puntaje:<9} {ganadas:<16} {mejor:<13} {promedio:.1f}")

    print("-------------------------------------------------------------")
    print()


def procesar_competencia(rounds):
    """
    Procesa toda la competencia, imprime la tabla por ronda
    y retorna la tabla final.
    """
    participantes = obtener_participantes(rounds)
    estadisticas = crear_estadisticas(participantes)

    numero_ronda = 1

    for ronda in rounds:
        tema = ronda["theme"]
        scores = ronda["scores"]

        resultados_ronda = calcular_resultados_de_ronda(scores)
        ganadores, puntaje_maximo = buscar_ganadores_ronda(resultados_ronda)

        actualizar_estadisticas(estadisticas, resultados_ronda, ganadores)

        tabla = construir_tabla(estadisticas)
        ordenar_tabla_por_puntaje(tabla)

        print(f"Ronda {numero_ronda} - {tema}:")

        if len(ganadores) == 1:
            print(f"Ganador: {ganadores[0]} ({puntaje_maximo} pts)")
        else:
            print(f"Ganadores: {', '.join(ganadores)} ({puntaje_maximo} pts)")

        imprimir_tabla(tabla)

        numero_ronda += 1

    tabla_final = construir_tabla(estadisticas)
    ordenar_tabla_por_puntaje(tabla_final)

    return tabla_final
    