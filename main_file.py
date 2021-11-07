from Maps import *

pygame.init()
clock = pygame.time.Clock()
game_state = GameState()


while True:
    global Map_Id
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        display_scroll[0] -= 5
    if keys[pygame.K_d]:
        display_scroll[0] += 5
    if keys[pygame.K_w]:
        display_scroll[1] -= 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        display_scroll[0] -= display_scroll[0]
        display_scroll[1] -= display_scroll[1]

    if Map_Id == 'main_game':
        print("XD")
        Redraw_Window()

    #print(display_scroll)
    game_state.state_manager()
    clock.tick(60)
