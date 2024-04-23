from utils.random_weighted import generate_random_weighted_graph

def init(G, s):
    global ds, ps
    ds = {}  # Inicjalizacja słownika odległości
    ps = {}  # Inicjalizacja słownika poprzedników

    # Inicjalizacja odległości dla każdego wierzchołka na nieskończoność
    for v in G.nodes():
        ds[v] = float('inf')
        ps[v] = []  # Inicjalizacja pustej listy poprzedników

    ds[s+1] = 0  # Odległość od źródła do samego siebie wynosi 0


def relax(u, v, w):
    global ds, ps
    if ds[v] > ds[u] + w.get((u, v), float('inf')):
        ds[v] = ds[u] + w.get((u, v), float('inf'))
        ps[v] = u  # Dodajemy tylko poprzedników na najkrótszej ścieżce



def dijkstra(G, w, s):
    global ds, ps
    init(G, s)
    S = set()  # Zbiór odwiedzonych wierzchołków

    while S != set(G.nodes()):

        # Wybierz wierzchołek o najmniejszej odległości spośród tych, które jeszcze nie są w zbiorze S
        u = min((node for node in G.nodes() if node not in S), key=lambda x: ds[x])

        S.add(u)
        # Wykonaj relaksację dla wszystkich krawędzi wychodzących z wierzchołka u
        for v in G.neighbors(u):

            if v in S:
                continue
            relax(u, v, w)

    # Wypisywanie scieżek dla konkretych wierzchołków

    #print("Ścieżki")
    paths = []
    for key,val in ds.items():
        path="d("+str(key)+") = " + str(val) + " ==> [ " + str(s+1) + " -"
        path2=""
        path2+=get_path(key,path2,s+1)
        path2 = path2[::-1]
        path2 = path2.replace("-", "", 1)
        path2 = path2.replace(" ", "", 1)
        path_full = path + path2 + " - " + str(key) + "]"
        path_full = path_full.replace("- -", "-")
        
        paths.append(path_full)
        # print(path_full)
    
    return paths, ds


# Funkcja rekurencyjna do znajdowania scieżek
def get_path(v,path,s):
    global ps
    while ps[v] != []:
        if ps[v] == s:
            break
        path = path + str(ps[v]) + " - "
        return get_path(ps[v],path,s)
    return path