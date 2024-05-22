import pandas as pd
import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg') 
import matplotlib.pyplot as plt
import networkx as nx
import base64
import io

def read_data(file_path):
    df = pd.read_csv(file_path, sep=' ', header=None, names=['x', 'y'])
    points = df.to_numpy().tolist()
    return points
# Funkcja symulująca wyżarzanie (implementacja algorytmu z zajęć)
def simulated_annealing(initial_cycle, max_iterations):
    P = initial_cycle[:]
    T = 0.001 * len(P)**2

    for i in range(100, 1, -1):
        T = 0.001 * i**2

        for it in range(max_iterations):
            a, b = random.sample(range(len(P)), 2)
            c, d = random.sample(range(len(P)), 2)

            # Zamiana krawędzi (a, b) i (c, d) na (a, c) i (b, d)
            Pnew = P[:]
            Pnew[min(a, b):max(a, b)+1], Pnew[min(c, d):max(c, d)+1] = Pnew[min(a, b):max(a, b)+1], Pnew[min(c, d):max(c, d)+1][::-1]

            d_Pnew = calculate_distance(Pnew)
            d_P = calculate_distance(P)

            if d_Pnew < d_P:
                P = Pnew[:]
            else:
                r = random.random()
                if r < math.exp(-(d_Pnew - d_P) / T):
                    P = Pnew[:]

    return P

# Funkcja obliczająca odległość
def calculate_distance(path):
    distance = 0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    x1, y1 = path[-1]
    x2, y2 = path[0]
    distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Funkcja do rozwiązania problemu
# Zwraca cykt w postaci listy oraz długośc cyklu
def solve_tsp(file_path, max_iterations):
    points = read_data(file_path)
    initial_cycle = points[:]

    result = simulated_annealing(initial_cycle, max_iterations)
    distance = calculate_distance(result)
    print("Najlepszy znaleziony cykl:", result)
    print("Długość cyklu:", distance)

    return result,distance


def plot_tsp(path, title):

    x = [point[0] for point in path]
    y = [point[1] for point in path]

    x.append(path[0][0])
    y.append(path[0][1])

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_tsp_to_img(path, title):
    x = [point[0] for point in path]
    y = [point[1] for point in path]

    x.append(path[0][0])
    y.append(path[0][1])

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, dpi=360, format='png')
    my_stringIObytes.seek(0)
    img = base64.b64encode(my_stringIObytes.read()).decode()
    return img


# Przykład użycia
# if __name__ == "__main__":
#     file_path = "data.csv"
#     max_iterations = 1000

#     points = read_data(file_path)
#     print(calculate_distance(points))
#     plot_tsp(points, "Dane początkowe")
#     result,distance = solve_tsp(file_path, max_iterations)
#     plot_tsp(result,"Najlepszy znaleziony cykl")