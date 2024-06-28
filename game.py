import pygame
import random
import os

# Inicializar o pygame
pygame.init()

# Definir as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definir o tamanho da tela
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir o título da janela
pygame.display.set_caption("Jogo da Cobrinha")

# Definir a velocidade do jogo
clock = pygame.time.Clock()
speed = 10

# Definir a posição inicial da cobrinha
snake_x = 300
snake_y = 200
snake_size = 10
snake = pygame.Rect(snake_x, snake_y, snake_size, snake_size)

# Definir a direção inicial da cobrinha
direction = "right"

# Definir a posição inicial da comida
food_x = 100
food_y = 100
food_size = 10
food = pygame.Rect(food_x, food_y, food_size, food_size)

# Definir a pontuação inicial
score = 0

# Definir a variável de controle do loop principal
done = False

# Adicionar uma variável para controlar se o jogo foi ganho
game_won = False

# Loop principal do jogo
while not done:
    # Processar os eventos
    for event in pygame.event.get():
        # Se o usuário clicar no botão de fechar
        if event.type == pygame.QUIT:
            # Sair do jogo
            done = True
        # Se o usuário pressionar uma tecla
        elif event.type == pygame.KEYDOWN:
            # Se a tecla for a seta para cima
            if event.key == pygame.K_UP:
                # Mudar a direção da cobrinha para cima
                direction = "up"
            # Se a tecla for a seta para baixo
            elif event.key == pygame.K_DOWN:
                # Mudar a direção da cobrinha para baixo
                direction = "down"
            # Se a tecla for a seta para esquerda
            elif event.key == pygame.K_LEFT:
                # Mudar a direção da cobrinha para esquerda
                direction = "left"
            # Se a tecla for a seta para direita
            elif event.key == pygame.K_RIGHT:
                # Mudar a direção da cobrinha para direita
                direction = "right"

    # Atualizar a posição da cobrinha de acordo com a direção
    if direction == "up":
        snake_y -= snake_size
    elif direction == "down":
        snake_y += snake_size
    elif direction == "left":
        snake_x -= snake_size
    elif direction == "right":
        snake_x += snake_size

    # Verificar se a cobrinha saiu da tela
    if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
        # Sair do jogo
        done = True

    # Atualizar o retângulo da cobrinha
    snake = pygame.Rect(snake_x, snake_y, snake_size, snake_size)

    # Verificar se a cobrinha comeu a comida
    if snake.colliderect(food):
        # Aumentar a pontuação
        score += 1
        # Gerar uma nova posição para a comida
        food_x = snake_size * (random.randint(0, screen_width // snake_size - 1))
        food_y = snake_size * (random.randint(0, screen_height // snake_size - 1))
        # Atualizar o retângulo da comida
        food = pygame.Rect(food_x, food_y, food_size, food_size)

    # Se o jogo foi ganho, reproduzir um vídeo
    if score >= 10 and not game_won:
        game_won = True
        # Preencher a tela com a cor preta
        screen.fill(BLACK)

        # Carregar e reproduzir o vídeo
        video_path = os.path.join(os.path.dirname(__file__), "susto.mp4")
        video = pygame.movie.Movie(video_path)
        video_screen = pygame.Surface(video.get_size()).convert()
        video.set_display(video_screen)
        video.play()

        # Atualizar a tela
        pygame.display.flip()

        # Aguardar até que o vídeo termine
        while video.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    break

        # Encerrar o jogo
        done = True

    # Preencher a tela com a cor preta
    screen.fill(BLACK)

    # Desenhar a cobrinha na tela com a cor verde
    pygame.draw.rect(screen, GREEN, snake)

    # Desenhar a comida na tela com a cor vermelha
    pygame.draw.rect(screen, RED, food)

    # Mostrar a pontuação na tela com a cor branca
    font = pygame.font.SysFont("Arial", 32)
    text = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a velocidade do jogo
    clock.tick(speed)

# Finalizar o pygame
pygame.quit()
