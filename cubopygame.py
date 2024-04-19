import pygame
import sys

# Definir as dimensões da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desenhar Cubo")

# Definir cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
verde = (37, 247, 131)

# Coordenadas iniciais dos vértices do cubo
vertices = [
    (200, 200), (400, 200), (400, 400), (200, 400),  # Face frontal
    (250, 150), (450, 150), (450, 350), (250, 350),  # Face traseira
    (250, 200), (400, 350)  # Coordenadas usadas para preencher face superior e lateral
]

# Linhas que compõem as arestas do cubo
linhas = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # Face frontal
    [4, 5], [5, 6], [9, 7], [7, 8],  # Face traseira
    [0, 4], [1, 5], [2, 6], [3, 7],   # Conexões entre as faces
]

# Função para desenhar o cubo
def desenhar_cubo():
    # Colorir o cubo
    pygame.draw.polygon(tela, azul, [vertices[i] for i in [0, 4, 5, 1]], 0)  # Face superior
    pygame.draw.polygon(tela, verde, [vertices[i] for i in [0, 1, 2, 3]], 0)  # Face frontal
    pygame.draw.polygon(tela, preto, [vertices[i] for i in [2, 6, 5, 1]], 0)  # Face lateral

    # Desenhar as linhas do cubo
    for linha in linhas:
        pygame.draw.line(tela, preto, vertices[linha[0]], vertices[linha[1]], 4)

# Função para mover o cubo de posição
def atualizar_posicao(teclas):
    velocidade = 1
    if teclas[pygame.K_w]:
        for i in range(len(vertices)):
            vertices[i] = (vertices[i][0], vertices[i][1] - velocidade)
    if teclas[pygame.K_s]:
        for i in range(len(vertices)):
            vertices[i] = (vertices[i][0], vertices[i][1] + velocidade)
    if teclas[pygame.K_a]:
        for i in range(len(vertices)):
            vertices[i] = (vertices[i][0] - velocidade, vertices[i][1])
    if teclas[pygame.K_d]:
        for i in range(len(vertices)):
            vertices[i] = (vertices[i][0] + velocidade, vertices[i][1])

# Loop principal do jogo
def principal():
    while True:
        tela.fill(branco)  # Preencher a tela com branco

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        atualizar_posicao(teclas)  # Atualizar a posição do cubo usando WASD
        desenhar_cubo()  # Desenhar o cubo

        pygame.display.flip()  # Atualizar a tela

if __name__ == "__main__":
    pygame.init()
    principal()
