import random
def printar_favoritas():
    file = open("favoritadas.txt","r",encoding="utf8")
    for i in file:
        i = i.strip()
        visualizar(i)
