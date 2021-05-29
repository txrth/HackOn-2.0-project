import pygame
import reward
import credits

class Points:
    def __init__(self):
        print("p")
        pygame.init()

        X = 450
        Y = 700

        background = (0, 153, 143)
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Front-End')

        point_font = pygame.font.Font('junegull.ttf', 75)
        point_text = point_font.render('Points', True, (255, 255, 255))
        point_rect = point_text.get_rect()
        point_rect.center = (X // 2, Y // 5)

        point_count_font = pygame.font.Font('junegull.ttf', 110)
        point_count_text = point_count_font.render('000000', True, (255, 255, 255))
        point_count_rect = point_count_text.get_rect()
        point_count_rect.center = (X // 2, Y // 5 + 200)

        app_name_font = pygame.font.Font('junegull.ttf', 50)
        app_name1 = app_name_font.render('Rewards', True, (255, 255, 255))
        app_name_rect1 = app_name1.get_rect()
        app_name_rect1.center = (X // 2, Y - 200)

        exit_button = pygame.image.load("exit.png").convert()
        settings_button = pygame.image.load("settings.png").convert()

        # infinite loop
        while True:
            display_surface.fill(background)
            display_surface.blit(point_text, point_rect)
            display_surface.blit(point_count_text, point_count_rect)
            display_surface.blit(app_name1, app_name_rect1)

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
                    elif X//2 - app_name1.get_width()/2 <= mouse[0] <= X//2 + app_name1.get_width()/2 and Y-200 - app_name1.get_height()/2 <= mouse[1] <= Y - 200 + app_name1.get_height()/2:
                        print("settings")
                        reward.Reward()


            mouse = pygame.mouse.get_pos()

            display_surface.blit(exit_button, (X - exit_button.get_width(), 0))
            display_surface.blit(settings_button, (0, 0))

            pygame.display.update()
