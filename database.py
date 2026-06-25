import mysql.connector

class Database:
    def __init__(self,banco='syscrud'):
        self.local = 'localhost'
        self.user = 'root'
        self.password = ''
        self.banco = banco

    def conectar(self):
        conexao = "MYSQL"
        self.conn = mysql.connector.connect(host=self.local,database=self.banco,user=self.user,password=self.password)
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            return db_info
        else:
            print("ERRO AO CONECTAR AO BANCO DE DADOS!!!")

    def insert_produto(self,dados:tuple):
        self.conectar()
        try:
            self.cursor.execute('INSERT INTO produto (nome,tipo,preco,qtde_estoque) VALUES (%s,%s,%s,%s)',dados) 
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

        finally:
            self.disconnect()


    def select_produto(self):
        self.conectar()  #### INICIANDO A CONEXÃO
        try:
            self.cursor.execute(" SELECT * FROM produto; ")
            produtos = self.cursor.fetchall() #### CONVERTER O OBJETO DO BANCO PARA UMA LISTA DE DICIONARIOS
            return produtos

        except Exception as error:
            print(error)

        finally:
            self.disconnect() ## ENCERRANDO A CONEXÃO


    def select_cliente(self):
        self.conectar()
        try:
            self.cursor.execute(" SELECT * FROM cliente; ")
            clientes = self.cursor.fetchall() #### CONVERTER O OBJETO DO BANCO PARA UMA LISTA DE DICIONARIOS
            return clientes

        except Exception as error:
            print(error)

        finally:
            self.disconnect() ## ENCERRANDO A CONEXÃO

    def select_produto_by_id(self,id_produto:int):
        self.conectar()
        try:
            self.cursor.execute(f" SELECT * FROM produto WHERE id_produto = {id_produto} ")
            prod = self.cursor.fetchone() #### CONVERTER O OBJETO DO BANCO PARA UMA LISTA DE DICIONARIOS
            return list(prod)

        except Exception as error:
            print(error)

        finally:
            self.disconnect() ## ENCERRANDO A CONEXÃO

    def update_produto(self,dados:tuple):
        self.conectar()
        try:
            self.cursor.execute(f"""
                                UPDATE produto SET nome='{dados[1]}',
                                tipo = '{dados[2]}', preco='{dados[3]}',
                                qtde_estoque = '{dados[4]}'
                                WHERE id_produto = {dados[0]}
                                """)
            self.conn.commit()
            return True
        
        except Exception as e:
            print(e)

        finally:
            self.disconnect() ## ENCERRANDO A CONEXÃO

    def delete_produto(self,id_produto):
        self.conectar()
        try:
            self.cursor.execute(f" DELETE FROM produto WHERE id_produto={id_produto};")
            self.conn.commit()
            # print("DELETADO COM SUCESSO!!!!")
            return True
        except Exception as error:
            print(error)

        finally:
            self.disconnect() ## ENCERRANDO A CONEXÃO

    def disconnect(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            # print("Conexão encerrada com sucesso!!")



if __name__ == "__main__":
    banco = Database()
    banco.insert_produto()  