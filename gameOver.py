import pygame

def gameOver(score1, score2):
    # Constants
    WIDTH = 1536
    HEIGHT = 793

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
    font = pygame.font.SysFont(None, 80)

    screen.fill((255,255,255))
    
    text = font.render("Game Over", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 200))
    screen.blit(text, text_rect)
    
    text = font.render(f'Player 1 score: {score1}', True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2 - 300, HEIGHT / 2 - 100))
    screen.blit(text, text_rect)
    
    text = font.render(f'Player 2 score: {score2}', True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2 + 300, HEIGHT / 2 - 100))
    screen.blit(text, text_rect)

    winner = 0
    if score1 > score2:
        winner = 1
    elif score2 > score1:
        winner = 2
    if winner != 0:
        win = font.render("Player "+str(winner) + ' won!', True, (0, 0, 0))
    else:
        win = font.render('It is draw! ', True, (0, 0, 0))
    win_rect = win.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(win, win_rect)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

# gameOver(12,14)