#Construa uma lista encadeada de objetor jogador, de forma que os jogadores sejam 
#adicionados na lista em ordem crescente pelo número da camisa. O objeto jogador deve 
#conter os atributos nome e número da camisa, além de um atributo fortemente privado 
#chamado posição. 
#A classe jogador, deve ter métodos assessores e modificadores para os atributos que 
#foram necessários.

from jogador import Jogador

#Classe listaJogadores
class ListaJogadores:
    def __init__(self):
        self.inicio = None

    def adicionar_jogador(self, numero_camisa, nome, posicao):
        novo_jogador = Jogador(numero_camisa, nome)
        novo_jogador.set_posicao(posicao)

        if self.inicio is None:
            self.inicio = novo_jogador
        if numero_camisa < self.inicio.get_numero_camisa():
            novo_jogador.proximo = self.inicio
            self.inicio = novo_jogador
        else:
            jogador_atual = self.inicio

            #Percorrer a lista enquanto há jogadores a serem impressos
            while (
                jogador_atual.proximo is not None
                and jogador_atual.proximo.get_numero_camisa() < numero_camisa):

                jogador_atual = jogador_atual.proximo

            novo_jogador.proximo = jogador_atual.proximo
            jogador_atual.proximo = novo_jogador

    def imprimir_lista(self):
        jogador_atual = self.inicio
        while jogador_atual is not None:
            print(
                f"Número da camisa: {jogador_atual.get_numero_camisa()}, Nome: {jogador_atual.get_nome()}, Posição: {jogador_atual.get_posicao()}"
            )
            jogador_atual = jogador_atual.proximo


