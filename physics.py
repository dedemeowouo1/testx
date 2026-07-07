import numpy as np

SOFTENING = 2.0

G = 1.0


def compute_acceleration(bodies):

    n = len(bodies)

    for b in bodies:
        b.acc[:] = 0

    for i in range(n):

        for j in range(i+1,n):

            dx = bodies[j].pos - bodies[i].pos

            r2 = np.dot(dx,dx)+SOFTENING**2

            r = np.sqrt(r2)

            F = G/r2

            a1 = F*bodies[j].mass*dx/r

            a2 = -F*bodies[i].mass*dx/r

            bodies[i].acc += a1

            bodies[j].acc += a2
