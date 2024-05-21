import pygame as pg
from pygame.locals import *
import math
import csv
import juegos as jg

# Inicializar Pygame
pg.init()
screen = pg.display.set_mode((720, 1000))
directorio = "menu2/"

#pointer
pg.mouse.set_cursor(*pg.cursors.tri_left)

#menu de modos de juego

def modosdejuego():
    #cargar imagenes
    fondo = pg.image.load(directorio + "fondo2.PNG").convert_alpha()
    titulo = pg.image.load(directorio + "Titulo2.PNG").convert_alpha()
    magofeliz = pg.image.load(directorio + "mago.PNG").convert_alpha()
    pinosatras = pg.image.load(directorio + "pinosatras.PNG").convert_alpha()
    arbol = pg.image.load(directorio + "arbol.PNG").convert_alpha()
    regreso = pg.image.load("Menu/Regreso_.png").convert_alpha()

    #imagenes de opciones
    logaritmos = pg.image.load(directorio + "log.png").convert_alpha()
    circulounitario = pg.image.load(directorio + "circulo.png").convert_alpha()
    graficas = pg.image.load(directorio + "graficas.png").convert_alpha()

    #escalar imagenes
    fondo = pg.transform.scale(fondo, (720, 1000))
    titulo = pg.transform.scale(titulo, (500, 300))
    magofeliz = pg.transform.scale(magofeliz, (600, 800))
    pinosatras = pg.transform.scale(pinosatras, (720, 1000))
    arbol = pg.transform.scale(arbol, (720, 1000))
    regreso = pg.transform.scale(regreso, (150,150))
    
    #escalar imagenes de opciones
    logaritmos = pg.transform.scale(logaritmos, (350, 200))
    circulounitario = pg.transform.scale(circulounitario, (350, 200))
    graficas = pg.transform.scale(graficas, (350, 200))

    #variables
    x_titulo = screen.get_width() // 2 - titulo.get_width() // 2 
    y_titulo = 0
    x_mago = screen.get_width() // 2 - magofeliz.get_width() // 2
    y_mago = 200
    x_pinosatras = screen.get_width() // 2 - pinosatras.get_width() // 2
    y_pinosatras = screen.get_height() - pinosatras.get_height()
    x_arbol = screen.get_width() // 2 - arbol.get_width() // 2
    y_arbol = screen.get_height() - arbol.get_height()
    x_regreso = 10 
    y_regreso = 800

    # variables de opciones una denajo de la otra
    x_log = screen.get_width() // 2 - logaritmos.get_width() // 2
    y_log = 450  

    x_circulo = screen.get_width() // 2 - circulounitario.get_width() // 2
    y_circulo = 600  

    x_graficas = screen.get_width() // 2 - graficas.get_width() // 2
    y_graficas = 750  


    #bucle
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                mouse_rect = pg.Rect(*mouse_pos, 1, 1)
                if logaritmos.get_rect(topleft=(x_log, y_log)).colliderect(mouse_rect):
                    # Ir al modo de juego de logaritmos
                    print("logaritmos")
                elif circulounitario.get_rect(topleft=(x_circulo, y_circulo)).colliderect(mouse_rect):
                    # Ir al modo de juego de circulounitario
                    jg.circulounitario()
                    
                elif graficas.get_rect(topleft=(x_graficas, y_graficas)).colliderect(mouse_rect):
                    # Ir al modo de juego de graficas
                    jg.graficas()
                    
                elif regreso.get_rect(topleft=(x_regreso, y_regreso)).colliderect(mouse_rect):
                    import blob
                    blob.blobmascota()
        #animacion imagenes seno y coseno
        y_mago = 209 + 2 * math.sin(pg.time.get_ticks() / 500)
        y_titulo = 10 + 10 * math.sin(pg.time.get_ticks() / 500)
        y_pinosatras = screen.get_height() - pinosatras.get_height() + 10 * math.cos(pg.time.get_ticks() / 500)
        y_log = 305 + 10 * math.sin(pg.time.get_ticks() / 500)
        y_circulo = 455 + 10 * math.sin(pg.time.get_ticks() / 500)
        y_graficas = 605 + 10 * math.sin(pg.time.get_ticks() / 500)

        #mostrar imagenes
        screen.blit(fondo, (0, 0))
        screen.blit(titulo, (x_titulo, y_titulo))
        screen.blit(pinosatras, (x_pinosatras, y_pinosatras))
        screen.blit(arbol, (x_arbol, y_arbol))
        screen.blit(magofeliz, (x_mago, y_mago))
        screen.blit(logaritmos, (x_log, y_log))
        screen.blit(circulounitario, (x_circulo, y_circulo))
        screen.blit(graficas, (x_graficas, y_graficas))
        screen.blit(regreso, (x_regreso, y_regreso))
        pg.display.update()


