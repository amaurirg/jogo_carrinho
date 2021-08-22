import pygame


# Inicia o pygame
pygame.init()


class Carro:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 300
        self.velocidade = 10
        self.imagem = ''

    def deslocar(self, x, y, velocidade):
        ...

    def pos_pista(self, pista):
        pos = {
            'a': 200,
            'b': 400,
            'c': 600
        }
        return pos[pista]

class Ambulancia(Carro):
    def __init__(self):
        super(Ambulancia, self).__init__()


def imagem(img):
    return pygame.image.load(f'./images/{img}')

def titulo(title):
    # Nome que aparece no cabeçalho da janela
    return pygame.display.set_caption(title)

def tamanho(x, y):
    # Define o tamanho da janela
    return pygame.display.set_mode((x, y))


fundo = imagem('/pista6.jpeg')
# Define o tamanho da janela
janela = tamanho(800, 600)
# Nome que aparece no cabeçalho da janela
titulo("Criando um jogo com Python")
# Para fazer o loop mantendo a janela aberta
janela_aberta = True

branco = Carro()
branco.imagem = './images/carro_branco2.png'
branco.pos_pista('a')

while janela_aberta:
    # Delay para atualizar a tela
    pygame.time.delay(50)
    # Para cada evento
    for event in pygame.event.get():
        # Se o evento for QUIT fecha a janela
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Atualiza a tela para limpar o rastro do objeto
    janela.fill((0, 0, 0))
    # Define o objeto que irá aparecer e a posição
    janela.blit(fundo, (0, 30))
    # # Imagens dos carros na posição x, y
    janela.blit(branco, (branco.pos_pista('a'), branco.pos_y))

    pygame.display.update()


# Sai do programa
pygame.quit()
