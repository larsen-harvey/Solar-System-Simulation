import math
from planet import Planet
from asteroid import Asteroid
from moon import Moon
from sun import Sun
from GC import GravitationalConstants

class SolarSystem:
    def __init__(self, sun=None):
        self.planet = []
        self.moons = []
        self.asteroids = []
        if sun is None:
            self.sun = Sun()
        else:
            self.sun = sun
           
    def add_planet(self, Planet):
        # Add a planet to the solar system if it doesn't already exist
        if Planet.name not in [p.name for p in self.planet]:
            self.planet.append(Planet)
        else:
            print(f"Planet {Planet.name} already exists in the solar system.")
    def add_moon(self, moon):
    # Add a moon to the solar system if it doesn't already exist
        if any(planet.name == moon.parent_planet for planet in self.planet):
                self.moons.append(moon)
        else:
            print(f"Parent planet {moon.parent_planet} not found for moon {moon.name}.")
    def add_asteroid(self, asteroid):
        if isinstance(asteroid, Asteroid) and asteroid.name not in [a.name for a in self.asteroids]:
            self.asteroids.append(asteroid)

    def calculate_orbital_characteristics(self, dt,):
        # Calculate the orbital characteristics of each planet
        for i, planet in enumerate(self.planet):
            # Use the inclination directly from the planet's attribute
            inclination = planet.inclination

            # Calculate the eccentric anomaly from the mean anomaly
            eccentric_anomaly = planet.mean_anomaly
            for _ in range(10):  # Iteratively solve Kepler's equation
                eccentric_anomaly = planet.mean_anomaly + planet.eccentricity * math.sin(eccentric_anomaly)

            # Calculate the true anomaly from the eccentric anomaly
            true_anomaly = 2 * math.atan2(
                math.sqrt(1 + planet.eccentricity) * math.sin(eccentric_anomaly / 2),
                math.sqrt(1 - planet.eccentricity) * math.cos(eccentric_anomaly / 2)
            )
            # Calculate the orbital period
            T = (2 * math.pi) * math.sqrt((planet.semi_major_axis ** 3) / (GravitationalConstants.G * self.sun.mass))
            # Update the mean anomaly considering the time step dt
            planet.mean_anomaly = (planet.mean_anomaly + 2 * math.pi * dt / T) % (2 * math.pi)

            # Print the orbital characteristics
            print(f"Planet {i+1}:")
            print(f"Name: {planet.name}")
            print(f"Mass: {planet.mass} kg")
            print(f"Radius: {planet.radius} km")
            print(f"Semi-major Axis: {planet.semi_major_axis} AU")
            print(f"Eccentricity: {planet.eccentricity}")
            print(f"Inclination: {inclination} rad")
            print(f"Longitude of Ascending Node: {planet.longitude_of_ascending_node} rad")
            print(f"Argument of Periapsis: {planet.argument_of_periapsis} rad")
            print(f"Orbital Period: {T / 86400} days")

    def calculate_gravitational_interactions(self, dt):
        positions = {planet.name: [] for planet in self.planet}
        # Calculate the gravitational interactions between planets
        for i, planet1 in enumerate(self.planet):
            force_x, force_y, force_z = 0, 0, 0
            for j, planet2 in enumerate(self.planet):
                if i != j:
                    x1, y1, z1 = planet1.calculate_position(planet1.mean_anomaly)
                    x2, y2, z2 = planet2.calculate_position(planet2.mean_anomaly)
                    r12 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
                    F_g = (GravitationalConstants * planet1.mass * planet2.mass) / (r12 ** 2)
                    force_x += F_g * (x2 - x1) / r12
                    force_y += F_g * (y2 - y1) / r12
                    force_z += F_g * (z2 - z1) / r12

            # Update velocities based on the net force
            planet1.vx += force_x / planet1.mass * dt
            planet1.vy += force_y / planet1.mass * dt
            planet1.vz += force_z / planet1.mass * dt

            # Update positions based on the velocities
            planet1.x += planet1.vx * dt
            planet1.y += planet1.vy * dt
            planet1.z += planet1.vz * dt

            # Print the gravitational interaction
            print(f"Planet {i+1} updated position: ({planet1.x}, {planet1.y}, {planet1.z})")
            positions[planet1.name].append((planet1.x, planet1.y, planet1.z))
        return positions