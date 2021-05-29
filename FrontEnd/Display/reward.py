import pygame
import FrontEnd.Display.credits as credits

class Reward:
    def __init__(self):
        print("p")
        pygame.init()

        X = 450
        Y = 700

        background = (0, 153, 143)
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Front-End')

        game_font = pygame.font.Font('FrontEnd/Display/junegull.ttf', 25)
        game1_text = game_font.render('HANGMAN', True, (255, 255, 255))
        game1_rect = game1_text.get_rect()
        game1_rect.center = (125, 125)

        game2_text = game_font.render('SPACE INVADERS', True, (255, 255, 255))
        game2_rect = game2_text.get_rect()
        game2_rect.center = (325, 125)

        game3_text = game_font.render('MEMES GALORE', True, (255, 255, 255))
        game3_rect = game3_text.get_rect()
        game3_rect.center = (125, 325)

        exit_button = pygame.image.load("FrontEnd/Display/exit.png").convert()
        settings_button = pygame.image.load("FrontEnd/Display/settings.png").convert()

        # infinite loop
        while True:
            display_surface.fill(background)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # deactivates the pygame library
                    pygame.quit()

                    # quit the program.
                    quit()

                # checks if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if X - 50 <= mouse[0] <= X and 0 <= mouse[1] <= 50:
                        print("exit")
                        return
                    elif 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                        print("settings")
                        credits.Credits()

            mouse = pygame.mouse.get_pos()

            pygame.draw.rect(display_surface, (21, 81, 81), [50, 50, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [50, 250, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [50, 450, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [250, 50, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [250, 250, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [250, 450, 150, 150])

            display_surface.blit(game1_text, game1_rect)
            display_surface.blit(game2_text, game2_rect)
            display_surface.blit(game3_text, game3_rect)

            display_surface.blit(exit_button, (X - exit_button.get_width(), 0))
            display_surface.blit(settings_button, (0, 0))

            pygame.display.update()