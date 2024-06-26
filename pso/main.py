"""
A module to run the Particle Swarm Optimization (PSO) algorithm.

## Classes
Main: Main class to run the Particle Swarm Optimization (PSO) algorithm.

### Methods
- graph_heuristic() -> None
- graph_particles() -> None
- heuristic(position: Position) -> float
- optimize() -> None

#### Getters
- get_cognitive_coefficient() -> float
- get_dimensions() -> int
- get_inertia_coefficient() -> float
- get_iterations() -> int
- get_particle_amount() -> int
- get_social_coefficient() -> float
- get_swarm() -> ParticleSwarm
"""
import numpy as np
import math

from pso.swarm.particle_swarm import ParticleSwarm
from pso.vector.position import Position

class Main:
    """Main class to run the Particle Swarm Optimization (PSO) algorithm.
    
    ## Parameters
    - cognitive_coefficient : float, optional
        The cognitive coefficient used in the PSO algorithm. Default is 2.
    - inertia_coefficient : float, optional
        The inertia coefficient used in the PSO algorithm. Default is 1.
    - social_coefficient : float, optional
        The social coefficient used in the PSO algorithm. Default is 2.
    - particle_amount : int, optional
        The number of particles in the swarm. Default is 10.
    - dimensions : int, optional
        The number of dimensions in the search space. Default is 3.
    - iterations : int, optional
        The number of iterations to run the algorithm. Default is 20.
    
    ## Attributes
    - __cognitive_coefficient : float
        The cognitive coefficient used in the PSO algorithm.
    - __dimensions : int
        The number of dimensions in the search space.
    - __inertia_coefficient : float
        The inertia coefficient used in the PSO algorithm.
    - __iterations : int
        The number of iterations to run the algorithm.
    - __particle_amount : int
        The number of particles in the swarm.
    - __social_coefficient : float
        The social coefficient used in the PSO algorithm.
    - __swarm : ParticleSwarm
        The particle swarm used in the optimization process.
    
    ## Methods
    - graph_heuristic() -> None
        Graphs the heuristic function to be optimized.
    - graph_particles() -> None
        Graphs the particles in the swarm.
    - heuristic(position: Position) -> float
        Heuristic function to be optimized.
    - optimize() -> None
        Optimizes the heuristic function using the PSO algorithm.

    ### Getters
    - get_cognitive_coefficient() -> float
        Returns the cognitive coefficient.
    - get_dimensions() -> int
        Returns the number of dimensions.
    - get_inertia_coefficient() -> float
        Returns the inertia coefficient.
    - get_iterations() -> int
        Returns the number of iterations.
    - get_particle_amount() -> int
        Returns the number of particles.
    - get_social_coefficient() -> float
        Returns the social coefficient.
    - get_swarm() -> ParticleSwarm
        Returns the particle swarm used in the optimization process.
    """
    def __init__(self, cognitive_coefficient: float = 2, inertia_coefficient: float = 1, social_coefficient: float = 2, particle_amount: int = 10, dimensions: int = 3, iterations: int = 20) -> None:
        self.__cognitive_coefficient: float = cognitive_coefficient
        self.__dimensions: int = dimensions
        self.__inertia_coefficient: float = inertia_coefficient
        self.__iterations: int = iterations
        self.__particle_amount: int = particle_amount
        self.__social_coefficient: float = social_coefficient
        # * So it doesn't create two particle swarms with different dimensions
        self.__swarm: ParticleSwarm = None

    def graph_heuristic(self) -> None:
        pass

    def graph_particles(self) -> None:
        pass
    
    def heuristic(self, position: Position, selection: int = "3") -> float:
        """Heuristic function to be optimized."""
        # TODO: Make a better implementation of choosing the desired function, at the moment it's done manually, by modifying the variable selection through the parameters
        # TODO: Implement the second function to the dimension that the user selects. It is set to two dimensions. ? A dimension parameter in the heuristic ? 
        # * Agree, but what should be then the type of the heuristic_value? A list or maybe an ndarray?
        
        if selection == "1":
            return np.sum(np.square(position.get_coordinates()))
        
        elif selection == "2":
            return 20 + np.sum(np.square(position.get_coordinates()) - 10*math.cos(2 * math.pi *position.get_coordinates()))
        
        elif selection == "3":
            x = position.get_coordinates()[0]
            y = position.get_coordinates()[1]
            return((1 + (x+y+1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36*x*y + 27 * y**2)))
        
        elif selection == "4":
            x = position.get_coordinates()[0]
            y = position.get_coordinates()[1]
            return (x + 2*y - 7)**2 + (2*x + y - 5)**2
        
        else:
            print(np.sum(np.square(position.get_coordinates())))
            return np.sum(np.square(position.get_coordinates()))
        
    def optimize(self) -> None:
        """Optimizes the heuristic function using the PSO algorithm."""
        self.__swarm = ParticleSwarm(self.__inertia_coefficient, self.__cognitive_coefficient, self.__social_coefficient, self.__dimensions, self.__particle_amount, self.heuristic)
        self.__swarm._initialize_particles_randomly()
        self.__swarm.update_gbest()

        for _ in range(self.__iterations):
            for particle in self.__swarm.get_particles():    
                particle.get_velocity()._update(self.__inertia_coefficient, self.__cognitive_coefficient, self.__social_coefficient, particle.get_position().get_coordinates().copy(), particle.get_pbest().get_coordinates().copy(), self.__swarm.get_gbest().get_coordinates().copy())

                particle.get_position()._update(particle.get_velocity())
                particle.get_heuristic()._update(particle.get_position())
                particle._update_pbest()
                print(particle, end="")
            self.__swarm.update_gbest()
            print(f"Global best: {self.__swarm.get_gbest()}\n")

    # * Getters
    # ! -they might not be needed though
    def get_cognitive_coefficient(self) -> float:
        return self.__cognitive_coefficient

    def get_dimensions(self) -> int:
        return self.__dimensions

    def get_inertia_coefficient(self) -> float:
        return self.__inertia_coefficient

    def get_iterations(self) -> int:
        return self.__iterations

    def get_particle_amount(self) -> int:
        return self.__particle_amount

    def get_social_coefficient(self) -> float:
        return self.__social_coefficient

    def get_swarm(self) -> ParticleSwarm:
        return self.__swarm

def run():
    pass

if __name__ == "__main__":
    main = Main(2, 0.8, 2, 15, 3, 50)
    main.optimize()
    print(main.get_swarm().get_gbest())
