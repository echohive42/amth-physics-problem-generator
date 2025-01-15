import random
from termcolor import termcolor
import math
import os

# Constants
COMPLEXITY_LEVELS = {
    1: "Basic mechanics problems",
    2: "Intermediate thermodynamics problems",
    3: "Advanced wave motion problems"
}

# Physics constants
GRAVITATIONAL_ACCELERATION = 9.81  # m/s²
SPEED_OF_SOUND = 343  # m/s at room temperature
SPECIFIC_HEAT_CAPACITY = {
    "water": 4186,  # J/kg·K
    "aluminum": 900,
    "iron": 450,
    "copper": 385
}
MATERIALS = list(SPECIFIC_HEAT_CAPACITY.keys())

def generate_basic_problem():
    """Generate a basic physics mechanics problem"""
    try:
        print(termcolor.colored("Generating basic mechanics problem...", "cyan"))
        
        problem_type = random.choice(["projectile", "force", "energy"])
        
        if problem_type == "projectile":
            initial_velocity = random.randint(10, 30)
            angle_degrees = random.randint(30, 60)
            angle_radians = math.radians(angle_degrees)
            
            # Calculate solution
            time_of_flight = 2 * initial_velocity * math.sin(angle_radians) / GRAVITATIONAL_ACCELERATION
            max_height = (initial_velocity * math.sin(angle_radians))**2 / (2 * GRAVITATIONAL_ACCELERATION)
            range_distance = initial_velocity**2 * math.sin(2 * angle_radians) / GRAVITATIONAL_ACCELERATION
            
            problem_text = f"""Physics Problem (Complexity Level: Basic - Projectile Motion)

A ball is launched with an initial velocity of {initial_velocity} m/s at an angle of {angle_degrees} degrees from the horizontal.
Assuming no air resistance, calculate:
1. The time of flight
2. The maximum height reached
3. The horizontal range

Answer:
1. Time of flight: {time_of_flight:.2f} seconds
2. Maximum height: {max_height:.2f} meters
3. Horizontal range: {range_distance:.2f} meters
"""
            solution_code = f"""# Python Solution:
initial_velocity = {initial_velocity}  # m/s
angle_degrees = {angle_degrees}
angle_radians = math.radians(angle_degrees)
g = {GRAVITATIONAL_ACCELERATION}  # m/s²

# Calculate time of flight
time_of_flight = 2 * initial_velocity * math.sin(angle_radians) / g

# Calculate maximum height
max_height = (initial_velocity * math.sin(angle_radians))**2 / (2 * g)

# Calculate range
range_distance = initial_velocity**2 * math.sin(2 * angle_radians) / g

print(f"Time of flight: {time_of_flight:.2f} seconds")
print(f"Maximum height: {max_height:.2f} meters")
print(f"Horizontal range: {range_distance:.2f} meters")
"""
        
        return problem_text, solution_code, (time_of_flight, max_height, range_distance)
    except Exception as e:
        print(termcolor.colored(f"Error generating basic problem: {str(e)}", "red"))
        return None, None, None

def generate_intermediate_problem():
    """Generate an intermediate physics thermodynamics problem"""
    try:
        print(termcolor.colored("Generating intermediate thermodynamics problem...", "cyan"))
        
        material = random.choice(MATERIALS)
        mass = random.randint(1, 10)
        initial_temp = random.randint(20, 30)
        final_temp = random.randint(60, 90)
        time = random.randint(2, 8) * 60  # in seconds
        
        # Calculate solution
        temp_change = final_temp - initial_temp
        energy = mass * SPECIFIC_HEAT_CAPACITY[material] * temp_change
        power = energy / time
        
        problem_text = f"""Physics Problem (Complexity Level: Intermediate - Thermodynamics)

A {mass} kg block of {material} is heated from {initial_temp}°C to {final_temp}°C over a period of {time/60:.0f} minutes.
Calculate:
1. The total energy required for this temperature change
2. The average power input required

Answer:
1. Energy required: {energy:.2f} Joules
2. Average power: {power:.2f} Watts
"""
        solution_code = f"""# Python Solution:
mass = {mass}  # kg
specific_heat = {SPECIFIC_HEAT_CAPACITY[material]}  # J/kg·K
initial_temp = {initial_temp}  # °C
final_temp = {final_temp}  # °C
time = {time}  # seconds

# Calculate temperature change
temp_change = final_temp - initial_temp

# Calculate energy required
energy = mass * specific_heat * temp_change

# Calculate average power
power = energy / time

print(f"Energy required: {energy:.2f} Joules")
print(f"Average power: {power:.2f} Watts")
"""
        return problem_text, solution_code, (energy, power)
    except Exception as e:
        print(termcolor.colored(f"Error generating intermediate problem: {str(e)}", "red"))
        return None, None, None

def generate_advanced_problem():
    """Generate an advanced physics wave motion problem"""
    try:
        print(termcolor.colored("Generating advanced wave problem...", "cyan"))
        
        frequency = random.randint(200, 2000)
        amplitude = round(random.uniform(0.001, 0.01), 3)
        distance = random.randint(5, 20)
        medium_speed = SPEED_OF_SOUND
        
        # Calculate solution
        wavelength = medium_speed / frequency
        period = 1 / frequency
        phase_difference = (2 * math.pi * distance) / wavelength
        
        problem_text = f"""Physics Problem (Complexity Level: Advanced - Wave Motion)

A sound wave with frequency {frequency} Hz and amplitude {amplitude} meters travels through air.
At a distance of {distance} meters from the source:
1. Calculate the wavelength
2. Determine the period of oscillation
3. Find the phase difference relative to the source

Answer:
1. Wavelength: {wavelength:.3f} meters
2. Period: {period:.6f} seconds
3. Phase difference: {phase_difference:.3f} radians
"""
        solution_code = f"""# Python Solution:
frequency = {frequency}  # Hz
amplitude = {amplitude}  # meters
distance = {distance}  # meters
medium_speed = {medium_speed}  # m/s (speed of sound in air)

# Calculate wavelength
wavelength = medium_speed / frequency

# Calculate period
period = 1 / frequency

# Calculate phase difference
phase_difference = (2 * math.pi * distance) / wavelength

print(f"Wavelength: {wavelength:.3f} meters")
print(f"Period: {period:.6f} seconds")
print(f"Phase difference: {phase_difference:.3f} radians")
"""
        return problem_text, solution_code, (wavelength, period, phase_difference)
    except Exception as e:
        print(termcolor.colored(f"Error generating advanced problem: {str(e)}", "red"))
        return None, None, None

def generate_problem(complexity_level):
    """Generate a problem based on complexity level"""
    try:
        print(termcolor.colored(f"Generating problem with complexity level {complexity_level}...", "green"))
        
        if complexity_level == 1:
            return generate_basic_problem()
        elif complexity_level == 2:
            return generate_intermediate_problem()
        elif complexity_level == 3:
            return generate_advanced_problem()
        else:
            raise ValueError("Invalid complexity level. Choose 1, 2, or 3.")
            
    except Exception as e:
        print(termcolor.colored(f"Error in problem generation: {str(e)}", "red"))
        return None, None, None

def save_to_files(problem_text, solution_code):
    """Save the generated problem and solution to separate files"""
    try:
        # Save problem text
        print(termcolor.colored("Saving problem to physics_problem.txt...", "yellow"))
        with open("physics_problem.txt", "w", encoding="utf-8") as f:
            f.write(problem_text)
        
        # Save solution code
        print(termcolor.colored("Saving solution to physics_solution.py...", "yellow"))
        with open("physics_solution.py", "w", encoding="utf-8") as f:
            f.write(solution_code)
            
        print(termcolor.colored("Files saved successfully!", "green"))
    except Exception as e:
        print(termcolor.colored(f"Error saving to files: {str(e)}", "red"))

def main():
    try:
        print(termcolor.colored("Physics Problem Generator", "cyan"))
        print(termcolor.colored("\nAvailable complexity levels:", "yellow"))
        for level, description in COMPLEXITY_LEVELS.items():
            print(f"{level}: {description}")
        
        complexity = int(input("\nEnter complexity level (1-3): "))
        problem_text, solution_code, solution = generate_problem(complexity)
        
        if problem_text and solution_code and solution is not None:
            save_to_files(problem_text, solution_code)
            print(termcolor.colored("\nProblem and solution files generated successfully!", "green"))
        else:
            print(termcolor.colored("Failed to generate problem.", "red"))
            
    except Exception as e:
        print(termcolor.colored(f"Error in main execution: {str(e)}", "red"))

if __name__ == "__main__":
    main() 