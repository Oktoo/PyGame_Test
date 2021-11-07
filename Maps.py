from Player import Player
from Enemy import Enemy
from Fight import *

TEST = False
wysokosc = 0
x = 0
Walka = True
class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        global draw_in_order, Draw_List, wysokosc, x
        global StartRender
        global Walka
        display.fill((24, 164, 255))
        player = Player(400, 100, 32, 32)
        enemy = Enemy(100, 200, 32, 32)
        enemy1 = Enemy(300, 220, 32, 32)
        enemy2 = Enemy(250, 300, 32, 32)
        enemy3 = Enemy(250, 320, 32, 32)

        draw_in_order.clear()
        draw_in_order.append(player)
        draw_in_order.append(enemy)
        draw_in_order.append(enemy1)
        draw_in_order.append(enemy2)
        draw_in_order.append(enemy3)




        Draw_List.clear()
        while wysokosc <= OknoY:
            for i in draw_in_order:
                if i == player and wysokosc == i.y :
                    Draw_List.append(i)


                elif wysokosc == i.y - display_scroll[1]:
                    Draw_List.append(i)
                    """if i == player:
                        print(i)
"""
            wysokosc += 1
        x = 0
        for i in Draw_List:
            i.main(display)
            x += 1
            """enemy.main(display)
            player.main(display)"""




        pygame.display.update()

        wysokosc = 0


        if Walka and enemy.x - display_scroll[0] - 32 <= player.x <= enemy.x - display_scroll[0] + 32 and enemy.y - display_scroll[1] - 32 <= player.y <= enemy.y - display_scroll[1] + 32:
            print("KOLIZJA!")
            self.state = 'main_game'
            Walka = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.state = 'main_game'



    def state_manager(self):
        global TEST

        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            TEST = main_game()
        if TEST == True and self.state == 'main_game':
            self.state = 'intro'


