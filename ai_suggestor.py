import random

def suggest_code(code_string):
    suggestions = []
    improved_code = code_string

    lines = code_string.splitlines()

    # Suggestion: print -> logging
    if any("print(" in line for line in lines):
        suggestions.append(
            "Replace print statements with logging for better practice."
        )
        improved_code = improved_code.replace(
            "print(", "logging.info("
        )

    # Suggestion: unused variables (generic guidance)
    suggestions.append(
        "Remove unused variables to make the code cleaner."
    )

    # Suggestion: function structure
    if "def " not in code_string:
        suggestions.append(
            "Organize the code into functions for better structure."
        )

    # If no suggestions detected
    if not suggestions:
        suggestions.append("Code looks clean. No major improvements suggested.")

    # Shuffle suggestions for refresh behavior
    random.shuffle(suggestions)

    return suggestions, improved_code








