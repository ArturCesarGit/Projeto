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
def filtrar_por_pais(pais):
            try:
        
    
                receitas_filtradas = []
                paises = open("receitas.txt", "r", encoding="utf8")
                for receita in paises:
                     receita = receita.strip()
                
                     file = open(f"{receita}.txt", "r", encoding="utf8")
                     for linha in file:
                         if pais in linha:
                             receitas_filtradas.append(receita) 
                             break
                         file.close()
            
                paises.close()
                for i  in range(len(receitas_filtradas)):
                  file = open(f"{receitas_filtradas[i]}.txt","r",encoding="utf8")
                  print(file.read())
                  file.close()
            
              
            except FileNotFoundError:
                print("pais não encontrado no banco de dados")
def atualizar_receita(nome_arquivo):
   
    file = open(f"{nome_arquivo}.txt", 'r', encoding='utf-8')
    linhas = file.readlines()
    file.close()

   
    nome = linhas[0].strip()
    pais = linhas[2].strip()
    index_ingredientes = linhas.index("Ingredientes:\n")
    index_modo_preparo = linhas.index("Modo de Preparo:\n")
    
    ingredientes = linhas[index_ingredientes + 1:index_modo_preparo]
    modo_preparo = linhas[index_modo_preparo + 1:]

    def exibir_lista(lista):
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item.strip()}")

    def alterar_lista(lista):
        while True:
            exibir_lista(lista)
            alterar = input("Deseja alterar algum item? (sim/não): ").strip().lower()
            if alterar != 'sim':
                break
            indice = int(input("Qual o número do item que deseja alterar? ")) - 1
            novo_valor = input("Digite o novo valor: ").strip()
            lista[indice] = novo_valor + '\n'

    
    alterar = input("Deseja alterar algum ingrediente? (sim/não): ").strip().lower()
    if alterar == 'sim':
        alterar_lista(ingredientes)

    
    alterar = input("Deseja alterar o modo de preparo? (sim/não): ").strip().lower()
    if alterar == 'sim':
        alterar_lista(modo_preparo)

  
    file = open(f"{nome_arquivo}.txt", 'w', encoding='utf-8')
    file.write(f"{nome}\n\n{pais}\n\nIngredientes:\n")
    file.writelines(ingredientes)
    file.write("\nModo de Preparo:\n")
    file.writelines(modo_preparo)
    file.close()

    print("Receita atualizada com sucesso!")

def filtrar_por_ingrediente(ingrediente):
 
             try:    
                receitas_filtradas_ingrediente = []
                ingredientes = open("receitas.txt", "r", encoding="utf8")
                for receita in ingredientes:
                     receita = receita.strip()
                
                     file = open(f"{receita}.txt", "r", encoding="utf8")
                     for linha in file:
                         if ingrediente in linha:
                             receitas_filtradas_ingrediente.append(receita) 
                             break
                     file.close()
            
                ingredientes.close()
                for i  in range(len(receitas_filtradas_ingrediente)):
                  file = open(f"{receitas_filtradas_ingrediente[i]}.txt","r",encoding="utf8")
                  print(file.read())
                  file.close()
             
              
             except FileNotFoundError:
                print("ingrediente não encontrado no banco de dados")
