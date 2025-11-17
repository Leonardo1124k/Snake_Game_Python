#COMENTARIOS SOBRE COMO ESTRUTURAR UM PROJETO DE JOGO
#1 - CONFIGURACOES INICIAIS
import pygame
import random

pygame.init() # sempre necessario para inicializar a biblioteca pygame
pygame.display.set_caption("Snake Game - Python") # Define nome da janela no computador
largura = 900
altura = 600
tela = pygame.display.set_mode((largura, altura)) #Estabelece as dimensoes
relogio = pygame.time.Clock()

#cores em RGB (pygame usa apenas nesse formato)
black = (0,0,0) # fundo
white = (255, 255, 255) # snake
darkred = (139, 0, 0) # pontuacao
green = (0,128,0) # comida

# parametros da snake
tamanho_quadrado = 15 # em px,quadrado que ficará visível a snake
velocidade_jogo = 10

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado)/ float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    # codigo abaixo seria para gerar comida em posições que não
    # estivessem, necessariamente, alinhados com a linha e coluna que a cobrinha está trilhando
    # comida_x = random.randrange(0, largura - tamanho_quadrado)
    # comida_y = random.randrange(0, altura - tamanho_quadrado)
    # Foi resolvido para tudo que for gerado estar alinhado em quadradinhos e não tornar complexo
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, green, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, white, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Roboto", 30)
    texto = fonte.render(f"Pontos: {pontuacao}", True, darkred)
    tela.blit(texto, [2,2])

#VELOCIDADE = DESLOCAMENTO (na verdade)
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura/2 # x e y definem onde a snake comeca no jogo
    y = largura/2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = list()

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(black)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        #desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        if x < 0 or x>= largura or y < 0 or y >= altura:
            fim_jogo = True

        #atualizar a posicao da cobra
        x += velocidade_x
        y += velocidade_y

        #desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

#se a cobrinha bateu no proprio corpo (exceto a cabeça com cabeça)
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)
        #desenhar_pontos

        #atualizacao da tela
        pygame.display.update()

        #criar uma nova comida (se ela já comeu)
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        relogio.tick(velocidade_jogo)



#2 - CRIAR LOOP INFINITO
#Pontuacao
#Cobrinha (player)
#Comida (alvo/objetivo)
#3 - DESENHAR OS OBJETOS DO JOGO NA TELA

#4 - CRIAR A LOGICA DE TERMINAR O JOGO

#5 - CAPTURAR INTERAÇÕES DO USUÁRIO (TECLAS...)

rodar_jogo()