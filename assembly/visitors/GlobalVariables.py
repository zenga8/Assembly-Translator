import ast
from ..helpers.helper import is_constant_name


class GlobalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all the left hand side of the global (top-level) assignments
    """

    def __init__(self) -> None:
        super().__init__()
        self.results = dict() #tuple of unique identifier given to the variable and value of the variable
        self.num_loops = 0 #keeps track of number of loops
        self.variable_number = 0 #Gives a unique identifier for every variable

    def visit_Assign(self, node):
        if len(node.targets) != 1:
            raise ValueError("Only unary assignments are supported")
        
        name = node.targets[0].id #variable name

        if is_constant_name(name):
            self.variable_number += 1
            self.results[name] = (self.variable_number, node.value.value)
            return

        if name not in self.results:
            self.variable_number += 1
            if type(node.value) == ast.Constant:  # if int value is known
                if self.num_loops == 0: #if it is not inside a while loop
                    self.results[name] = (self.variable_number, node.value.value)
                else:
                    self.results[name] = (self.variable_number, None)
            else:
                self.results[name] = (self.variable_number, None)

    def visit_FunctionDef(self, node):
        """We do not visit function definitions, they are not global by definition"""
        pass

    def visit_While(self, node):
        self.num_loops += 1
        for contents in node.body:
            self.visit(contents)
        self.num_loops -= 1