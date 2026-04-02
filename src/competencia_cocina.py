def calcular_puntaje_ronda(puntajes_jueces):
    """
    Recibe un diccionario con los puntajes de los 3 jueces
    y retorna la suma total de la ronda.
    """
    total = 0

    for juez in puntajes_jueces:
        total += puntajes_jueces[juez]

    return total