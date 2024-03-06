import pandas as pd
import numpy as np

def read_excel_file(file_path):
    """
    Read the Excel file and return the distance matrix.
    """
    df = pd.read_excel(file_path, index_col=0)
    return df.values, df.index.tolist()

def la_plus_forte_descente_2_echanges(distances):
    """
    Apply the 'la plus forte descente 2-echanges' algorithm to find the best route.
    """
    n = len(distances)
    # Initialize the current route randomly
    current_route = np.random.permutation(n)
    best_distance = calculate_distance(current_route, distances)

    # Number of iterations
    max_iterations = 1000
    iteration = 0

    # Main loop of the algorithm
    while iteration < max_iterations:
        # Generate two random indices
        i, j = np.random.choice(n, 2, replace=False)
        # Swap the cities at indices i and j
        new_route = current_route.copy()
        new_route[i], new_route[j] = new_route[j], new_route[i]
        # Calculate the new distance
        new_distance = calculate_distance(new_route, distances)
        # If the new distance is better, update the current route and best distance
        if new_distance < best_distance:
            current_route = new_route
            best_distance = new_distance
        iteration += 1

    return current_route, best_distance

def calculate_distance(route, distances):
    """
    Calculate the total distance of a route.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i], route[i + 1]]
    total_distance += distances[route[-1], route[0]]  # Return to the starting city
    return total_distance

if __name__ == "__main__":
    # File path of the Excel file
    excel_file_path = input("Veuillez saisir le chemin du fichier Excel : ")
    
    # Read the Excel file
    distances, city_names = read_excel_file(excel_file_path)

    # Apply the algorithm
    best_route, best_distance = la_plus_forte_descente_2_echanges(distances)

    # Output the best route and distance
    print("Best route:", best_route)
    print("Best distance:", best_distance)


