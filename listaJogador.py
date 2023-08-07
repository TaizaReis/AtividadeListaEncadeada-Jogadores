from jogador import Jogador

class ListaJogador:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def add_jogador(self, numero_camisa, nome, posicao):
        novo_jogador = Jogador(numero_camisa, nome, posicao)

        if self.inicio is None or numero_camisa < self.inicio.numero_camisa:
            novo_jogador.proximo = self.inicio
            self.inicio = novo_jogador
        else:
            jogador_anterior = self.inicio
            jogador_atual = self.inicio.proximo

            while (
                jogador_atual is not None
                and jogador_atual.numero_camisa < numero_camisa
            ):
                jogador_anterior = jogador_atual
                jogador_atual = jogador_atual.proximo

            novo_jogador.proximo = jogador_atual
            jogador_anterior.proximo = novo_jogador

        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio is None:
            print("Lista Vazia")
        else:
            print("-----------")
            jogador_atual = self.inicio
            while jogador_atual is not None:
                print(f"Número da camisa: {jogador_atual.numero_camisa}, Nome: {jogador_atual.nome}, Posição: {jogador_atual._posicao}")
                jogador_atual = jogador_atual.proximo
            print("Total de elementos:", str(self.tamanho))

    def remover_inicio(self):
        if self.inicio is None:
            print("Lista Vazia")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        self.imprimir()

    def remover_fim(self):
        if self.inicio is None:
            print("Lista Vazia")
        elif self.inicio.proximo is None:
            self.inicio = None
            self.tamanho = 0
        else:
            jogador_anterior = self.inicio
            jogador_atual = self.inicio.proximo
            while jogador_atual.proximo is not None:
                jogador_anterior = jogador_atual
                jogador_atual = jogador_atual.proximo

            jogador_anterior.proximo = None
            self.tamanho -= 1
        self.imprimir()
