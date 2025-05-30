from utils import load_texture
from planet import Planet

class Moon(Planet):
    """
    Represents a moon orbiting a planet in the solar system.

    Inherits from the Planet class and adds a reference to the parent planet.

    Parameters:
    name (str): The name of the moon.
    mass (float): The mass of the moon in kilograms.
    radius (float): The radius of the moon in kilometers.
    semi_major_axis (float): The semi-major axis of the moon's orbit in kilometers.
    eccentricity (float): The eccentricity of the moon's orbit.
    inclination (float): The inclination of the moon's orbit in radians.
    longitude_of_ascending_node (float): The longitude of the ascending node in radians.
    argument_of_periapsis (float): The argument of periapsis in radians.
    parent_planet (str): The name of the parent planet.
    mean_anomaly (float): The mean anomaly of the moon in radians.
    texture (str): The path to the texture image for the moon.
    """
    def __init__(self, name, mass, radius, semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, parent_planet, mean_anomaly=0, texture_path="self.texture"):
        super().__init__(name, mass, radius, semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, mean_anomaly, texture_path)
        self.parent_planet = parent_planet

    def __post_init__(self):
        """
        Load the texture image during initialization if a texture path is provided.
        """
        if self.texture:
            self.texture = load_texture(self.texture)
