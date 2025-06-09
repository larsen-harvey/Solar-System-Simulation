import math
from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from planet import Planet
from moon import Moon
from asteroid import Asteroid
from solar_system import SolarSystem

def calculate_position(dt, positions):
    system = SolarSystem()

    if not hasattr(system, 'planet') or not isinstance(system.planet, list):
        raise ValueError("SolarSystem object does not have a valid 'planet' attribute.")
    positions = {planet.name: [] for planet in system.planet if hasattr(planet, 'name')}
    for i, planet1 in enumerate(system.planet):
        if not all(hasattr(planet1, attr) for attr in ['x', 'y', 'z']):
            continue  # Skip if planet1 lacks position attributes
        else:
        # Example gravitational interaction calculation
            for i, planet1 in enumerate(system.planet):
                if not all(hasattr(planet1, attr) for attr in ['x', 'y', 'z', 'vx', 'vy', 'vz', 'mass', 'name']):
                    continue  # Skip if planet1 lacks required attributes
            for j, planet2 in enumerate(system.planet):
                if i != j and all(hasattr(planet2, attr) for attr in ['x', 'y', 'z', 'mass']):
                    dx = planet2.x - planet1.x
                    dy = planet2.y - planet1.y
                    dz = planet2.z - planet1.z
                    distance = math.sqrt(dx**2 + dy**2 + dz**2)
                    if distance == 0:
                        continue  # Skip calculation if distance is zero
                    force = (6.67430e-11 * planet1.mass * planet2.mass) / (distance**2)
                    ax = force * dx / distance / planet1.mass
                    ay = force * dy / distance / planet1.mass
                    az = force * dz / distance / planet1.mass
                    planet1.vx += ax * dt
                    planet1.vy += ay * dt
                    planet1.vz += az * dt
            planet1.x += planet1.vx * dt
            planet1.y += planet1.vy * dt
            planet1.z += planet1.vz * dt
            # Print the gravitational interaction
            print(f"Planet {i+1} updated position: ({planet1.x}, {planet1.y}, {planet1.z})")
            positions[planet1.name].append((planet1.x, planet1.y, planet1.z))
            print(f"{positions}")
    return positions            

"""positions[planet1.name].append((planet1.x, planet1.y, planet1.z))
print(f"Planet {i+1}:")
print(f"Name: {planet.name}")
print(f"Mass: {planet.mass} kg")
print(f"Radius: {planet.radius} km")
print(f"Semi-major Axis: {planet.semi_major_axis} AU")
print(f"Eccentricity: {planet.eccentricity}")
print(f"Inclination: {inclination} rad")
print(f"Longitude of Ascending Node: {planet.longitude_of_ascending_node} rad")
print(f"Argument of Periapsis: {planet.argument_of_periapsis} rad")
print(f"Orbital Period: {T / 86400} days"""

def main(simulation_years=15):
    """
    Main function to set up and simulate the solar system.
    It initializes the SolarSystem object, adds planets, moons, and asteroids,
    and then simulates their orbits over time. Finally, it plots the simulation results.

    Parameters:
    simulation_years (int): The number of years to run the simulation.

    Notes:
    The `simulate_and_plot` function returns a `FuncAnimation` object, which can be used to display
    or save the animation. To display the animation, call `plt.show()` after invoking this function.
    To save it, use the `save` method of the `FuncAnimation` object.
    """
    print(f"Running simulation for {simulation_years} years.")
    system = SolarSystem()
    
    # Planets with textures
    system.add_planet(Planet("Mercury", 3.3022e23, 2439.7, 0.387098 * Planet.AU, 0.2056, 0, math.pi/4, math.pi/4, texture_path="textures/mercury.jpg"))
    system.add_planet(Planet("Venus", 4.8695e24, 6051.8, 0.723336 * Planet.AU, 0.0068, math.pi/2, math.pi/4, 3*math.pi/4, texture_path="textures/venus.jpg"))
    system.add_planet(Planet("Earth", 5.972e24, 6371, 1.000 * Planet.AU, 0.0167, 0, 0, 0, texture_path="textures/earthnight.jpg")) # test texture
    system.add_planet(Planet("Mars", 6.4171e23, 3389.5, 1.524 * Planet.AU, 0.0934, 0, 0, 0, texture_path="textures/mars.jpg"))
    system.add_planet(Planet("Jupiter", 1.8982e27, 69911, 5.2044 * Planet.AU, 0.0489, 0, 0, 0, texture_path="textures/jupiter.jpg"))
    system.add_planet(Planet("Saturn", 5.6834e26, 58232, 9.5826 * Planet.AU, 0.0565, 0, 0, 0, texture_path="textures/saturn.jpg"))
    system.add_planet(Planet("Uranus", 8.6810e25, 25362, 19.2184 * Planet.AU, 0.046, 0, 0, 0, texture_path="textures/uranus.jpg"))
    system.add_planet(Planet("Neptune", 1.02413e26, 24622, 30.110387 * Planet.AU, 0.009, 0, 0, 0, texture_path="textures/neptune.jpg"))

    # Dwarf planets with textures
    system.add_planet(Planet("Pluto", 1.303e22, 1188.3, 39.482 * Planet.AU, 0.2488, 17.16, 110.299, 113.834, texture_path="textures/pluto.jpg"))
    system.add_planet(Planet("Haumea", 4.006e21, 816, 43.335 * Planet.AU, 0.191, 28.2, 121.8, 240.6, texture_path="textures/haumea.jpg"))
    system.add_planet(Planet("Makemake", 3.1e21, 715, 45.79 * Planet.AU, 0.159, 29.0, 79.0, 298.0, texture_path="textures/makemake.jpg"))
    system.add_planet(Planet("Eris", 1.66e22, 1163, 67.781 * Planet.AU, 0.44, 44.0, 35.9, 151.0, texture_path="textures/eris.jpg"))
    system.add_planet(Planet("Ceres", 9.393e20, 473, 2.77 * Planet.AU, 0.075, 10.6, 80.3, 73.6, texture_path="textures/ceres.jpg"))

    # Moons with textures
    # Earth
    system.add_moon(Moon("Moon", 7.342e22, 1737.1, 0.00257 * Planet.AU, 0.0549, 5.145, 0, 0, "Earth", texture_path="textures/moon.jpg"))
    # Mars
    system.add_moon(Moon("Phobos", 1.0659e16, 11.267, 9376, 0.0151, 1.093, 0, 0, "Mars", texture_path="textures/phobos.jpg"))
    system.add_moon(Moon("Deimos", 1.4762e15, 6.2, 23463.2, 0.0002, 0.93, 0, 0, "Mars", texture_path="textures/deimos.jpg"))
    # Jupiter
    system.add_moon(Moon("Io", 8.9319e22, 1821.6, 421700, 0.0041, 0.036, 0, 0, "Jupiter", texture_path="textures/io.jpg"))
    system.add_moon(Moon("Europa", 4.7998e22, 1560.8, 671034, 0.009, 0.466, 0, 0, "Jupiter", texture_path="textures/europa.jpg"))
    system.add_moon(Moon("Ganymede", 1.4819e23, 2634.1, 1070412, 0.0013, 0.177, 0, 0, "Jupiter", texture_path="textures/ganymede.jpg"))
    system.add_moon(Moon("Callisto", 1.0759e23, 2410.3, 1882709, 0.0074, 0.192, 0, 0, "Jupiter", texture_path="textures/callisto.jpg"))
    # Saturn
    system.add_moon(Moon("Titan", 1.3452e23, 2574.73, 1221870, 0.0288, 0.34854, 0, 0, "Saturn", texture_path="textures/titan.jpg"))
    system.add_moon(Moon("Rhea", 2.3065e21, 763.8, 527108, 0.001258, 0.345, 0, 0, "Saturn", texture_path="textures/rhea.jpg"))
    system.add_moon(Moon("Iapetus", 1.8056e21, 734.5, 3560820, 0.028612, 15.47, 0, 0, "Saturn", texture_path="textures/iapetus.jpg"))
    system.add_moon(Moon("Mimas", 3.7493e19, 198.2, 185539, 0.0196, 1.574, 0, 0, "Saturn", texture_path="textures/mimas.jpg"))
    system.add_moon(Moon("Enceladus", 1.08022e20, 252.1, 238042, 0.0047, 0.009, 0, 0, "Saturn", texture_path="textures/enceladus.jpg"))
    system.add_moon(Moon("Tethys", 6.17449e20, 531.1, 294619, 0.0001, 1.091, 0, 0, "Saturn", texture_path="textures/tethys.jpg"))
    system.add_moon(Moon("Dione", 1.095452e21, 561.4, 377396, 0.0022, 0.028, 0, 0, "Saturn", texture_path="textures/dione.jpg"))
    system.add_moon(Moon("Hyperion", 5.6e18, 135, 1481000, 0.0232, 0.568, 0, 0, "Saturn", texture_path="textures/hyperion.jpg"))
    system.add_moon(Moon("Phoebe", 8.292e18, 106.5, 12942000, 0.1634, 175.3, 0, 0, "Saturn", texture_path="textures/phoebe.jpg"))
    # Uranus
    system.add_moon(Moon("Titania", 3.527e21, 788.4, 435910, 0.0011, 0.340, 0, 0, "Uranus", texture_path="textures/titania.jpg"))
    system.add_moon(Moon("Oberon", 3.014e21, 761.4, 583520, 0.0014, 0.068, 0, 0, "Uranus", texture_path="textures/oberon.jpg"))
    system.add_moon(Moon("Ariel", 1.353e21, 578.9, 190900, 0.0012, 0.260, 0, 0, "Uranus", texture_path="textures/ariel.jpg"))
    system.add_moon(Moon("Umbriel", 1.172e21, 584.7, 266000, 0.0039, 0.128, 0, 0, "Uranus", texture_path="textures/umbriel.jpg"))
    system.add_moon(Moon("Miranda", 6.59e19, 235.8, 129900, 0.0013, 4.338, 0, 0, "Uranus", texture_path="textures/miranda.jpg"))
    # Neptune
    system.add_moon(Moon("Triton", 2.14e22, 1353.4, 354759, 0.000016, 157.37, 0, 0, "Neptune", texture_path="textures/triton.jpg"))
    system.add_moon(Moon("Nereid", 3.1e19, 170, 5513818, 0.7507, 7.090, 0, 0, "Neptune", texture_path="textures/nereid.jpg"))

    # Asteroids
    system.add_asteroid(Asteroid("Vesta", 2.59076e20, 262.7, 2.362 * Planet.AU, 0.089, 7.14, 103.8, 151.2))
    system.add_asteroid(Asteroid("Pallas", 2.11e20, 273, 2.773 * Planet.AU, 0.231, 34.8, 173, 310))
    system.add_asteroid(Asteroid("Hygiea", 8.67e19, 215, 3.139 * Planet.AU, 0.117, 3.83, 283.2, 312.2))
    system.add_asteroid(Asteroid("Eunomia", 3.12e19, 136, 2.643 * Planet.AU, 0.186, 11.74, 97.8, 293.0))
    system.add_asteroid(Asteroid("Psyche", 2.72e19, 113, 2.922 * Planet.AU, 0.140, 3.10, 150.2, 228.0))
    system.add_asteroid(Asteroid("Juno", 2.67e19, 117, 2.669 * Planet.AU, 0.257, 12.98, 169.8, 248.0))
    system.add_asteroid(Asteroid("Eros", 6.687e15, 16.84, 1.458 * Planet.AU, 0.223, 10.83, 304.3, 178.7))
    system.add_asteroid(Asteroid("Bennu", 7.329e10, 0.245, 1.126 * Planet.AU, 0.203, 6.034, 2.060, 101.703))
    system.add_asteroid(Asteroid("Ryugu", 4.5e11, 0.435, 1.189 * Planet.AU, 0.190, 5.883, 251.47, 211.44))

def simulate_and_plot(system, simulation_years=15):
    """
    Simulate the solar system and plot the results.

    Parameters:
    system (SolarSystem): The solar system to simulate.
    time_steps (int): The number of time steps to simulate.
    dt (float): The time step duration in years.

    Returns:
    FuncAnimation: The animation object.

    Notes:
    The `positions` variable is expected to be a dictionary where the keys are the names of celestial objects (e.g., planets, moons),
    and the values are lists of tuples representing the (x, y, z) coordinates of the objects at each time step.
    For example:
    {
        "Earth": [(x1, y1, z1), (x2, y2, z2), ...],
    # Updates the positions of celestial bodies for each frame in the animation.
    def update(frame):
        ...
    }"""

    dt = 1 / 365  # time step duration in years (1 day)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    time_steps = int(simulation_years * 365)  # Total number of days in the simulation
    

    def update(frame, positions, lines):
        print(f"Updating frame {frame}")  # Debugging output
        for planet_name, line in lines.items():
            if planet_name in positions and frame < len(positions[planet_name]):
                x, y, z = positions[planet_name][frame]
                print(f"Planet {planet_name}: Position ({x}, {y}, {z})")  # Debugging output
                line.set_data([x], [y])
                line.set_3d_properties([z])
            else:
                print(f"Warning: No data for {planet_name} at frame {frame}")
        return lines.values()
    
    # Add a background image
    import os
    texture_path = "textures/astar.jpg"
    if os.path.exists(texture_path):
        background_image = plt.imread(texture_path)  # test texture
    # Removed recursive call to simulate_and_plot to prevent infinite recursion
    else:
        print(f"Warning: Background texture file '{texture_path}' not found.")
    
    # Simulate and plot the solar system
    ani = simulate_and_plot(system, simulation_years)
    ani = FuncAnimation(fig, update, frames=time_steps, blit=False)
    plt.show()  # Ensure the animation is displayed
    return ani
    # Run the simulation and plot the results

if __name__ == "__main__":
    main(simulation_years=15)
    print ("hello world")
