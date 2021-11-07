from settings import *

def MakeTurn(enemy):
    global YourTurn
    i = enemies[enemy]



    def CanAttack():
        for x in players:
            #print(i.xx, i.yy, x.name, x.xx, x.yy)
            if x.xx + 1 == i.xx and x.yy == i.yy or x.xx - 1 == i.xx and x.yy == i.yy or x.yy + 1 == i.yy and x.xx == i.xx or x.yy - 1 == i.yy and x.xx == i.xx:
                if i.energy > 0:
                    while i.energy > 0:
                        x.health -= i.attack
                        print(i.name, "zaatakował", x.name, "zadając", i.attack, "obrażeń, pozostało", x.health, "punktów zycia", x.name)
                        i.energy -= 1
                    return True
                else:
                    return False
        return False

    def MakeMove():
        range_list = []
        ListNr = 0
        for x in players:
            x_diff = i.xx - x.xx
            y_diff = i.yy - x.yy

            if x_diff < 0:
                x_diff *= -1
            if y_diff < 0:
                y_diff *= -1
            sum_diff = x_diff + y_diff
            PlayerPos = [int(sum_diff), ListNr]
            range_list.append(PlayerPos)
            ListNr += 1


        for y in range(100):
            Licznik = 0
            for z in range_list:
                if z[0] == y:
                    print(i.name, "podchodzi do", players[z[1]].name)
                    return Licznik
                else:
                    Licznik += 1
        return -1


    DMG = CanAttack()
    if DMG == False and i.energy > 0:
        direction = MakeMove()
        if direction == -1:
            print("FALSE")
            return
        else:
            print(i.xx, i.yy, players[direction].xx, players[direction].yy)
            x_dir = "None"
            y_dir = "None"
            x = i.xx - players[direction].xx
            y = i.yy - players[direction].yy
            print(x, y)

            if x < 0.0:
                x *= -1
                x_dir = "R"
            elif x > 0.0:
                x_dir = "L"

            if y < 0.0:
                y *= -1
                y_dir = "D"
            elif y > 0.0:
                y_dir = "U"

            if x == 1 and y == 1:
                print("Korekta Y")
                y_dir = "None"
            elif x == 1 and y > 1:
                print("Korekta X")
                x_dir = "None"
            elif y == 1 and x > 1:
                print("Korekta Y")
                y_dir = "None"

            print(x, y, x_dir, y_dir)


            #print(x, y)

    i.energy = i.maxenergy
    i.move = i.maxmove