import random

def suggest_code(code_string):
    suggestions = []

    lines = code_string.splitlines()

    if any("print(" in line for line in lines):
        suggestions.append(
            "Consider using logging instead of print statements for better debugging."
        )

    if len(lines) > 10:
        suggestions.append(
            "Consider breaking the code into smaller functions for better readability."
        )

    if any(len(word) == 1 for word in code_string.split()):
        suggestions.append(
            "Avoid using single-letter variable names; use descriptive names instead."
        )

    if "def " not in code_string:
        suggestions.append(
            "Organize the code into functions to improve structure."
        )

    if "" in lines:
        suggestions.append(
            "Remove unnecessary blank lines to keep the code clean."
        )

    if not suggestions:
        suggestions.append("Code looks clean. No major improvements suggested.")

    # 🔁 Shuffle suggestions to simulate refresh behavior
    random.shuffle(suggestions)

    return suggestions




