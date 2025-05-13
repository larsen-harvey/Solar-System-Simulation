from PIL import Image
import numpy as np

def load_texture(texture_path):
    """
    Load and normalize a texture image.

    Parameters:
    texture_path (str): The path to the texture image file.

    Returns:
    numpy.ndarray: The normalized image array or None if the file is not found.
    """
    texture_path (img)
    try:
        img = Image.open(texture_path)
        img = img.resize((50, 25))  # Resize for consistency
        return np.array(img) / 255  # Normalize pixel values
    except FileNotFoundError:
        print(f"Texture file {texture_path} not found.")
        return None

def calculate_gravitational_force(m1, m2, distance):
    """
    Calculate the gravitational force between two masses.

    Parameters:
    m1 (float): The mass of the first object in kilograms.
    m2 (float): The mass of the second object in kilograms.
    distance (float): The distance between the two objects in meters.

    Returns:
    float: The gravitational force in newtons.
    """
    from math import sqrt

    if distance == 0:
        return 0  # Avoid division by zero
    G = 6.67430e-11  # Gravitational constant
    return G * (m1 * m2) / (distance ** 2)

def normalize_vector(vector):
    """
    Normalize a vector.

    Parameters:
    vector (numpy.ndarray): The vector to normalize.

    Returns:
    numpy.ndarray: The normalized vector.
    """
    from numpy.linalg import norm

    magnitude = norm(vector)
    if magnitude == 0:
        return vector
    return vector / magnitude