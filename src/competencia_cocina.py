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