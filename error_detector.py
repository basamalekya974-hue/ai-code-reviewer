import ast

class ErrorFinder(ast.NodeVisitor):
    def __init__(self):
        self.defined_vars = set()
        self.used_vars = set()
        self.errors = []

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined_vars.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_vars.add(node.id)
        self.generic_visit(node)

    def find_unused_variables(self):
        unused = self.defined_vars - self.used_vars
        for var in unused:
            self.errors.append({
                "type": "UnusedVariable",
                "message": f"Variable '{var}' is never used",
                "severity": "Warning"
            })
        return self.errors
      
def detect_errors(code_string):
    tree = ast.parse(code_string)
    finder = ErrorFinder()
    finder.visit(tree)
    return finder.find_unused_variables()
