import datetime
import threading
import time
import pygame
import FrontEnd.Display.credits as credits
import FrontEnd.Display.breaks as breaks
import points


class Work:
    def __init__(self):
        print("hello")
        pygame.init()

        X = 450
        Y = 700
        global current
        current = datetime.datetime.now()
        stopwatch = False
        stopwatch_on = False
        paused = False
        self.counter = 0

        background = (0, 153, 143)
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Front-End')

        app_name_font = pygame.font.Font('./junegull.ttf', 50)
        app_name1 = app_name_font.render('START', True, (255, 255, 255))
        app_name_rect1 = app_name1.get_rect()
        app_name_rect1.center = (X // 4, Y // 2)

        app_name2 = app_name_font.render('STOP', True, (255, 255, 255))
        app_name_rect2 = app_name2.get_rect()
        app_name_rect2.center = (X // 4 + X // 2, Y // 2)

        app_name3 = app_name_font.render('PAUSE', True, (255, 255, 255))
        app_name_rect3 = app_name3.get_rect()
        app_name_rect3.center = (X // 2, Y // 3 + Y // 3)

        app_name4 = app_name_font.render('BREAK', True, (255, 255, 255))
        app_name_rect4 = app_name4.get_rect()
        app_name_rect4.center = (X // 2, Y // 3 + 350)

        point_font = pygame.font.Font('./junegull.ttf', 100)
        timing = str(datetime.datetime.now() - current)
        timing = timing[0:timing.index(".")]
        point_text = point_font.render(str(timing), True, (255, 255, 255))
        point_rect = point_text.get_rect()
        point_rect.center = (X // 2, Y // 5)

        exit_button = pygame.image.load("./exit.png").convert()
        settings_button = pygame.image.load("./settings.png").convert()

        # infinite loop
        while True:

            def thread_f():
                while (stopwatch == True):
                    print(str(datetime.datetime.now() - current))
                    display_surface.fill(background)

                    display_surface.blit(app_name1, app_name_rect1)
                    display_surface.blit(app_name2, app_name_rect2)
                    display_surface.blit(app_name3, app_name_rect3)
                    display_surface.blit(app_name4, app_name_rect4)

                    timing = str(datetime.datetime.now() - current)
                    timing = timing[0:timing.index(".")]
                    point_text = point_font.render(str(timing), True, (255, 255, 255))
                    display_surface.blit(exit_button, (X - exit_button.get_width(), 0))
                    display_surface.blit(settings_button, (0, 0))
                    display_surface.blit(point_text, (X / 2 - point_text.get_width() / 2, Y / 4))

                    self.counter += 1

                    pygame.display.update()
                    time.sleep(1)

            if (not stopwatch_on):
                display_surface.fill(background)

                display_surface.blit(app_name1, app_name_rect1)
                display_surface.blit(app_name2, app_name_rect2)
                display_surface.blit(app_name3, app_name_rect3)
                display_surface.blit(app_name4, app_name_rect4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # deactivates the pygame library
                    pygame.quit()

                    # quit the program
                    quit()


                # checks if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if X - 50 <= mouse[0] <= X and 0 <= mouse[1] <= 50:
                        print("exit")
                        return
                    elif 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                        print("settings")
                        credits.Credits()
                    elif X // 4 - app_name1.get_width() / 2 <= mouse[0] <= X // 4 + app_name1.get_width() / 2 and \
                            Y // 2 - app_name1.get_height() / 2 <= mouse[1] <= Y // 2 + app_name1.get_height() / 2:
                        print("start")
                        stopwatch = True
                        stopwatch_on = True
                        if (not paused):
                            current = datetime.datetime.now()
                            paused = False
                        x = threading.Thread(target=thread_f)

                        x.start()

                    elif X / 4 + X / 2 - app_name2.get_width() / 2 <= mouse[
                        0] <= X / 4 + X / 2 + app_name2.get_width() / 2 and Y / 2 - app_name2.get_height() / 2 <= mouse[
                        1] <= Y / 2 + app_name2.get_height() / 2:
                        print("stop")
                        stopwatch = False
                        paused = False

                        current_points = 0
                        with open("./point_counter.txt", "r") as point_file:
                            current_points = int(point_file.readline().strip())

                        with open("./point_counter.txt", "w") as point_file:
                            point_file.write(str(current_points + self.counter))

                    elif X // 2 - app_name3.get_width() / 2 <= mouse[0] <= X // 2 + app_name3.get_width() / 2 and \
                            Y // 3 + Y // 3 - app_name3.get_height() / 2 <= mouse[
                            1] <= Y // 3 + Y // 3 + app_name3.get_height() / 2:
                        print("continue")
                        stopwatch = False
                        paused = True
                        x = threading.Thread(target=thread_f)
                        x.start()

                    elif X // 2 - app_name4.get_width() / 2 <= mouse[0] <= X // 2 + app_name4.get_width() / 2 and \
                            Y // 3 + 350 - app_name4.get_height() / 2 <= mouse[
                            1] <= Y // 3 + 350 + app_name4.get_height() / 2:
                        print("settings")
                        if (not paused):
                            paused = True
                            stopwatch = False
                        breaks.Breaks()


            mouse = pygame.mouse.get_pos()
            if (not stopwatch_on):
                display_surface.blit(exit_button, (X - exit_button.get_width(), 0))
                display_surface.blit(settings_button, (0, 0))
                display_surface.blit(point_text, (X / 2 - point_text.get_width() / 2, Y / 4))

                pygame.display.update()