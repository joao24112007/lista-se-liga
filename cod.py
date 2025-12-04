nivel = float ( input (" Digite o nivel do reservatorio (%) : ") )
 if nivel < 20:
 print (" Nivel Critico - Ligar Bomba de Emergencia ")
 elif 20 <= nivel <= 80:
 print (" Nivel Operacional - Monitorar ")
 else :
 print (" Nivel Alto - Desligar Entrada ") 
tensoes = [12.5 , 11.9 , 13.1 , 10.5 , 12.0 , 11.8 , 13.5 , 12.2 , 11.5 , 12.8]
 soma = 0
 fora_faixa = 0

 for t in tensoes :
 soma += t
 if t < 11.5 or t > 12.5:
 fora_faixa += 1

 media = soma / len( tensoes )
 print ( f" Media : { media :.2f}V")
 print ( f" Max : { max( tensoes )}V, Min: {min( tensoes )}V")
 print ( f" Leituras fora da faixa : { fora_faixa }")
matriz = [
 [1 , 2 , 3] ,
 [4 , 5 , 6] ,
 [7 , 8 , 9]
 ]
 soma_diagonal = 0

 print (" Matriz :")
 for i in range (3) :
10 print ( matriz [ i ])
11 soma_diagonal += matriz [ i ][ i ] # Elemento onde linha = coluna
12
13 print ( f" Soma da Diagonal Principal : { soma_diagonal }")
print("\n=== SISTEMA DE CONTROLE DE ESTOQUE ===")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Calcular valor total do estoque")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome do produto: ")
        try:
            preco = float(input("Preço do produto: "))
        except ValueError:
            print("Preço inválido! Tente novamente.")
            continue
        
        produtos.append({"nome": nome, "preco": preco})
        print(f"Produto '{nome}' adicionado com sucesso!")
    
    elif opcao == "2":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\n--- Lista de Produtos ---")
            for i, p in enumerate(produtos, start=1):
                print(f"{i}. {p['nome']} - R$ {p['preco']:.2f}")
    
    elif opcao == "3":
        total = sum(p["preco"] for p in produtos)
        print(f"Valor total do estoque: R$ {total:.2f}")
    
    elif opcao == "0":
        print("Saindo do programa... Até mais!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
