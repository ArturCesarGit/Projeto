import random
def printar_favoritas():
    file = open("favoritadas.txt","r",encoding="utf8")
    for i in file:
        i = i.strip()
        visualizar(i)
def aleatoria():
    vetor = []
    file=open("receitas.txt","r", encoding="utf8")
    for linha in file:
     vetor.append(linha) 

    file.close()
    nome = random.choice(vetor)
    nome = nome.strip()
    receita = open(f"{nome}.txt","r",encoding="utf8")
    print(receita.read())
    receita.close()

