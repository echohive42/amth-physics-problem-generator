# Math Problem Generators

A collection of Python scripts that generate mathematical problems with varying complexity levels. These tools are designed to create problems that can be used to test the accuracy of large language models or for educational purposes.

## Available Generators

1. Investment Math Problem Generator (`math_problem_generator.py`)
2. Physics Problem Generator (`physics_problem_generator.py`)

 ## 🎥 Watch How It's Built!

**[Watch the complete build process on Patreon](https://www.patreon.com/posts/how-to-build-and-120084275)** - This tutorial is part of the comprehensive 1000x Cursor Course!

See exactly how the files in this tutorial was created step by step, with detailed explanations and insights into the development process. Learn advanced techniques for building AI applications while mastering the Cursor Code Editor.

## ❤️ Support & Get 400+ AI Projects

This is one of 400+ fascinating projects in my collection! [Support me on Patreon](https://www.patreon.com/c/echohive42/membership) to get:

- 🎯 Access to 400+ AI projects (and growing daily!)
- 📥 Full source code & detailed explanations
- 📚 1000x Cursor Course (32 chapters, 21+ hours of comprehensive content for mastering the Cursor Code Editor)
- 🎓 Live coding sessions & AMAs
- 💬 1-on-1 consultations (higher tiers)
- 🎁 Exclusive discounts on AI tools & platforms (up to $180 value)

## Features

- Three complexity levels for each generator
- Automatic generation of:
  - Clear problem statements
  - Python solution code
  - Calculated answers
- Color-coded terminal output for better user experience
- Error handling with informative messages
- UTF-8 encoding support

## Requirements

```bash
pip install -r requirements.txt
```

## Investment Problem Generator

### Usage

1. Run the script:

```bash
python math_problem_generator.py
```

2. Choose a complexity level (1-3)
3. The script will generate:

   - `investment_problem.txt`: Contains the problem statement and answer
   - `investment_solution.py`: Contains the Python code to solve the problem

### Problem Types

#### Basic Level

- Simple compound interest calculations
- Initial investment with fixed interest rate
- Annual compounding

Example:

```
An investor starts with $5,000 and invests it for 3 years with an annual return rate of 7%.
```

#### Intermediate Level

- Monthly contribution problems
- Compound interest with regular deposits
- Monthly compounding

Example:

```
An investor begins with $10,000 and plans to contribute $500 monthly for 5 years.
The annual return rate is 8%, compounded monthly.
```

#### Advanced Level

- Portfolio optimization problems
- Multiple asset types (stocks, bonds, mutual funds, real estate)
- Risk and return calculations
- Asset allocation strategies

Example:

```
An investor has $100,000 to allocate across 4 different assets with varying returns and risks.
```

## Physics Problem Generator

### Usage

1. Run the script:

```bash
python physics_problem_generator.py
```

2. Choose a complexity level (1-3)
3. The script will generate:

   - `physics_problem.txt`: Contains the problem statement and answer
   - `physics_solution.py`: Contains the Python code to solve the problem

### Problem Types

#### Basic Level - Mechanics

- Projectile motion problems
- Calculations include:
  - Time of flight
  - Maximum height
  - Horizontal range

Example:

```
A ball is launched with an initial velocity of 20 m/s at an angle of 45 degrees from the horizontal.
```

#### Intermediate Level - Thermodynamics

- Heat transfer problems
- Multiple materials (water, aluminum, iron, copper)
- Calculations include:
  - Energy required for temperature change
  - Average power input

Example:

```
A 5 kg block of aluminum is heated from 25°C to 75°C over a period of 5 minutes.
```

#### Advanced Level - Wave Motion

- Sound wave problems
- Calculations include:
  - Wavelength
  - Period of oscillation
  - Phase difference

Example:

```
A sound wave with frequency 1000 Hz and amplitude 0.005 meters travels through air.
```

## Constants and Units

### Physics Constants

- Gravitational acceleration: 9.81 m/s²
- Speed of sound in air: 343 m/s
- Specific heat capacities:
  - Water: 4186 J/kg·K
  - Aluminum: 900 J/kg·K
  - Iron: 450 J/kg·K
  - Copper: 385 J/kg·K

### Investment Constants

- Interest rates: 3% to 15%
- Investment types: stocks, bonds, mutual funds, real estate

## Error Handling

Both scripts include comprehensive error handling for:

- Invalid input validation
- File writing operations
- Calculation errors
- Mathematical domain errors
