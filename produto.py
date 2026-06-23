from database import Database

class Produto:
    def __init__(self,nome=None,tipo=None,preco=0,estoque=0):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.estoque = estoque

    def cadastrar(self):
        db = Database()
        tupla = (self.nome,self.tipo,self.preco,self.estoque)
        resposta = db.insert_produto(tupla)
        return resposta
    
    def listar_produtos(self):
        db = Database()
        produtos = db.select_produto()
        return produtos
    
    def selecionar_produto(self,id):
        db = Database()
        produto = db.select_produto_by_id(id)
        return produto
    
    def atualizar_produto(self, dados):
        db = Database()
        res = db.update_produto(dados)
        return res
    
    def deletar_produto(self, id):
        print("Parametro recebido: ",id)
        db = Database()
        prod_delete = db.select_produto_by_id(id)
        return prod_delete