import pygame
import sys
import time


Fight_End = False
Map_Id = ""
draw_in_order = []
draw_in_order_F = []
Draw_List = []
Draw_List_F = []
display_scroll = [0, 0]
P_scroll = [0, 0]
StartRender = 1
YourTurn = 0
Tura_Licznik = 0
OknoX = 800
OknoY = 600
grid_size = 32
display = pygame.display.set_mode((OknoX, OknoY))
enemies = []
players = []
walls = []
kolejka = []

npc = pygame.image.load('npc.gif').convert_alpha()
gracz1 = pygame.image.load('wolmar1.gif').convert_alpha()
szczur = pygame.image.load('szczur.gif').convert_alpha()
gracz = pygame.image.load('strzelec.gif').convert_alpha()
znak = pygame.image.load('znacznik.png').convert_alpha()