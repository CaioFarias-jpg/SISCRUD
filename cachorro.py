class cachorro:
    def __init__(self, nome, cor):
        self.name = nome
        self.cor = cor
    
    def gert_nome(self):
        print(self.name)

    def get_cor(self):
        print(self.cor)

    def latir(self):
        print(self.name, "AU AU AU")

dog1 = cachorro("Bilu", "Branco")
dog1.get_nome()

dog2 = cachorro("laila", "amarela")
dog2.get_nome()