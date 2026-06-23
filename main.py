from produto import Produto

prod = Produto()

id_atualiza = int(input("Digite o id do produto que deseja atualizar: "))

prod_atualizar = prod.selecionar_produto(id_atualiza)
print(prod_atualizar)

prod_atualizar[1] = input("Digite o nome: ")
prod_atualizar[2] = input("Digite o tipo: ")
prod_atualizar[3] = float(input("Digite o preço: "))
prod_atualizar[4] = int(input("Digite a quantidade: "))

resposta = prod.atualizar_produto(prod_atualizar)
if resposta == True:
    print("Atualizado com sucesso")













































# print(prod)
# # prod.nome = input("Digite o nome do produto: ")
# # prod.tipo = input("Digite o tipo do produto: ")
# # prod.preco = float(input("Digite o preço do produto: "))
# # prod.estoque = int(input("Digite o estoque do produto: "))

# # res = prod.cadastrar()
# # if res == True:
# #     print("PRODUTO CADASTRADO COM SUCESSO!")

# lista_produtos = prod.listar_produtos()
# for prod in lista_produtos:
#     print(f" id: {prod[0]} / nome: {prod[1]} / preco: {prod[3]} ")

# id_deletar = int(input("Digite o id do produto que deseja deletar: "))
# prod2 = Produto()
# prod2.deletar_produto(id_deletar)