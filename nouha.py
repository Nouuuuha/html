import pandas as pd
import copy

# Function to calculate the total distance of a tour
def total_distance(tour, distance_matrix):
    total = 0
    for i in range(len(tour) - 1):
        j = i + 1
        total += distance_matrix[tour[i]][tour[j]]
    total += distance_matrix[tour[0]][tour[-1]]  # Add distance from last to first point
    return total

# Function to implement the 2-opt swap
def two_opt_swap(tour, i, j):
    new_tour = copy.deepcopy(tour)
    sub_tour = new_tour[i:j + 1]
    sub_tour.reverse()
    new_tour[i:j + 1] = sub_tour
    return new_tour

# Load distance matrix from Excel file
def load_distance_matrix_from_excel(file_path):
    data = pd.read_excel(file_path, header=None)
    distance_matrix = data.values.tolist()
    return distance_matrix

# Main code
file_path = 'distance_matrix.xlsx'  # Update with your file path
distance_matrix = load_distance_matrix_from_excel(file_path)

# Initial tour (can be any order)
initial_tour = [0, 1, 2, 3, 4]

# Main optimization loop
improved = True
while improved:
    improved = False
    for i in range(1, len(initial_tour) - 2):
        for j in range(i + 1, len(initial_tour) - 1):
            new_tour = two_opt_swap(initial_tour, i, j)
            if total_distance(new_tour, distance_matrix) < total_distance(initial_tour, distance_matrix):
                initial_tour = new_tour
                improved = True

# Print the optimized tour and its total distance
print("Optimized tour:", initial_tour)
print("Total distance:", total_distance(initial_tour, distance_matrix))
