def leapfrog(bodies,dt):

    for b in bodies:

        b.vel += 0.5*b.acc*dt

        b.pos += b.vel*dt

    from physics import compute_acceleration

    compute_acceleration(bodies)

    for b in bodies:

        b.vel += 0.5*b.acc*dt
