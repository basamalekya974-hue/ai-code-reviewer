import logging
import random

def suggest_code(code_string):
    pool = []
    improved_code = code_string

    lines = code_string.splitlines()

    # Print → logging
    if any("print(" in line for line in lines):
        pool.append("Replace print statements with logging for better practice.")
        pool.append("Avoid using print in production-level code.")
        improved_code = improved_code.replace("print(", "logging.info(")

    # Unused variables
    pool.append("Remove unused variables to improve code clarity.")
    pool.append("Clean up unused variables for better maintainability.")

    # Structure
    if "def " not in code_string:
        pool.append("Organize the code into functions.")
        pool.append("Refactor code into reusable functions.")

    if not pool:
        pool.append("Code looks clean. No major improvements suggested.")

    # 🔥 THIS IS THE KEY PART
    # Randomly choose 1–3 suggestions every run
    num = random.randint(1, min(3, len(pool)))
    suggestions = random.sample(pool, num)

    return {
        "suggestions": suggestions,
        "improved_code": improved_code
    }



















