import os
import pygame
import sys
import numpy as np
# Inicializar pygame
pygame.init()
onx=False
ony=False
onimg=True
izq = False
derch = False
up=True
down=False
superficie_transparente = pygame.Surface((200, 100), pygame.SRCALPHA)
color = (50, 50, 100, 0)
color2 = (50, 50, 100,255)
# Configurar el tamaño de la ventana
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("GTA 2")

cocheizq=pygame.image.load("pixil-frame-0 (2)izq.png")
cochederch=pygame.image.load("pixil-frame-0 (2)derch.png")
cocheup=pygame.image.load("pixil-frame-0 (1).png")
cochedown=pygame.image.load("pixil-frame-0 (2)down.png")

# Colores
BLANCO = (123, 255, 255)
fondo_img = pygame.image.load("pixil-frame-0.png")
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))
# Configurar el jugador
jugador_img=cocheup
jugador_size = jugador_img.get_rect().size 
# Obtener el tamaño de la imagen
jugador_x = ANCHO // 2 - jugador_size[0] // 2
jugador_y = ALTO // 2 - jugador_size[1] // 2
velocidad_jugador = 5

# Bucle principal del juego
vX= pygame.math.Vector2(jugador_x + 30, jugador_x - 30)
vY= pygame.math.Vector2(jugador_y + 30, jugador_y - 30)
esquina_pos=pygame.math.Vector2(jugador_x,jugador_y)
area_size = pygame.math.Vector2(jugador_size[0],jugador_size[1])
jugando = True
while jugando:
    mouse_pos = pygame.mouse.get_pos()
    pygame.display.set_caption(f"Jugador X: {jugador_x} Jugador Y: {jugador_y} MOUSE POS: {mouse_pos}")
    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in range(int(esquina_pos.x), int(esquina_pos.x + area_size.x)) and \
            mouse_pos[1] in range(int(esquina_pos.y), int(esquina_pos.y + area_size.y)):
            print("si")
            jugador_img=pygame.image.load("transparente.png")
            pantalla.blit(jugador_img, (jugador_x,jugador_y))
            pygame.display.flip()
            onimg = False
    if onimg:
        if izq:
            if jugador_img == cocheup or jugador_img == cochedown:
                jugador_img=cocheizq
        elif derch:
            if jugador_img == cocheup or jugador_img == cochedown:
                jugador_img=cochederch
        elif up:
            if jugador_img == cochederch or jugador_img == cocheizq:
                jugador_img=cocheup
        elif down:
            if jugador_img == cochederch or jugador_img == cocheizq:
                jugador_img=cochedown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
            pygame.quit()
            sys.exit()
    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover el jugador
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad_jugador
        down=False
        up=False
        izq = True
        derch = False
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad_jugador
        down=False
        up=False
        izq = False
        derch = True
    if teclas[pygame.K_UP]:
        down=False
        up=True
        izq=False
        derch=False
        jugador_y -= velocidad_jugador
    if teclas[pygame.K_DOWN]:
        down=True
        up=False
        izq=False
        derch=False
        jugador_y += velocidad_jugador

    # Mantener el jugador dentro de los límites
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x > ANCHO - jugador_size[0]:
        jugador_x = ANCHO - jugador_size[0]
    if jugador_y < 0:
        jugador_y = 0
    if jugador_y > ALTO - jugador_size[0]:
        jugador_y = ALTO - jugador_size[0]

    # Rellenar la pantalla con color blanco
    pantalla.fill(BLANCO)
    # Dibujar el jugador (cuadrado rojo)
    pantalla.blit(fondo_img, (0, 0))
    pantalla.blit(jugador_img, (jugador_x,jugador_y))
    
    vX= pygame.math.Vector2(jugador_x + 30, jugador_x - 30)
    vY= pygame.math.Vector2(jugador_y + 30, jugador_y - 30)
    esquina_pos=pygame.math.Vector2(jugador_x,jugador_y )
    area_size = pygame.math.Vector2(jugador_size[0],jugador_size[1])
    pygame.draw.rect(superficie_transparente, color, (*esquina_pos, *area_size))
    
    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    pygame.time.Clock().tick(60)


