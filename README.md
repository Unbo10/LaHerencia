# LaHerencia

``` mermaid
    classDiagram

    class Test{
        - int dimensions
        - int iterations

        - test_function()
        - start_test(heuristic, iterations)
        - graph_heuristic(heuristic)
        - graph_particle(Particle)
    }

    Test o-- Vector
    Test --> ParticleSwarm : Uses

    class Vector {
        <!-- * Proposed class -->
        <!-- ! Since we need to use inheritance, we could consider each vector -velocity, heuristic and position-, to inherit from the vector class. I don't see many other classes were this could happen -->
        - ~float~ coordinates
        - ~int~ color
        <!-- * To distinguish between gbest and other particles -->
        - int dimensions

        - initialize_randomly(float)

        + get_coordinates(): ~float~
        + set_coordinates(): ~float~
    }

    class Velocity {
        - update_velocity(velocity, gbest, cognitive_coefficient, social_coefficient, inertia, pbest, position, r_1, r_2) 
    }

    class ParticleSwarm{
        - float cognitive_coefficient
        - float inertia
        - float social_coefficient
        - int particle_amount
        - ~Particle~ particles
        - Vector gbest

        - update_gbest(particles)

        + get_cognitive_coefficient(): float
        + get_inertia(): float
        + get_social_coefficient(): float
        + get_particles_amount(): int
        + get_gbest(): Vector

    }
    ParticleSwarm o-- Particle :The swarm contains Particles, but they can exist without the swarm (Aggreggation) 
    ParticleSwarm o-- Vector

    class Particle{
        <!-- ? Are r_1 and r_2 chosen for every iteration or at each iteration? -->
        # Vector heuristic_value
        # Vector pbest
        # Vector position
        # Vector velocity

        - update_heuristic(Vector)
        - update_position(position)
        - update_pbest(position)
        
        + get_position()
        + get_velocity()
        + get_pbest()

        + set_position()
        + set_velocity()
        + set_pbest()
    }
    Particle o-- Vector

    ```
