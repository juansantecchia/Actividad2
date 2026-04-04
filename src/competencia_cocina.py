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