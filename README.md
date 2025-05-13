Solar System Simulation
This project simulates a solar system, including the sun, planets, moons, and asteroids. It provides a 3D visualization of their orbits and gravitational interactions over time.

Overview
The solar system simulation is designed for educational purposes, allowing users to explore the dynamics of celestial bodies. The simulation runs for a specified number of years and visualizes the results using 3D graphics.

Features
Simulates gravitational interactions between celestial bodies.
Supports planets, moons, and asteroids with realistic orbital mechanics.
Includes texture mapping for celestial bodies.
Provides a 3D animated visualization of the solar system.
Project Structure
solar_system_simulation/
├── src/
│   ├── __init__.py          # Marks the directory as a Python package
│   ├── main.py              # Entry point for the simulation
│   ├── solar_system.py      # Defines the SolarSystem class
│   ├── planet.py            # Defines the Planet class
│   ├── moon.py              # Defines the Moon class
│   ├── asteroid.py          # Defines the Asteroid class
│   ├── utils.py             # Utility functions
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
Setup Instructions
Clone the repository:

git clone <repository-url>
cd solar_system_simulation
Install the required dependencies:

pip install -r requirements.txt
Usage
To run the simulation, execute the main.py file:

python src/main.py
You can modify the number of simulation years in the main.py file to explore different time frames.

Dependencies
This project requires the following Python packages:

matplotlib
numpy
Pillow
License
This project is for educational purposes only. Feel free to use and modify it as needed.
