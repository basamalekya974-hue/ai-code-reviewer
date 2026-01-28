def suggest_code(code_string):
    suggestions = []

    lines = code_string.splitlines()

    # Suggestion 1: print usage
    if any("print(" in line for line in lines):
        suggestions.append(
            "Consider using logging instead of print statements for better debugging and scalability."
        )

    # Suggestion 2: Long code
    if len(lines) > 10:
        suggestions.append(
            "Consider breaking the code into smaller functions to improve readability."
        )

    # Suggestion 3: Variable naming
    if any(len(word) == 1 for word in code_string.split()):
        suggestions.append(
            "Avoid using single-letter variable names; use descriptive names instead."
        )

    # Suggestion 4: Function usage
    if "def " not in code_string:
        suggestions.append(
            "Consider organizing the code into functions for better structure."
        )

    # Suggestion 5: Empty lines check
    if "" in lines:
        suggestions.append(
            "Remove unnecessary blank lines to keep the code clean."
        )

    if not suggestions:
        suggestions.append("Code looks clean. No major improvements suggested.")

    return suggestions


