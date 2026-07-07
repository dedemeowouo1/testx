import pygame

import random

from galaxy import Body

from physics import compute_acceleration

from integrator import leapfrog

pygame.init()

WIDTH=1200
HEIGHT=900

screen=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()

bodies=[]

# 建立100個星系種子

for i in range(100):

    x=random.uniform(-400,400)

    y=random.uniform(-400,400)

    vx=random.uniform(-0.5,0.5)

    vy=random.uniform(-0.5,0.5)

    m=random.uniform(100,500)

    bodies.append(

        Body(

            m,

            [x,y],

            [vx,vy],

            (255,255,255)

        )

    )

# 建立5000個藍色粒子

for i in range(5000):

    x=random.uniform(-500,500)

    y=random.uniform(-500,500)

    vx=random.uniform(-1,1)

    vy=random.uniform(-1,1)

    bodies.append(

        Body(

            1,

            [x,y],

            [vx,vy],

            (80,120,255)

        )

    )

compute_acceleration(bodies)

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            running=False

    leapfrog(bodies,0.05)

    screen.fill((0,0,0))

    for b in bodies:

        sx=int(b.pos[0])+WIDTH//2

        sy=int(b.pos[1])+HEIGHT//2

        if 0<=sx<WIDTH and 0<=sy<HEIGHT:

            pygame.draw.circle(

                screen,

                b.color,

                (sx,sy),

                1 if b.mass<10 else 4

            )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
