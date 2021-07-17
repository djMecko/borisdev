def matrizT(matriz):
    t=[]
    for i in range(len(matriz[0])):
        t.append([])
        for j in range(len(matriz)):
            t[i].append(matriz[j][i])
    return t
k=matrizT([[1,2,3],[3,4,5],[6,7,8]])
print(k)