import pygame as pg
from pygame.locals import *
import math
import csv

# Inicializar Pygame
pg.init()
screen = pg.display.set_mode((720, 1000))
directorio = "menu2/"

#pointer
pg.mouse.set_cursor(*pg.cursors.tri_left)

def graficas():
    directorio = "graficas/"
    #cargar imagenes
    fondo = pg.image.load(directorio + "fondo3.png").convert_alpha()
    titulo = pg.image.load(directorio + "titulo3.png").convert_alpha()
    opcion1 = pg.image.load(directorio + "OPCION1.png").convert_alpha()
    opcion2 = pg.image.load(directorio + "OPCION2.png").convert_alpha()
    opcion3 = pg.image.load(directorio + "OPCION3.png").convert_alpha()
    opcion4 = pg.image.load(directorio + "OPCION4.png").convert_alpha()
    opcion5 = pg.image.load(directorio + "OPCION5.png").convert_alpha()

    #escalar imagenes
    fondo = pg.transform.scale(fondo, (720, 1000))
    titulo = pg.transform.scale(titulo, (500, 300))

    #respuestas de preguntas
    opcion1 = pg.transform.scale(opcion1, (300, 100))
    opcion2 = pg.transform.scale(opcion2, (300, 100))
    opcion3 = pg.transform.scale(opcion3, (300, 100))
    opcion4 = pg.transform.scale(opcion4, (300, 100))
    opcion5 = pg.transform.scale(opcion5, (300, 100))


    #imagenes de preguntas
    pregunta1 = pg.image.load(directorio + "absoluto.png").convert_alpha()
    pregunta2 = pg.image.load(directorio + "DIVIDIDO1.png").convert_alpha()
    pregunta3 = pg.image.load(directorio + "X2.png").convert_alpha()
    pregunta4 = pg.image.load(directorio + "X3.png").convert_alpha()
    pregunta5 = pg.image.load(directorio + "5.png").convert_alpha()

    #escalar imagenes de preguntas
    pregunta1 = pg.transform.scale(pregunta1, (350, 300))
    pregunta2 = pg.transform.scale(pregunta2, (350, 300))
    pregunta3 = pg.transform.scale(pregunta3, (350, 300))
    pregunta4 = pg.transform.scale(pregunta4, (350, 300))
    pregunta5 = pg.transform.scale(pregunta5, (350, 300))

    puntuacion = 0
    pregunta_actual = 0

    preguntas = [
        {'imagen': 'pregunta1', 'opciones': ['opcion1', 'opcion3', 'opcion5'], 'correcta': 'opcion5'},
        {'imagen': 'pregunta2', 'opciones': ['opcion1', 'opcion2', 'opcion3'], 'correcta': 'opcion1'},
        {'imagen': 'pregunta3', 'opciones': ['opcion1', 'opcion2', 'opcion4'], 'correcta': 'opcion4'},
        {'imagen': 'pregunta4', 'opciones': ['opcion1', 'opcion2', 'opcion3'], 'correcta': 'opcion2'},
        {'imagen': 'pregunta5', 'opciones': ['opcion1', 'opcion5', 'opcion3'], 'correcta': 'opcion3'}
    ]

    #cambiar de identificador a imagen
    imagenes_opciones = {
        'opcion1': opcion1,
        'opcion2': opcion2,
        'opcion3': opcion3,
        'opcion4': opcion4,
        'opcion5': opcion5, }
    
    imagenes_preguntas = {'pregunta1': pregunta1, 'pregunta2': pregunta2, 'pregunta3': pregunta3, 'pregunta4': pregunta4, 'pregunta5': pregunta5}


    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                mouse_rect = pg.Rect(*mouse_pos, 1, 1)
                for i, opcion in enumerate(preguntas[pregunta_actual]['opciones']):
                    imagen_opcion = imagenes_opciones[opcion]
                    if imagen_opcion.get_rect(topleft=(200, 500 + 100 * i)).colliderect(mouse_rect):
                        if opcion == preguntas[pregunta_actual]['correcta']:
                            print("Correcto")
                            puntuacion += 1
                        else:
                            print("Incorrecto")
                        pregunta_actual += 1
                        if pregunta_actual >= len(preguntas):
                            with open('puntuacion.csv', 'a', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow([puntuacion])
                            return

        screen.blit(fondo, (0, 0))
        screen.blit(titulo, (screen.get_width() // 2 - titulo.get_width() // 2, 0))
        screen.blit(imagenes_preguntas[preguntas[pregunta_actual]['imagen']], (150, 200))
        for j, opcion in enumerate(preguntas[pregunta_actual]['opciones']):
            screen.blit(imagenes_opciones[opcion], (200, 500 + 100 * j))
        pg.display.update()

def circulounitario():
    #directorios
    directorio = "circulo/"
    #cargar imagenes
    fondo = pg.image.load(directorio + "Fondo4.png").convert_alpha()
    titulo = pg.image.load(directorio + "titulo4.png").convert_alpha()
    
    #circulo unitario imagenes
    opcion1 = pg.image.load(directorio + "opcion1.png").convert_alpha()
    opcion2 = pg.image.load(directorio + "opcion2.png").convert_alpha()
    opcion3 = pg.image.load(directorio + "opcion3.png").convert_alpha()
    opcion4 = pg.image.load(directorio + "opcion4.png").convert_alpha()
    opcion5 = pg.image.load(directorio + "opcion5.png").convert_alpha()
    opcion6 = pg.image.load(directorio + "opcion6.png").convert_alpha()
    opcion7 = pg.image.load(directorio + "opcion7.png").convert_alpha()
    opcion8 = pg.image.load(directorio + "opcion8.png").convert_alpha()

    #respuestas de preguntas
    respuesta1 = pg.image.load(directorio + "respuesta1.png").convert_alpha()
    respuesta2 = pg.image.load(directorio + "respuesta2.png").convert_alpha()
    respuesta3 = pg.image.load(directorio + "respuesta3.png").convert_alpha()
    respuesta4 = pg.image.load(directorio + "respuesta4.png").convert_alpha()
    respuesta5 = pg.image.load(directorio + "respuesta5.png").convert_alpha()
    respuesta6 = pg.image.load(directorio + "respuesta6.png").convert_alpha()
    respuesta7 = pg.image.load(directorio + "respuesta7.png").convert_alpha()
    respuesta8 = pg.image.load(directorio + "respuesta8.png").convert_alpha()

    #escalar imagenes
    fondo = pg.transform.scale(fondo, (720, 1000))
    titulo = pg.transform.scale(titulo, (500, 300))

    #respuestas de preguntas
    respuesta1 = pg.transform.scale(respuesta1, (300, 100))
    respuesta2 = pg.transform.scale(respuesta2, (300, 100))
    respuesta3 = pg.transform.scale(respuesta3, (300, 100))
    respuesta4 = pg.transform.scale(respuesta4, (300, 100))
    respuesta5 = pg.transform.scale(respuesta5, (300, 100))
    respuesta6 = pg.transform.scale(respuesta6, (300, 100))
    respuesta7 = pg.transform.scale(respuesta7, (300, 100))
    respuesta8 = pg.transform.scale(respuesta8, (300, 100))

    #circulo unitario imagenes
    opcion1 = pg.transform.scale(opcion1, (300, 300))
    opcion2 = pg.transform.scale(opcion2, (300, 300))
    opcion3 = pg.transform.scale(opcion3, (300, 300))
    opcion4 = pg.transform.scale(opcion4, (300, 300))
    opcion5 = pg.transform.scale(opcion5, (300, 300))
    opcion6 = pg.transform.scale(opcion6, (300, 300))
    opcion7 = pg.transform.scale(opcion7, (300, 300))
    opcion8 = pg.transform.scale(opcion8, (300, 300))

    puntuacion = 0
    pregunta_actual = 0

    preguntas = [
        {'imagen': 'opcion1', 'opciones': ['respuesta1', 'respuesta2', 'respuesta3'], 'correcta': 'respuesta1'},
        {'imagen': 'opcion2', 'opciones': ['respuesta4', 'respuesta2', 'respuesta6'], 'correcta': 'respuesta2'},
        {'imagen': 'opcion3', 'opciones': ['respuesta3', 'respuesta8', 'respuesta1'], 'correcta': 'respuesta3'},
        {'imagen': 'opcion4', 'opciones': ['respuesta2', 'respuesta3', 'respuesta4'], 'correcta': 'respuesta4'},
        {'imagen': 'opcion5', 'opciones': ['respuesta5', 'respuesta6', 'respuesta7'], 'correcta': 'respuesta5'},
        {'imagen': 'opcion6', 'opciones': ['respuesta6', 'respuesta1', 'respuesta2'], 'correcta': 'respuesta6'},
        {'imagen': 'opcion7', 'opciones': ['respuesta3', 'respuesta4', 'respuesta7'], 'correcta': 'respuesta7'},
        {'imagen': 'opcion8', 'opciones': ['respuesta6', 'respuesta7', 'respuesta8'], 'correcta': 'respuesta8'}]
    
    #imagenes de preguntas 
    imagenes_opciones = {
        'respuesta1': respuesta1,
        'respuesta2': respuesta2,
        'respuesta3': respuesta3,
        'respuesta4': respuesta4,
        'respuesta5': respuesta5,
        'respuesta6': respuesta6,
        'respuesta7': respuesta7,
        'respuesta8': respuesta8}
    
    imagenes_preguntas = {'opcion1': opcion1, 'opcion2': opcion2, 'opcion3': opcion3, 'opcion4': opcion4, 'opcion5': opcion5, 'opcion6': opcion6, 'opcion7': opcion7, 'opcion8': opcion8}

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                mouse_rect = pg.Rect(*mouse_pos, 1, 1)
                for i, opcion in enumerate(preguntas[pregunta_actual]['opciones']):
                    imagen_opcion = imagenes_opciones[opcion]
                    if imagen_opcion.get_rect(topleft=(200, 500 + 100 * i)).colliderect(mouse_rect):
                        if opcion == preguntas[pregunta_actual]['correcta']:
                            print("Correcto")
                            puntuacion += 1
                        else:
                            print("Incorrecto")
                        pregunta_actual += 1
                        puntuacion_circulo_unitario = puntuacion
                        if pregunta_actual >= len(preguntas):
                            with open('puntuacion.csv', 'a', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow([puntuacion, puntuacion_circulo_unitario])
                            return
        #animacion de imagenes
        x_titulo = screen.get_width() // 2 - titulo.get_width() // 2
        y_titulo = -50 + 10 * math.sin(pg.time.get_ticks() / 300)

        screen.blit(fondo, (0, 0))
        screen.blit(titulo, (x_titulo, y_titulo))
        screen.blit(imagenes_preguntas[preguntas[pregunta_actual]['imagen']], (200, 200))
        for j, opcion in enumerate(preguntas[pregunta_actual]['opciones']):
            screen.blit(imagenes_opciones[opcion], (200, 500 + 100 * j))
        pg.display.update()





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
                    print("circulo unitario")
                elif graficas.get_rect(topleft=(x_graficas, y_graficas)).colliderect(mouse_rect):
                    # Ir al modo de juego de graficas
                    print("graficas")
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


circulounitario()