import networkx as nx
# from draw import draw_with_circle

# sprawdza, czy dana sekwencja liczb naturalnych jest ciągiem graficznym
def degree_seq(A):
    A = sorted(A, reverse=True)
    n = len(A)
    while True:
        # sprawdzamy czy tablica sklada sie z samych zer (jesli tak - ciag graficzny)
        non_zero = False
        for el in A:
            if el != 0:
                non_zero = True
        if not non_zero:
            return True
        
        # sprawdzmy czy tablicy zawiera elementy wieksze niz n (jesli tak - ciag nie jest graficzny)
        if A[0] >= n:
            return False
        
        # sprawdzmy czy tablicy zawiera elementy ujemne (jesli tak - ciag nie jest graficzny)
        for el in A:
            if el < 0:
                return False
        
        # zmniejszamy o 1 stopien A[0] wierzcholkow zaczynajac od indeksu jeden 
        i = 1
        while i <= A[0]:
            A[i] -= 1
            i += 1
        # i zerujemy wierzcholek o najwiekszym stopniu
        A[0] = 0

        # sortujemy tablice nierosnaco
        A = sorted(A, reverse=True)


# konstruuje graf prosty o stopniach wierzchołkow zadanych przez ciąg graficzny 
def create_graph(A):
    
    # sprawdzamy czy podany ciag na pewno jest graficzny
    if not degree_seq(A):
        raise Exception("To nie jest ciag graficzny")

    n = len(A)
    G = nx.Graph()

    # dodajemy n wierzcholkow do grafu
    G.add_nodes_from(range(1,n+1))

    # sortujemy tablice nierosnaco na wejsciu
    A = sorted(A, reverse=True)

    # tablica indeksow
    index_list = [i for i in range(1,n+1)]

    # dopoki tablica posiada dodanie elementy
    while True:
        non_zero = False
        for el in A:
            if el != 0:
                non_zero = True
        if not non_zero:
            # jesli w tablicy zostaly same zera, zwracamy graf
            return G
        
        # sortowanie tablicy A nierosnaco, wrac z indeksami
        # wspomoglem sie stackiem
        # https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other
        A, index_list = (list(t) for t in zip(*sorted(zip(A, index_list), reverse=True, key=lambda x: x[0])))
        
        # dodajemy A[0] krawedzi 
        for node in index_list[1:A[0]+1]:
            G.add_edge(index_list[0], node)

        # zmniejszamy stopien o 1 wierzcholkow, do ktorych poprowadzilismy krawedx
        for i in range(1,A[0]+1):
            A[i] -= 1

        # zerujemy stopien wierzholka, z ktorego prowadzilismy krawedzie do pozostalych
        A[0] = 0