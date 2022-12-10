import pygame, random
pygame.init()


# creation de la fenetre
screen = pygame.display.set_mode((1915, 1040))
pygame.display.set_caption("ALpaint")

# mettre la couleur du fond a blanc
screen.fill((255, 255, 255))


# mise en place de la distance x et y
x = 0
y = 0


# nb pixel de large pour rect de couleur
pixel = 5

# creation de la boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # creation de la couleur aleatoire
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)

    # generation d'un rectangle de couleur
    rect = pygame.Rect(x, y, pixel, pixel)
    pygame.draw.rect(screen, (c1, c2, c3), rect)

    if x < 1920:
        x += pixel
        if x == 1920:
            x = 0
            y += pixel

    pygame.display.flip()
