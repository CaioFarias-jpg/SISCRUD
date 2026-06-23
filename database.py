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

    def insert_produto(self,dados):
        self.conectar()
        try:
            self.cursor.execute("INSERT INTO produto (nome,tipo,preco,qtde_estoque) VALUES (%s,%s,%s,%s)",dados)
            self.conn.commit()
            return True

        except Exception as error:
            print(error)

        finally:
            self.disconnect()


    def select_produto(self):
        self.conectar()
        try:
            self.cursor.execute("SELECT * FROM produto; ")
            produtos = self.cursor.fetchall()  ###Converter o objeto do banco para uma lista de dicionarios
            return produtos
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


    def update_produto(self, dados):
        self.conectar()
        try:
            self.cursor.execute(f"""
                                UPDATE produto SET nome = '{dados[1]}',
                                tipo = '{dados[2]}', preco = '{dados[3]}',
                                qtde_estoque = '{dados[4]}'
                                WHERE id_produto = '{dados[0]}';
                                """)
            self.conn.commit()
            return True
        except:
            pass

        finally:
            self.disconnect()


    def delete_produto(self, id_produto):
        self.conectar()
        try:
            self.cursor.execute(f" DELETE FROM produto WHERE id_produto={id_produto}; ")
            self.conn.commit()
            return True
        
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