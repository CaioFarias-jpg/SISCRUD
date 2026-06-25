from Produto import Produto

def menu():
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Sair")

while True:
    print(" ***** SYSCRUD ***** ")
    menu()
    op = input("Digite a opção: ")
    if op == '1':
        produto = Produto()
        produto.nome = input("DIGITE O NOME DO PRODUTO: ")
        produto.tipo = input("DIGITE O TIPO DO PRODUTO: ")
        produto.preco = float(input("DIGITE O PREÇO DO PRODUTO: "))
        produto.estoque = int(input("DIGITE O ESTOQUE DO PRODUTO: "))

        res = produto.cadastrar()
        if res == True:
            print("PRODUTO CADASTRADO COM SUCESSO!!!")

    elif op == '2':
        produto = Produto()
        lista_produtos = produto.listar_produtos()
        for produto in lista_produtos:
            print(f" id: {produto[0]} | nome:{produto[1]} | preco: {produto[3]} ")

    elif op == '3':
        prod = Produto()
        id_atualiza = int(input("DIGITE O ID DO PRODUTO QUE DESEJA ATUALIZAR: "))
        prod_atualizar = prod.selecionar_produto(id_atualiza)
        prod_atualizar[1] = input("DIGITE O NOME:  ")
        prod_atualizar[2] = input("DIGITE O TIPO: ")
        prod_atualizar[3] = float(input("DIGITE O PRECO: "))
        prod_atualizar[4] = int(input("DIGITE A QUANTIDADE: "))

        resposta = prod.atualizar_produto( prod_atualizar )
        if resposta == True:
            print("ATUALIZADO COM SUCESSO!!!!")

    elif op == '4':
        id_deletar = int(input("DIGITE O ID PARA DELETAR O PRODUTO: "))
        prod2 = Produto()
        res = prod2.deletar_produto(id_deletar)
        if res == True:
            print("PRODUTO DELETADO COM SUCESSO!!2")

    elif op == '5':
        print("LOGOFF DO SYSCRUD")
        break

    else:
        print("OPÇÃO INVÁLIDA!!!!")