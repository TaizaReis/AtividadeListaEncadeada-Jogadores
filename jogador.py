#Método construtor
#Classe jogador, com seus atributos e métodos
class Jogador:
    def __init__(self, numero_camisa, nome):
        self.numero_camisa = numero_camisa
        self.nome = nome
        self.__posicao = None
        self.proximo = None


#Métodos para ACESSAR e MODIFICAR 
    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_numero_camisa(self):
        return self.numero_camisa

    def set_numero_camisa(self, numero_camisa):
        self.numero_camisa = numero_camisa
        
