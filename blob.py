import pygame as pg
from pygame.locals import *
import math


# Inicializar Pygame
pg.init()
screen = pg.display.set_mode((720, 1000))
directorio = "blob/"

#poner musica de fondo
pg.mixer.music.load("musica/8_bit_ice_cave_lofi.mp3")
pg.mixer.music.play(-1)

#pointer
pg.mouse.set_cursor(*pg.cursors.tri_left)

#mago se apach
mago_apach = False

#animacion mago serio y enojado 
def mago():
    global mago_apach
    #emociones imagenes
    serio = pg.image.load(directorio + "magoserio.PNG").convert_alpha()
    enojado = pg.image.load(directorio + "magoenojado.PNG").convert_alpha()
    #escalar imagenes
    serio = pg.transform.scale(serio, (600, 300))
    enojado = pg.transform.scale(enojado, (600, 300))
    #aparecer abajo por 5 segundos
    x_serio = screen.get_width() // 2 - serio.get_width() // 2
    y_serio = 500
    # Variables
    mago_actual = serio
    mouse_rect = pg.Rect(0, 0, 1, 1)
    # Bucle
    while True:
        if not mago_apach:
            #reproducir sonido mientras aparece
            pg.mixer.Sound("musica/mago.mp3").play()
            screen.blit(serio, (x_serio, y_serio))
            pg.display.update()
            pg.time.delay(100)
            screen.blit(enojado, (x_serio, y_serio))
            pg.display.update()
            pg.time.delay(2000)
            screen.fill((0, 0, 0))
            pg.display.update()
            mago_apach = True



    

def blobmascota():
    # Cargar imagenes
    fondo = pg.image.load(directorio + "blofondo.png").convert_alpha()
    blobfeliz = pg.image.load(directorio + "feliz.png").convert_alpha()
    blobtriste = pg.image.load(directorio + "triste.png").convert_alpha()
    blobserio = pg.image.load(directorio + "serio.png").convert_alpha()
    superficie = pg.image.load(directorio + "superficie.png").convert_alpha()
    botonjugar = pg.image.load(directorio + "botonjugar.png").convert_alpha()
    hamburguesa = pg.image.load(directorio + "burger-1.png").convert_alpha()
    regreso = pg.image.load("Menu/Regreso_.png").convert_alpha()

    # Escalar imagenes
    blobfeliz = pg.transform.scale(blobfeliz, (450, 450))
    blobtriste = pg.transform.scale(blobtriste, (450, 450))
    blobserio = pg.transform.scale(blobserio, (450, 450))
    superficie = pg.transform.scale(superficie, (720, 1000))
    botonjugar = pg.transform.scale(botonjugar, (300, 200))
    hamburguesa = pg.transform.scale(hamburguesa, (100, 100))
    regreso = pg.transform.scale(regreso, (150,150))
    
    # Variables
    x_blob = screen.get_width() // 2 - blobfeliz.get_width() // 2
    y_blob = 200
    x_superficie = screen.get_width() // 2 - superficie.get_width() // 2
    y_superficie = screen.get_height() - superficie.get_height()
    x_botonjugar = 200
    y_botonjugar = 800
    x_hamburguesa = x_superficie + superficie.get_width() - hamburguesa.get_width() - 100
    y_hamburguesa = y_superficie + superficie.get_height() - hamburguesa.get_height() - 200
    x_regreso = 10 
    y_regreso = 800

    # Variables
    blob_actual = blobserio
    mouse_rect = pg.Rect(0, 0, 1, 1)

    while True:
        # Eventos
        screen.blit(fondo, (0, 0))
        screen.blit(superficie, (x_superficie, y_superficie))
        screen.blit(botonjugar, (x_botonjugar, y_botonjugar))
        screen.blit(hamburguesa, (x_hamburguesa, y_hamburguesa))
        

        #animacion de blob arriba y abajo con sin
        angulo = math.sin(pg.time.get_ticks() * 0.01) * 10
        y_blob = 200 + angulo

        #animacion de flotar boton jugar
        angulo = math.sin(pg.time.get_ticks() * - 0.01) * 10
        y_botonjugar = 800 + angulo

        #animacion de hamburguesa
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            #al presionar la hamburguesa el mood de blob cambia
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                mouse_rect = pg.Rect(*mouse_pos, 1, 1)
                if hamburguesa.get_rect(topleft=(x_hamburguesa, y_hamburguesa)).colliderect(mouse_rect):
                    blob_actual = blobtriste
                    if not mago_apach:
                        mago()
                        #esperar 5 segundos
                        pg.time.delay(5000)
                        # Establece mago_apachurado en True
                        mago_apach = True
                    elif mago_apach == True:
                        mago_apach = False
                elif botonjugar.get_rect(topleft=(x_botonjugar, y_botonjugar)).colliderect(mouse_rect):
                    #sonido al presionar
                    pg.mixer.Sound("musica/sfx_sounds_powerup2.wav").play()
                    blob_actual = blobfeliz
                    #parar musica de fondo
                    pg.mixer.music.stop()
                    import modos as m 
                    m.modosdejuego()
                elif regreso.get_rect(topleft=(x_regreso, y_regreso)).colliderect(mouse_rect):
                    #sonido al presionar
                    pg.mixer.Sound("musica/sfx_sounds_powerup2.wav").play()
                    pg.mixer.music.stop()
                    import main as m
                    m.main()
        #dibujar blob    
        screen.blit(blob_actual, (x_blob, y_blob))
        screen.blit(regreso, (x_regreso, y_regreso))
        pg.display.flip()


              
