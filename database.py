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
        param = ("Arroz", "alimento", 10.00, 20)
        self.conectar()
        try:
            self.cursor.execute("INSERT INTO produto (nome,tipo,preco,qtde_estoque) VALUES (%s,%s,%s,%s)",param)
            self.conn.commit()
            print("PRODUTO CADASTRADO COM SUCESSO!")

        except Exception as error:
            print(error)

        finally:
            self.disconnect()


    def select_produto(self):
        self.conectar()
        try:
            self.cursor.execute("SELECT * FROM produto; ")
            produtos = self.cursor.fetchall()  ###Converter o objeto do banco para uma lista de dicionarios
            for prod in produtos:
                print(f" id: {prod[0]} / nome: {prod[1]} / preco: {prod[3]} ")
        except Exception as error:
            print(error)

        finally:
            self.disconnect()    


    def select_produto_by_id(self, id_produto):
        self.conectar()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id_produto = {id_produto}; ")
            prod = self.cursor.fetchone()  ###Converter o objeto do banco para uma lista de dicionarios
            return list(prod)
        
        except Exception as error:
            print(error)

        finally:
            self.disconnect()


    def update_produto(self, id_prod):
        self.conectar()
        try:
            prod = self.select_produto_by_id(id_prod)
            print(prod)
            prod[1] = input("Digite o nome: ")
            prod[2] = input("Digite o tipo: ")
            prod[3] = float(input("Digite o preço: "))
            prod[4] = int(input("Digite a quantidade: "))
            print(prod)
            self.cursor.execute(f"""
                                UPDATE produto SET nome = '{prod[1]}',
                                tipo = '{prod[2]}', preco = '{prod[3]}',
                                qtde_estoque = '{prod[4]}'
                                WHERE id_produto = '{prod[0]}';
                                """)
            self.conn.commit()
            print("PRODUTO ATUALIZADO COM SUCESSO!!!")
        except:
            pass

        finally:
            self.disconnect()


    def delete_produto(self, id_produto):
        self.conectar()
        try:
            self.cursor.execute(f" DELETE FROM produto WHERE id_produto={id_produto}; ")
            self.conn.commit()
            print("DELETADO COM SUCESSO!")
        except Exception as error:
            print(error)

        finally:
            self.disconnect()

    def disconnect(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("CONEXÃO ENCERRADA COM SUCESSO!!")

if __name__ == "__main__":
    banco = Database()
    banco.update_produto(1)