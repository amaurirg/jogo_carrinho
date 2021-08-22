import pygame
from random import randint


# Inicia o pygame
pygame.init()

# Eixo x
x = 360     # max 690, min 20
# Eixo y
y = 100
pos_x = 126
pos_y = 800
pos_y_a = 800
pos_y_c = 800
# Velocidade em pixel para mover o objeto
velocidade = 10
velocidade_outros = 12
# Images de fundo e carros
fundo = pygame.image.load('./images/pista6.jpeg')
carro_jogador = pygame.image.load('./images/carro_amarelo_jogador2.png')
carro_ambulancia = pygame.image.load('./images/carro_ambulancia2.png')
carro_policia = pygame.image.load('./images/carro_policia2.png')
carro_branco = pygame.image.load('./images/carro_branco2.png')
carro_cinza = pygame.image.load('./images/carro_cinza2.png')
carro_vermelho = pygame.image.load('./images/carro_vermelho2.png')

# Define o tamanho da janela
janela = pygame.display.set_mode((800, 600))
# Nome que aparece no cabeçalho da janela
pygame.display.set_caption("Criando um jogo com Python")
# Para fazer o loop mantendo a janela aberta
janela_aberta = True

# Contador de tempo
timer = 0
tempo_segundo = 0

# Fontes
# Fonte utilizada
font = pygame.font.SysFont('arial black', 30)
# Texto Tempo. True ou False não mudou.
# Cor da fonte. Cor do fundo
texto = font.render(f"Tempo: {timer}", True, (255, 255, 255), (0, 0, 0))
# Retângulo que fica atrás do texto
pos_texto = texto.get_rect()
# Posição no canto da tela
pos_texto.center = (50, 16)



while janela_aberta:
    # Delay para atualizar a tela
    pygame.time.delay(50)
    # Para cada evento
    for event in pygame.event.get():
        # Se o evento for QUIT fecha a janela
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Quando for pressionada uma tecla
    comandos = pygame.key.get_pressed()
    # Comentado porque o carro só se movimenta para o lado
    # if comandos[pygame.K_UP]:
    #     y -= velocidade
    # if comandos[pygame.K_DOWN]:
    #     y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 689:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 23:
        x -= velocidade

    if (pos_y <= -180) and (pos_y_a <= -180) and (pos_y_c <= -180):
        pos_y = randint(800, 2000)
        pos_y_a = randint(800, 2000)
        pos_y_c = randint(800, 2000)

    # Devido ao delay de 50ms do while. 20*50 = 1000ms = 1 segundo
    if timer < 20:
        timer += 1
    # Após 1 segundo, incrementa o tempo em segundos
    # Zera o timer para começar o novo tempo em segundos
    else:
        tempo_segundo += 1
        texto = font.render(f"Tempo: {str(tempo_segundo)}", True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_c -= velocidade_outros + 10

    # Atualiza a tela para limpar o rastro do objeto
    janela.fill((0, 0, 0))
    # Define o objeto que irá aparecer e a posição
    janela.blit(fundo, (0, 30))
    # Imagens dos carros na posição x, y
    janela.blit(carro_jogador, (x, y))
    janela.blit(carro_policia, (pos_x, pos_y))
    janela.blit(carro_ambulancia, (pos_x + 515, pos_y - 270))
    janela.blit(carro_vermelho, (pos_x, pos_y - 260))
    janela.blit(carro_cinza, (pos_x + 215, pos_y))
    # janela.blit(carro_branco, (x, pos_y))
    janela.blit(texto, pos_texto)

    # Cria um círculo (RGB), a posição na tela (400,300) e o raio do círculo em pixels
    # pygame.draw.circle(janela, (0, 255, 0), (x, y), 50)

    # Atualiza a tela
    pygame.display.update()


# Sai do programa
pygame.quit()
