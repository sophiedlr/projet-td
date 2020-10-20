#tableau = var globale

def select_lignes(date1, date2) :
    '''Crée un nouveau tableau "periode" avec les lignes du tableau de base comprises entre les deux dates incluses '''
    periode = []
    for ligne in tableau :
        if ligne[-1]>=date1 and ligne[-1]<=date2 :
            periode.append(ligne)
    return periode