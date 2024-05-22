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

def gameover():
    directorio = "Game/"
    #cargar imagenes
    fondo = pg.image.load(directorio + "fondo6.png").convert_alpha()
    titulo = pg.image.load(directorio + "titulo6.png").convert_alpha()
    arbol1 = pg.image.load(directorio + "arbol1.png").convert_alpha()
    arbol2 = pg.image.load(directorio + "arbol2.png").convert_alpha()

    #boton
    regresar = pg.image.load(directorio + "regresarboton.png").convert_alpha()

    #escalar imagenes
    fondo = pg.transform.scale(fondo, (720, 1000))
    titulo = pg.transform.scale(titulo, (450, 500))
    regresar = pg.transform.scale(regresar, (350, 300))
    arbol1 = pg.transform.scale(arbol1, (720, 1000))
    arbol2 = pg.transform.scale(arbol2, (720, 1000))

    #variables
    x_titulo = screen.get_width() // 2 - titulo.get_width() // 2
    y_titulo = 0

    #boton
    x_regresar = screen.get_width() // 2 - regresar.get_width() // 2 
    y_regresar = screen.get_height() // 2 - regresar.get_height() // 2 + 90

    #bucle
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                mouse_rect = pg.Rect(*mouse_pos, 1, 1)
                if regresar.get_rect(topleft=(x_regresar, y_regresar)).colliderect(mouse_rect):
                    # Ir al menu
                    import modos 
                    modos.modosdejuego()
        #animacion de imagenes
        x_arbol1 = 0 + 10 * math.sin(pg.time.get_ticks() / 500)
        x_arbol2 = 10 + 10 * math.sin(pg.time.get_ticks() / 500)
        #boton regresar animada
        x_regresar = 200 + 10 * math.sin(pg.time.get_ticks() / 500)
        y_titulo = 10 + 10 * math.cos(pg.time.get_ticks() / 500)
        #mostrar imagenes
        screen.blit(fondo, (0, 0))
        screen.blit(titulo, (x_titulo, y_titulo))
        screen.blit(regresar, (x_regresar, y_regresar))
        screen.blit(arbol1, (x_arbol1, 0))
        screen.blit(arbol2, (x_arbol2, 0))
        #mostrar puntuacion
        with open('puntuacion.csv', 'r') as f:
            reader = csv.reader(f)
            puntuaciones = list(reader)
            puntuacion = puntuaciones[-1][0]
            font = pg.font.Font(None, 36)
            text = font.render(f"Puntuacion: {puntuacion}", True, (255, 255, 255))
            screen.blit(text, (10, 10))
        pg.display.update()




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
                            gameover()  # Go to gameover screen
                            pg.display.quit()
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
                            gameover()
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
