import pygame as pg
from pygame.locals import *
import math

# Inicializar Pygame
pg.init()
screen = pg.display.set_mode((720, 1000))
directorio = "Menu/"

#poner musica de fondo
pg.mixer.music.load("musica/8_bit_ice_cave_lofi.mp3")
pg.mixer.music.play(-1)


#cambiar el mouse a puntero
pg.mouse.set_cursor(*pg.cursors.tri_left)


# menu principal con opciones de jugar y salir usando imagenes animadas con coseno y seno
def menu_principal():
    # Cargar imagenes
    titulo = pg.image.load(directorio + "titulo.png").convert_alpha()
    fondo = pg.image.load(directorio + "fondo.png").convert_alpha()
    play = pg.image.load(directorio + "jugar.png").convert_alpha()
    salir = pg.image.load(directorio + "salir.png").convert_alpha()
    arboles = pg.image.load(directorio + "arboles.png").convert_alpha()
    nube1 = pg.image.load(directorio + "nube1.png").convert_alpha()
    nube2 = pg.image.load(directorio + "nube2.png").convert_alpha()
    # Escalar imagenes
    play = pg.transform.scale(play, (200, 200))
    salir = pg.transform.scale(salir, (200, 200))
    arboles = pg.transform.scale(arboles, (720, 1000))
    titulo = pg.transform.scale(titulo, (500, 300))
    nube1 = pg.transform.scale(nube1, (800, 800))
    nube2 = pg.transform.scale(nube2, (800, 800))
    # Variables
    x_play = 260
    y_play = 400
    x_salir = 260
    y_salir = 600
    angulo = 0
    x_titulo = 100
    y_titulo = 100
    x_arboles = screen.get_width() // 2 - arboles.get_width() // 2
    y_arboles = screen.get_height() - arboles.get_height()
    x_nube1 = 280
    y_nube1 = screen.get_height() - arboles.get_height() - 200
    x_nube2 = 300
    y_nube2 = screen.get_height() - arboles.get_height() - 200

    # Bucle
    while True:
        screen.blit(fondo, (0, 0))
        screen.blit(nube1, (x_nube1, y_nube1))
        screen.blit(nube2, (x_nube2, y_nube2))
        screen.blit(arboles, (x_arboles, y_arboles))
        screen.blit(play, (x_play, y_play))
        screen.blit(salir, (x_salir, y_salir))
        screen.blit(titulo, (x_titulo, y_titulo))
        
        pg.display.flip()

        #definir x, y
        x, y = 0, 0

        # Eventos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
            if x >= x_play and x <= x_play + 200 and y >= y_play and y <= y_play + 200:
                #reproducir sonido de boton
                pg.mixer.Sound("musica/sfx_sounds_powerup3.wav").play()
                #parar musica de fondo
                pg.mixer.music.stop()
                import blob as juego
                juego.blobmascota()
            if x >= x_salir and x <= x_salir + 200 and y >= y_salir and y <= y_salir + 200:
                #reproducir sonido de boton
                pg.mixer.Sound("musica/sfx_sounds_negative1.wav").play()
                #esperar 2 segundo antes de cerrar
                pg.time.wait(2000)
                pg.quit()
                return
        # Animacion
        angulo += 0.05
        x_play = 260 + 2 * math.cos(angulo)
        x_salir = 260 - 2 * math.cos(angulo)
        y_titulo = 100 - 2 * math.sin(angulo)
        #mover arboles arriba y abajo usando sin
        y_arboles = screen.get_height() - arboles.get_height() + 2 * math.sin(angulo)
        #mover nubes de derecha a izquierda hasta que desaparezcan y vuelvan a aparecer
        x_nube1 += 1
        x_nube2 += 1
        if x_nube1 > screen.get_width():
            x_nube1 = -800
        if x_nube2 > screen.get_width():
            x_nube2 = -800



menu_principal()
