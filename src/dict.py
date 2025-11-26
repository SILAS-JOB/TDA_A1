import utils.cl as cl


"""
Sistema para cadastro de produtos usando dicionários em Python.
"""

prod = {}

while True:
    print("Sistema para cadastro de produtos")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")
    escolha = input("Escolha uma opção: \n")
    if escolha == '1':
        nome = str(input("Digite o nome do produto: \n")).strip()
        preco = float(input("Digite o preço do produto: \n").replace(',', '.'))
        prod[nome] = preco
        print(f"Produto {nome} adicionado com sucesso!")
        cl.clean()
    elif escolha == '2':
        if not prod:
            print("Nenhum produto cadastrado.")
        else:
            print("Produtos cadastrados: \n")
            for nome, preco in prod.items(): # type: ignore
                print(f"Produto: {nome} - Preço: R$ {preco:.2f}")
        cl.clean()
    elif escolha == '3':
        print("Programa Encerrado !")
        cl.clean()
        break
    else:
        print(f"{Exception('Opção inválida')}")
        cl.clean()
