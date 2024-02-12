from Treballador2 import Treballador

def calcul_cost_treballador(treballador):
    """
    Calcula el cost total d'un treballador, tenint en compte el seu salari base i les hores extres.

    Paràmetres:
        treballador (Treballador): Objecte que representa al treballador.

    Retorna:
        float: El cost total del treballador, incloent el seu salari base i les hores extres.

    """
    if treballador.getTipusTreballador() == [Treballador.DIRECTOR, Treballador.SUBDIRECTOR]:
            return treballador.getNomina()
    else:
        return treballador.getNomina() + (treballador.getHoresExtres()*20)
    

def calculaCostDelPersonal(treballadors: list):
    """
    Calcula el cost total del personal d'una empresa sumant els costos individuals de cada treballador.

    Paràmetres:
        treballadors (list): Llista d'objectes Treballador que representen el personal de l'empresa.

    Retorna:
        float: El cost total del personal de l'empresa, sumant els costos individuals de cada treballador.

    """
    costFinal = 0
    for treballador in treballadors:
        costFinal += calcul_cost_treballador(treballador)
    return costFinal


