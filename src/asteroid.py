from planet import Planet
from utils import load_texture

class Asteroid(Planet):
    """
    Represents an asteroid in the solar system.

    Inherits from the Planet class and represents smaller celestial bodies.

    Parameters:
    name (str): The name of the asteroid.
    mass (float): The mass of the asteroid in kilograms.
    radius (float): The radius of the asteroid in kilometers.
    semi_major_axis (float): The semi-major axis of the asteroid's orbit in AU.
    eccentricity (float): The eccentricity of the asteroid's orbit.
    inclination (float): The inclination of the asteroid's orbit in radians.
    longitude_of_ascending_node (float): The longitude of the ascending node in radians.
    argument_of_periapsis (float): The argument of periapsis in radians.
    mean_anomaly (float): The mean anomaly of the asteroid in radians.
    texture (str): The path to the texture image for the asteroid.
    """
    def __init__(self, name, mass, radius, semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, mean_anomaly=0, texture_path="self.texture"):
        super().__init__(name, mass, radius, semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, mean_anomaly, texture_path)
        self.__post_init__()

    def __post_init__(self):
        """
        Load the texture image during initialization if a texture path is provided.
        """
        if self.texture:
            self.texture = load_texture ("self.texture")