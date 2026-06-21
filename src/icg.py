from parser import VarDecl, Print, Var, BinOp, Num

class ICG:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, ast_nodes):
        for node in ast_nodes:
            if isinstance(node, VarDecl):
                res = self.visit_expr(node.expr)
                self.code.append(f"{node.name} = {res}")
            elif isinstance(node, Print):
                self.code.append(f"PRINT {node.name}")
        return self.code

    def visit_expr(self, node):
        if isinstance(node, Num): return str(node.val)
        if isinstance(node, Var): return node.name
        if isinstance(node, BinOp):
            left = self.visit_expr(node.left)
            right = self.visit_expr(node.right)
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {node.op} {right}")
            return temp