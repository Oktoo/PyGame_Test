from Fight_Entities import *
from Button import button
from AI import *
import sys



tury_licznik = 0
start = 1
colision = 0
celX = 32
celY = 32
licznik_E = 0
licznik_P = 0
Y = -100
flag_tura = True
Tura_Nr = 0

def main_game():
    global Fight_End
    global tury_licznik, licznik_E, licznik_P, Tura_Licznik, flag_tura, Tura_Nr
    global YourTurn
    global start
    global colision
    global celX, celY
    global draw_in_order_F, Y
    display.fill((24, 164, 86))
    UpButton = button((0, 255, 0), 700, 500, 32, 32)
    DownButton = button((0, 0, 255), 700, 536, 32, 32)
    RightButton = button((255, 0, 0), 736, 518, 32, 32)
    LeftButton = button((0, 0, 0), 664, 518, 32, 32)
    DmgButton = button((200, 0, 55), 506, 518, 48, 32)
    EndButton = button((200, 25, 40), 576, 518, 64, 32)
    player = Player_Fight(32 * 12, 32 * 10, 32, 48, "Okto1", gracz)
    player1 = Player_Fight(32 * 10, 32 * 10, 32, 52, "Okto2", gracz1)
    UpButton.draw(display)
    DownButton.draw(display)
    RightButton.draw(display)
    LeftButton.draw(display)
    DmgButton.draw(display)
    EndButton.draw(display)

    cel = Cel(celX, celY, znak)
    cel.main(display)

    if start == 1:
        print("START!")
        enemies.clear()
        walls.clear()
        players.clear()
        enemies.append(Enemy_Fight(32 * 14, 32 * 6, 32, 48, npc, "Zły Łowca"))
        enemies.append(Enemy_Fight(32 * 12, 32 * 6, 32, 48, npc, "Bardzo Zły Łowca"))
        walls.append(Wall_Fight(32 * 10, 32 * 4, 32, 32))
        players.append(player)
        players.append(player1)

        for i in range(25):
            walls.append(Wall_Fight(32 * i, 32 * 0, 32, 32))
            walls.append(Wall_Fight(32 * i, 32 * 18, 32, 32))

        for i in range(17):
            walls.append(Wall_Fight(32 * 0, 32 * (i + 1) , 32, 32))
            walls.append(Wall_Fight(32 * 24, 32 * (i + 1), 32, 32))

        for i in players:
            i.tura = tury_licznik
            kolejka.append(i)
            tury_licznik += 1
        for i in enemies:
            i.tura = tury_licznik
            kolejka.append(i)
            tury_licznik += 1

        start = 0

    draw_in_order_F.clear()

    for i in enemies:
        draw_in_order_F.append(i)
    for i in walls:
        draw_in_order_F.append(i)
    for i in players:
        draw_in_order_F.append(i)


    Draw_List_F.clear()
    while Y <= OknoY:
        for i in draw_in_order_F:
            if i == players[0] and Y == i.y - P_scroll[1]:
                Draw_List_F.append(i)

            elif Y == i.y - i.pos[1] and i != players[0]:
                Draw_List_F.append(i)
        Y += 1


    x = 0
    for i in Draw_List_F:
        i.main(display)
        x += 1

    Y = -100


    for i in enemies:
        if i.health <= 0:
            i.alive = False
            kolejka.remove(i)
            enemies.remove(i)
            print(len(kolejka))
    if len(enemies) <= 0:
        Fight_End = True

    for i in players:
        if len(players) > 1:
            if i.health <= 0:
                i.alive = False
                kolejka.remove(i)
                players.remove(i)
                print(len(kolejka))
        elif i.health <= 0:
            print("PRZEGRAŁEŚ...")
            Fight_End = True

    if Fight_End == True:
        print("YYY")
        start = 1
        tury_licznik = 0
        licznik_E = 0
        licznik_P = 0
        Tura_Nr = 0
        colision = 0
        players.clear()
        enemies.clear()
        walls.clear()
        time.sleep(2)
        Fight_End = False
        return True

#Zarządzanie kolejką walki! #Licznik_E liczy miejsce enemy w liście Enemies, Tura_Licznik odpowiada za nr entity w turze
    while licznik_P >= len(players):
        licznik_P -= 1
    if flag_tura:
        for i in kolejka:
            if i.tura == Tura_Licznik and i.type == "enemy":
                Tura_Nr += 1
                napis = "[" + str(Tura_Nr) + "]"
                print(napis, "Tura", i.name)
                for E in enemies:
                    if E.tura == Tura_Licznik:
                        MakeTurn(licznik_E)
                    licznik_E += 1
                Tura_Licznik += 1
            elif i.tura == Tura_Licznik and i.type == "player":
                Tura_Nr += 1
                napis = "[" + str(Tura_Nr) + "]"
                print(napis, "Tura", i.name)
                for P in players:
                    if P.tura == Tura_Licznik:
                        flag_tura = False
                        break
                    licznik_P += 1

            licznik_E = 0

        Tura_Licznik += 1


        if Tura_Licznik >= len(kolejka):
            Tura_Licznik = 0
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            #print(kolejka)
            #print("Tura", player.name, player.tura)



    player = players[0]

    pygame.display.update()



#Zarządzanie ruchami gracza!

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if UpButton.isOver(pos):
                for i in walls:
                    if i.y == player.y - 32 - P_scroll[1] + (player.height - 32) and i.x == player.x + P_scroll[0]:
                        colision = 1
                if colision == 0 and players[licznik_P].move >= 1:
                    players[licznik_P].pos[1] -= 32
                    players[licznik_P].move -= 1
                    players[licznik_P].yy -= 1
                else:
                    colision = 0
            if DownButton.isOver(pos):
                for i in walls:
                    if i.y == player.y + 32 - P_scroll[1] + (player.height - 32) and i.x == player.x + P_scroll[0]:
                        colision = 1
                if colision == 0 and players[licznik_P].move >= 1:
                    players[licznik_P].pos[1] += 32
                    players[licznik_P].move -= 1
                    players[licznik_P].yy += 1
                else:
                    colision = 0
            if RightButton.isOver(pos):
                for i in walls:
                    if i.x == player.x + 32 + P_scroll[0] and i.y == player.y - P_scroll[1]:
                        colision = 1
                if colision == 0 and players[licznik_P].move >= 1:
                    players[licznik_P].pos[0] += 32
                    players[licznik_P].move -= 1
                    players[licznik_P].xx += 1
                else:
                    colision = 0
            if LeftButton.isOver(pos):
                for i in walls:
                    if i.x == player.x - 32 + P_scroll[0] and i.y == player.y - P_scroll[1]:
                        colision = 1
                if colision == 0 and players[licznik_P].move >= 1:
                    players[licznik_P].pos[0] -= 32
                    players[licznik_P].move -= 1
                    players[licznik_P].xx -= 1
                else:
                    colision = 0
            #print(player.xx, player.yy)

            if DmgButton.isOver(pos):
                if flag_tura == False:
                    for i in enemies:
                        print(i.name, i.health)
                        i.health -= player.attack
                        print(i.name, i.health)

            if EndButton.isOver(pos):
                if flag_tura == False:
                    players[licznik_P].move = players[licznik_P].maxmove
                    licznik_P = 0
                    flag_tura = True
                    print("Zakończono Turę")


def Redraw_Window():
    display.fill((24, 164, 86))
    pygame.display.update()