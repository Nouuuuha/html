import pandas as pd
import numpy as np
import random

def distance(point1, point2):
    """Calcul de la distance euclidienne entre deux points"""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(points_order, points):
    """Calcul de la distance totale parcourue en visitant les points dans l'ordre donné"""
    total = 0
    for i in range(len(points_order)-1):
        total += distance(points[points_order[i]], points[points_order[i+1]])
    return total

def descente_2_echanges(points):
    """Algorithme de la plus forte descente 2-échanges"""
    n = len(points)
    # Générer une solution initiale aléatoire
    solution_actuelle = list(range(n))
    random.shuffle(solution_actuelle)
    meilleure_solution = solution_actuelle.copy()
    meilleure_distance = total_distance(meilleure_solution, points)
    amelioration = True
    while amelioration:
        amelioration = False
        for i in range(n-1):
            for j in range(i+1, n):
                nouvelle_solution = meilleure_solution[:i] + meilleure_solution[i:j][::-1] + meilleure_solution[j:]
                nouvelle_distance = total_distance(nouvelle_solution, points)
                if nouvelle_distance < meilleure_distance:
                    meilleure_solution = nouvelle_solution
                    meilleure_distance = nouvelle_distance
                    amelioration = True
    return meilleure_solution, meilleure_distance

# Charger les données à partir du fichier Excel
data = pd.read_excel('points.xlsx')

# Convertir les données en liste de tuples de coordonnées (x, y)
points = [(row['x'], row['y']) for index, row in data.iterrows()]

# Appliquer l'algorithme de la plus forte descente 2-échanges
meilleure_solution, meilleure_distance = descente_2_echanges(points)

print("Meilleure solution trouvée:", meilleure_solution)
print("Distance totale parcourue:", meilleure_distance)
