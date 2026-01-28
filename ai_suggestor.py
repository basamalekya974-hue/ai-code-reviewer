import random

def suggest_code(code_string):
    pool = []
    lines = code_string.splitlines()

    # Possible suggestions pool
    if any("print(" in line for line in lines):
        pool.append("Use logging instead of print statements for better debugging.")
        pool.append("Avoid print statements in production-level code.")

    if len(lines) > 10:
        pool.append("Break the code into smaller functions for better readability.")
        pool.append("Large code blocks can be refactored into reusable functions.")

    if any(len(word) == 1 for word in code_string.split()):
        pool.append("Avoid single-letter variable names; use descriptive names.")
        pool.append("Use meaningful variable names to improve code clarity.")

    if "def " not in code_string:
        pool.append("Organize logic into functions for better structure.")

    if "" in lines:
        pool.append("Remove unnecessary blank lines to keep the code clean.")

    if not pool:
        return ["Code looks clean. No major improvements suggested."]

    # 🔁 NEW PART: return RANDOM SUBSET
    num_suggestions = random.randint(1, min(3, len(pool)))
    return random.sample(pool, num_suggestions)






