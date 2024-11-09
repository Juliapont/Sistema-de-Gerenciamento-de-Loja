import random 

# Dicionário que armazena os produtos da loja
produtos = {
    "Canecas BT21": {"preço": 15.00, "estoque": 90},
    "Posters BTS": {"preço": 10.00, "estoque": 80},
    "Cardenos BT21": {"preço": 20.00, "estoque": 70},
    "Pelucia BT21": {"preço": 35.00, "estoque": 100},
    "Bolsa BT21":{"preço": 40.00, "estoque": 90},

}

# Variável que armazena o total de vendas realizadas 
total_vendas = 0.0 

# Função para cadastrar um novo produto 
def casdastrar_produto():
    nome = input("Digite o nome do produto:")
    preço = float(input(f"Digite o preço de {nome}:"))
    estoque = int(input(f"Digite a quantidade em estoque de {nome}:"))
    produtos [nome] = {"preço": preço,"estoque":estoque}
    print(f"Produto {nome} cadastrado com sucesso!\n")

# Função para exibir os produtos disponíveis   
def exibir_produtos():
    print("\nProdutos desponíveis:") 
    for produto, info in produtos.items():
        print(f"{produto} - Preço R${info['preço']:.2f}, Estoque: {info['estoque']} unidades")
    print()

# Função para realizar uma venda 
def realizar_venda():
    global total_vendas
    produto_vendido = input("Digite o nome do produto que deseja comprar: ")    

    #Verificar se o produto existe e se há estoque 
    if produto_vendido in produtos:
        quantidade = int(input(f"Digite a quantidade de {produto_vendido} que deseja comprar:"))
        if produtos[produto_vendido]["estoque"] >= quantidade:
            valor_venda = quantidade * produtos[produto_vendido]["preço"]
            produtos [produto_vendido]["estoque"] -= quantidade
            total_vendas += valor_venda
            print(f"Venda realizada: {quantidade}x {produto_vendido} - Total: R${valor_venda:.2f\}\n")   
        else:
            print("Quantidade em estoque insuficiente.\n")     
    else:
        print("Produto não encontrado.\n")  

# Função para exibir o total das vendas
def exibir_vendas():
    print(f"\nTotal de vendas realizadas: R${total_vendas:.2f}\n")              

# Função para aplicar uma promoção
def sortear_promoção():
    produto_sorteado = random.choice(list(produtos.keys()))   
    desconto = random.randint(10,50) # Desconto entre 10% e 50%
    produtos[produto_sorteado]["preço"] *= (1 - desconto / 100)
    print (f"\nPromoção! O produto {produto_sorteado} está co {desconto}% de desconto!\n")

# Menu principal
def menu():
    while True:
        print("=== Sistema de Gerenciamento de Loja ===")    
        print("1. Cadastrar produto")
        print("2. Exibir produos")
        print("3. Realizar venda")
        print("4. Exibir total de vendas")
        print("5. Sortear promoção")
        print("6. Sair")

        opcao = input("Escolha uma opção:")

        if opcao == "1":
            casdastrar_produto()
        elif opcao =="2":
            exibir_produtos()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            exibir_vendas()
        elif opcao == "6":
            print("Saindo do sistema...")        
            break
        else:
            print("Opeção inválida! Tente novamente.\n") 

# Iniciar o sisema 
menu()               
        

