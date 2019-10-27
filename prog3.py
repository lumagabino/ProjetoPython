#Luma
#Pietro Ruy Pugliesi - RA: 185921

# python3 prog3.py < arq1.in - como rodar

# Entrada: 1ª linha - velocidade máxima de todas as ruas
#          Linhas seguintes - vertice U, vertice V, distancia, (opcional) velociadade amxima da rua/aresta
#          Linha em branco
#          Linhas seguintes - vertice U, vertice V, velocidades resgistradas
#          Penúltima linha - vértice de origem
#          Última linha - vértice de destino

if __name__ == "__main__":
    velocidade_maxima = float(input())

    arestas  = []
    aresta  = [str(z) if any(i.isalpha() for i in z) else float(z) for z in input().split()]
    while aresta != []:
        arestas.append(aresta)
        aresta  = [str(z) if any(i.isalpha() for i in z) else float(z) for z in input().split()]
    print(arestas)

    velocidades = []
    while True:
        try:
            velocidades_aresta  = [str(z) if any(i.isalpha() for i in z) else float(z) for z in input().split()]
            velocidades.append(velocidades_aresta)
        except EOFError:
            break
    # print(velocidades)

    # Manter a ordem do pop!
    destino = (velocidades.pop(-1)).pop()
    origem = (velocidades.pop(-1)).pop()
    print(velocidades)
    print(origem)
    print(destino)


    



    

