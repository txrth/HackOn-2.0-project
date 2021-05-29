import pygame

class Credits:
    def __init__(self):
        print("p")
        pygame.init()

        X = 450
        Y = 700

        background = (0, 153, 143)
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Front-End')

        game_font = pygame.font.Font('junegull.ttf', 100)
        game1_text = game_font.render('CREDITS', True, (255, 255, 255))
        game1_rect = game1_text.get_rect()
        game1_rect.center = (X//2, Y//5)

        game_font = pygame.font.Font('junegull.ttf', 25)
        first1_text = game_font.render('ARJUN', True, (255, 255, 255))
        first1_rect = first1_text.get_rect()
        first1_rect.center = (125, 300)
        last1_text = game_font.render('MUDHAR', True, (255, 255, 255))
        last1_rect = last1_text.get_rect()
        last1_rect.center = (125, 350)

        game_font = pygame.font.Font('junegull.ttf', 25)
        first2_text = game_font.render('DHRUV', True, (255, 255, 255))
        first2_rect = first2_text.get_rect()
        first2_rect.center = (325, 300)
        last2_text = game_font.render('PATEL', True, (255, 255, 255))
        last2_rect = last2_text.get_rect()
        last2_rect.center = (325, 350)

        game_font = pygame.font.Font('junegull.ttf', 25)
        first3_text = game_font.render('KHUSHI', True, (255, 255, 255))
        first3_rect = first3_text.get_rect()
        first3_rect.center = (125, 500)
        last3_text = game_font.render('PATEL', True, (255, 255, 255))
        last3_rect = last3_text.get_rect()
        last3_rect.center = (125, 550)

        game_font = pygame.font.Font('junegull.ttf', 25)
        first4_text = game_font.render('TIRTH', True, (255, 255, 255))
        first4_rect = first4_text.get_rect()
        first4_rect.center = (325, 500)
        last4_text = game_font.render('PATEL', True, (255, 255, 255))
        last4_rect = last4_text.get_rect()
        last4_rect.center = (325, 550)

        exit_button = pygame.image.load("exit.png").convert()
        settings_button = pygame.image.load("settings.png").convert()

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
                        return

            mouse = pygame.mouse.get_pos()

            pygame.draw.rect(display_surface, (21, 81, 81), [50, 250, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [50, 450, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [250, 250, 150, 150])
            pygame.draw.rect(display_surface, (21, 81, 81), [250, 450, 150, 150])

            display_surface.blit(game1_text, game1_rect)
            display_surface.blit(first1_text, first1_rect)
            display_surface.blit(last1_text, last1_rect)
            display_surface.blit(first2_text, first2_rect)
            display_surface.blit(last2_text, last2_rect)
            display_surface.blit(first3_text, first3_rect)
            display_surface.blit(last3_text, last3_rect)
            display_surface.blit(first4_text, first4_rect)
            display_surface.blit(last4_text, last4_rect)

            display_surface.blit(exit_button, (X - exit_button.get_width(), 0))
            display_surface.blit(settings_button, (0, 0))

            pygame.display.update()