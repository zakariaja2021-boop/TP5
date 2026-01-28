def trouver_maximum(liste):
    if not liste:  # vérifier si la liste est vide
        return None
    
    maximum = liste[0]
    
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    
    return maximum