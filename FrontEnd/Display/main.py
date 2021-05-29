import pygame
import FrontEnd.Display.todolist as todolist
import FrontEnd.Display.work as work
import FrontEnd.Display.points as points
import FrontEnd.Display.credits as credits

pygame.init()

X = 450
Y = 700

background = (0, 153, 143)
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Taskily')

app_name_font = pygame.font.Font("FrontEnd/Display/junegull.ttf", 100)
app_name1 = app_name_font.render('SMART', True, (255, 255, 255))
app_name_rect1 = app_name1.get_rect()
app_name_rect1.center = (X // 2, Y // 5)

app_name2 = app_name_font.render('WORKS', True, (255, 255, 255))
app_name_rect2 = app_name2.get_rect()
app_name_rect2.center = (X // 2, Y // 5 + 75)

button_font = pygame.font.Font("FrontEnd/Display/junegull.ttf", 40)
to_do_button_text = button_font.render('View My Tasks', True, (255, 255, 255))
work_button_text = button_font.render('Start My Work Session', True, (255, 255, 255))
points_button_text = button_font.render('View My Points', True, (255, 255, 255))

exit_button = pygame.image.load("FrontEnd/Display/exit.png").convert()
settings_button = pygame.image.load("FrontEnd/Display/settings.png").convert()

# infinite loop
while True:
    display_surface.fill(background)

    display_surface.blit(app_name1, app_name_rect1)
    display_surface.blit(app_name2, app_name_rect2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            if X / 2 - 180 <= mouse[0] <= X / 2 + 180 and Y / 2 <= mouse[1] < Y / 2 + 60:
                print ("list")
                todolist.ToDoList()
            elif X / 2 - 180 <= mouse[0] <= X / 2 + 180 and Y / 2 + 60 <= mouse[1] < Y / 2 + 150:
                print ("work")
                work.Work()
            elif X / 2 - 220 <= mouse[0] <= X / 2 + 220 and Y / 2 + 150 <= mouse[1] <= Y / 2 + 240:
                print ("points")
                points.Points()
            elif X - 50 <= mouse[0] <= X and 0 <= mouse[1] <= 50:
                print ("exit")
                pygame.quit()
            elif 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                print("settings")
                credits.Credits()


    mouse = pygame.mouse.get_pos()

    display_surface.blit(to_do_button_text, (X / 2 - to_do_button_text.get_width()/2, Y / 2 + 30))
    display_surface.blit(work_button_text, (X / 2 - work_button_text.get_width()/2, Y / 2 + 100))
    display_surface.blit(points_button_text, (X / 2 - points_button_text.get_width()/2, Y / 2 + 170))
    display_surface.blit(exit_button, (X - exit_button.get_width(), 0))
    display_surface.blit(settings_button, (0, 0))

    pygame.display.update()