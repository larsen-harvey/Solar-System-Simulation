from utils import load_texture
from dataclasses import dataclass
from PIL import Image
import math

@dataclass
class Planet:
    name: str
    mass: float
    radius: float
    semi_major_axis: float
    eccentricity: float
    inclination: float
    longitude_of_ascending_node: float
    argument_of_periapsis: float
    mean_anomaly: float = 0
    texture_path: str = "self.texture"  # Path to texture image
    x: float = 0  # x position in kilometers
    y: float = 0  # y position in kilometers
    z: float = 0  # z position in kilometers
    vx: float = 0.0  # Velocity in x direction
    vy: float = 0.0  # Velocity in y direction
    vz: float = 0.0  # Velocity in z direction

    AU = 1.496e8  # 1 AU in kilometers

    def calculate_orbital_period(self, sun_mass):
        """
        Calculate the orbital period of the planet.

        Parameters:
        sun_mass (float): The mass of the sun in kilograms.

        Returns:
        float: The orbital period of the planet in seconds.
        """
        T = 2 * math.pi * math.sqrt(self.semi_major_axis ** 3 / (6.67430e-11 * sun_mass))
        return T

    def calculate_position(self, mean_anomaly):
        """
        Calculate the position of the planet in its orbit.

        Parameters:
        mean_anomaly (float): The mean anomaly of the planet in radians.

        Returns:
        tuple: The (x, y, z) coordinates of the planet in kilometers.
        """
        E = mean_anomaly + self.eccentricity * math.sin(mean_anomaly)
        for _ in range(10):
            E_new = mean_anomaly + self.eccentricity * math.sin(E)
            if abs(E - E_new) < 1e-6:
                E = E_new
                break
        x = self.semi_major_axis * (math.cos(E) - self.eccentricity)
        y = self.semi_major_axis * math.sqrt(1 - self.eccentricity**2) * math.sin(E)
        z = self.semi_major_axis * math.sin(self.inclination) * math.sin(E)
        return x, y, z

    def __post_init__(self):
        """
        Load the texture image during initialization if a texture path is provided.
        """
        
        if self.texture:
            self.texture = load_texture("self.texture");