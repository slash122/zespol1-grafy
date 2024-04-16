#Implementacja algorytmu podanego w materiałach z zajęć
#Parametrem wejściowym jest graf w postaci listy sąsiedztwa (prosto przekonwertować ją na ciąg graficzny)
def components(G):
    # print(G)
    nr = 0
    comp = [-1 for _ in range(len(G))]
    for i in range(len(G)):
        if comp[i] == -1:
            nr+=1
            comp[i] = nr
            components_R(nr,i,G,comp)

    # sprawdzamy ile utworzyło się obszarów spójności
    groups = []
    for i in range(len(comp)):
        if comp[i] not in groups:
            groups.append(comp[i])

    # robimy liste wierzcholkow ktore należą do danej grupy spójności
    node_groups = []
    for i in range(len(groups)):
        node_group=[]
        for j in range(len(comp)):
            if comp[j] == groups[i]:
                node_group.append(j+1)
        node_groups.append(node_group)

    max = node_groups[0]

    for i in range(len(max)):
        max[i] -= 1

    return max


def components_R(nr,i,G,comp):
    for j in range(len(G[i])):
        if comp[G[i][j]-1] == -1:
            comp[G[i][j]-1] = nr
            components_R(nr,G[i][j]-1,G,comp)