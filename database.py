import mysql.connector

class Database:
    def __init__(self,banco='syscrud'):
        self.local = '10.28.2.22'
        self.user = 'devweeb'
        self.password = 'suporte@22'
        self.banco = banco

    def conectar(self):
        self.conn = mysql.connector.connect(host=self.local,database=self.banco,user=self.user,password=self.password)
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("CONECTADO COM SUCESSO:",db_info)
        else:
            print("ERRO AO CONECTAR AO BANCO DE DADOS!!")

    def insert_produto(self):
        param = ("Coca-cola", "refri", 12.00, 50)
        self.conectar()
        try:
            self.cursor.execute("INSERT INTO produto (nome,tipo,preco,qtde_estoque) VALUES (%s,%s,%s,%s)",param)
            self.conn.commit()
            print("PRODUTO CADASTRADO COM SUCESSO!")

        except Exception as error:
            print(error)

if __name__ == "__main__":
    banco = Database()
    banco.insert_produto()

