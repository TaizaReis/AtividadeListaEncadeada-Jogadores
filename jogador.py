#Construa uma lista encadeada de objetor jogador, de forma que os jogadores sejam 
#adicionados na lista em ordem crescente pelo número da camisa. O objeto jogador deve 
#conter os atributos nome e número da camisa, além de um atributo fortemente privado 
#chamado posição. 
#A classe jogador, deve ter métodos assessores e modificadores para os atributos que 
#foram necessários.
class Jogador:
    def __init__(self, numero_camisa, nome, posicao):
        self.numero_camisa = numero_camisa
        self.nome = nome
        self._posicao = posicao

    def get_posicao(self):
        return self._posicao

    def set_posicao(self, posicao):
        self._posicao = posicao
        

