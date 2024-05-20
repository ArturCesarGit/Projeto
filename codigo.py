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
def favoritar(nome_fav):
    while True:
        try:
            nome = open(f"{nome_fav}.txt", "r", encoding="utf8")
            nome.close()    
            favoritas = open("favoritadas.txt", "a", encoding="utf8")
            favoritas.write(f"\n{nome_fav}\n")
            favoritas.close()
            break
        
        except FileNotFoundError:
            print("receita não encontrada")
def visualizar(receita):
    try:
        file = open("receitas.txt", "r", encoding="utf8")
        linhas = file.readlines()
        if (f"{receita}\n") not in linhas:
            file.close()
            print("receita não encontrada")
            
        else:
            file.close()
            printar = open(f"{receita}.txt","r",encoding="utf8")
            print(printar.read())
            printar.close()
    except FileNotFoundError:
        print("arquivo não encontrado")
def cadastrar_receita():
    try:
        j = 0
        ingredientes = []
        preparo = []
        nome = input("Digite o nome da receita: ")
        pais = input("Digite o país da receita: ")
        qnti = int(input("Digite quantos ingredientes tem a receita: "))

        nova_receita = open(f"{nome}.txt", "w", encoding="utf8")
        nova_receita.write(f"Nome: {nome}\n")
        nova_receita.write("\n")
        nova_receita.write(f"País: {pais}\n")
        nova_receita.write("\n")
        nova_receita.write("Ingredientes:\n")

        for i in range(qnti):
            ingredientes.append(input(f"Digite o {i+1}° ingrediente da receita: "))
            nova_receita.write(f"- {ingredientes[i]}.\n")
        nova_receita.write("\n")
        nova_receita.write("Modo de Preparo:\n")
        
        while True:
            preparo.append(input(f"Digite o {j+1}° passo da receita: "))
            nova_receita.write(f"{j +1}. {preparo[j]}.\n")
            alt = input("Deseja adicionar mais um passo a receita? (s/n): ").lower()
            j += 1
            if alt == "n":
                break
        
        fav = input("Deseja adicionar essa receita à lista de receitas favoritas? [S/N] : ").lower()
        if fav == 's':
            favoritar(nome)
        
        nova_receita.close()
        with open("receitas.txt", "a", encoding="utf8") as banco:
            banco.write(f"\n{nome}\n")
        
        visualizar(nome)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
def excluir_receita(receita):
    while True:
        try:
            nome = open(f"{receita}.txt","w",encoding="utf8")
            nome.close()
            banco = open("receitas.txt", "r", encoding="utf8")
            linhas  = banco.readlines()
            banco.close()
            banco = open("receitas.txt","w",encoding="utf8")
            for linha in linhas:
                if receita not in linha:
                    banco.write(linha)
            banco.close()
            break
        except FileNotFoundError:
            print("receita não encontrado no banco de dados")
            escolha = input("deseja excluir outra receita?(s/n)").lower()
            if escolha == "s":
                receita = input()
            else:
                break
