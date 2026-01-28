def suggest_code(code_string):
    suggestions = []

    if "print(" in code_string:
        suggestions.append(
            "Consider using logging instead of print statements for better practice."
        )

    if len(code_string.splitlines()) > 20:
        suggestions.append(
            "Consider breaking the code into smaller functions for better readability."
        )

    if not suggestions:
        suggestions.append("No major issues detected. Good job!")

    return suggestions
