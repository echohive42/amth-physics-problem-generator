import random
from termcolor import termcolor
import os
from datetime import datetime, timedelta

# Constants
COMPLEXITY_LEVELS = {
    1: "Basic investment calculations",
    2: "Intermediate compound interest problems",
    3: "Advanced portfolio optimization"
}

INVESTMENT_TYPES = ["stocks", "bonds", "mutual funds", "real estate"]
TIMEFRAMES = ["months", "years", "quarters"]
INTEREST_RATES = [0.03, 0.05, 0.07, 0.10, 0.15]

def generate_basic_problem():
    """Generate a basic investment problem"""
    try:
        print(termcolor.colored("Generating basic investment problem...", "cyan"))
        
        initial_investment = random.randint(1000, 10000)
        rate = random.choice(INTEREST_RATES)
        time = random.randint(1, 5)
        
        # Calculate solution
        final_amount = initial_investment * (1 + rate) ** time
        
        problem_text = f"""Investment Problem (Complexity Level: Basic)
        
An investor starts with ${initial_investment:,} and invests it for {time} years with an annual return rate of {rate*100}%.
Assuming the interest is compounded annually, how much will the investment be worth at the end of the period?

Answer: ${final_amount:,.2f}
"""
        solution_code = f"""# Python Solution:
initial_investment = {initial_investment}
rate = {rate}
time = {time}
final_amount = initial_investment * (1 + rate) ** time
print(f"Final amount: ${final_amount:,.2f}")
"""
        return problem_text, solution_code, final_amount
    except Exception as e:
        print(termcolor.colored(f"Error generating basic problem: {str(e)}", "red"))
        return None, None, None

def generate_intermediate_problem():
    """Generate an intermediate investment problem"""
    try:
        print(termcolor.colored("Generating intermediate investment problem...", "cyan"))
        
        initial_investment = random.randint(10000, 50000)
        monthly_contribution = random.randint(500, 2000)
        rate = random.choice(INTEREST_RATES)
        years = random.randint(5, 15)
        
        # Calculate solution
        total = initial_investment
        for _ in range(years * 12):
            total = total * (1 + rate/12) + monthly_contribution
            
        problem_text = f"""Investment Problem (Complexity Level: Intermediate)
        
An investor begins with ${initial_investment:,} and plans to contribute ${monthly_contribution} monthly for {years} years.
The annual return rate is {rate*100}%, compounded monthly. What will be the total value of the investment after {years} years?

Answer: ${total:,.2f}
"""
        solution_code = f"""# Python Solution:
initial_investment = {initial_investment}
monthly_contribution = {monthly_contribution}
rate = {rate}
years = {years}

total = initial_investment
for _ in range(years * 12):
    total = total * (1 + rate/12) + monthly_contribution
print(f"Total value: ${total:,.2f}")
"""
        return problem_text, solution_code, total
    except Exception as e:
        print(termcolor.colored(f"Error generating intermediate problem: {str(e)}", "red"))
        return None, None, None

def generate_advanced_problem():
    """Generate an advanced investment problem"""
    try:
        print(termcolor.colored("Generating advanced investment problem...", "cyan"))
        
        portfolio_value = random.randint(100000, 500000)
        num_assets = random.randint(3, 5)
        assets = random.sample(INVESTMENT_TYPES, num_assets)
        returns = [round(random.uniform(0.05, 0.20), 3) for _ in range(num_assets)]
        risks = [round(random.uniform(0.10, 0.30), 3) for _ in range(num_assets)]
        
        # Calculate optimal portfolio weights using a simplified approach
        total_return = sum(returns)
        weights = [round(r/total_return, 3) for r in returns]
        
        # Calculate expected portfolio return and risk
        portfolio_return = sum(w * r for w, r in zip(weights, returns))
        
        problem_text = f"""Investment Problem (Complexity Level: Advanced)

An investor has ${portfolio_value:,} to allocate across {num_assets} different assets: {', '.join(assets)}.
The expected annual returns for these assets are {', '.join([f'{r*100}%' for r in returns])} respectively.
The risk levels (standard deviation) are {', '.join([f'{r*100}%' for r in risks])} respectively.
Calculate the optimal portfolio allocation weights to maximize the return while considering risk.

Optimal Portfolio Allocation:
"""
        for asset, weight in zip(assets, weights):
            problem_text += f"{asset}: {weight*100:.1f}%\n"
        
        problem_text += f"\nExpected Portfolio Return: {portfolio_return*100:.2f}%"

        solution_code = f"""# Python Solution:
portfolio_value = {portfolio_value}
assets = {assets}
returns = {returns}
risks = {risks}

# Calculate weights based on return contribution
total_return = sum(returns)
weights = [round(r/total_return, 3) for r in returns]

# Calculate expected portfolio return
portfolio_return = sum(w * r for w, r in zip(weights, returns))

print("Optimal Portfolio Allocation:")
        for asset, weight in zip(assets, weights):
    print(f"{asset}: {weight*100:.1f}%")
print(f"\\nExpected Portfolio Return: {portfolio_return*100:.2f}%")
"""
        return problem_text, solution_code, weights
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
        print(termcolor.colored("Saving problem to investment_problem.txt...", "yellow"))
        with open("investment_problem.txt", "w", encoding="utf-8") as f:
            f.write(problem_text)
        
        # Save solution code
        print(termcolor.colored("Saving solution to investment_solution.py...", "yellow"))
        with open("investment_solution.py", "w", encoding="utf-8") as f:
            f.write(solution_code)
            
        print(termcolor.colored("Files saved successfully!", "green"))
    except Exception as e:
        print(termcolor.colored(f"Error saving to files: {str(e)}", "red"))

def main():
    try:
        print(termcolor.colored("Investment Math Problem Generator", "cyan"))
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