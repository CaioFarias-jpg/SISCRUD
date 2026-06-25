#### exemplo de classe

class Cachorro:
    def __init__(self,nome,cor): ##### MÉTODO CONSTRUTOR
        self.name = nome
        self.color = cor

    def get_nome(self):
        return self.name

    def set_nome(self,novo_nome):
        self.name = novo_nome

    def get_cor(self):
        return self.color

    def latir(self):
        print(self.nome , " AU AU AU ")


dog1 = Cachorro("BILU","BRANCO") ##OBJETO
dog1.get_nome()

dog2 = Cachorro("LAILA","AMARELA") ### OUTRO OBJETO
dog2.get_nome()

dog2.set_nome("BELA")
dog2.get_nome()