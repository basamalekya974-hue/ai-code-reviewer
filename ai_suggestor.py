import logging

def suggest_code(code_string):
    suggestions = []
    improved_code = code_string

    lines = code_string.splitlines()

    # Suggestion: replace print with logging
    if any("print(" in line for line in lines):
        suggestions.append(
            "Replace print statements with logging for better practice."
        )
        improved_code = improved_code.replace(
            "print(", "logging.info("
        )

    # Suggestion: unused variables (generic improvement)
    suggestions.append(
        "Remove unused variables to improve code clarity."
    )

    # Suggestion: function structure
    if "def " not in code_string:
        suggestions.append(
            "Organize the code into functions for better structure."
        )

    if not suggestions:
        suggestions.append("Code looks clean. No major improvements suggested.")

    return {
        "suggestions": suggestions,
        "improved_code": improved_code
    }










