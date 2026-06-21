class ASTNode: pass
class VarDecl(ASTNode):
    def __init__(self, name, expr): self.name, self.expr = name, expr
class Print(ASTNode):
    def __init__(self, name): self.name = name
class BinOp(ASTNode):
    def __init__(self, op, left, right): self.op, self.left, self.right = op, left, right
class Num(ASTNode):
    def __init__(self, val): self.val = val
class Var(ASTNode):
    def __init__(self, name): self.name = name

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def consume(self, expected_kind):
        if self.current()[0] == expected_kind:
            val = self.current()[1]
            self.pos += 1
            return val
        raise Exception(f"Sintaks Error: Diharapkan {expected_kind}, tapi mendapat {self.current()[0]}")

    def parse_program(self):
        statements = []
        while self.current()[0] != 'EOF':
            if self.current()[0] == 'VAR':
                self.consume('VAR')
                name = self.consume('ID')
                self.consume('ASSIGN')
                expr = self.parse_expr()
                self.consume('SEMI')
                statements.append(VarDecl(name, expr))
            elif self.current()[0] == 'PRINT':
                self.consume('PRINT')
                self.consume('LPAREN')
                name = self.consume('ID')
                self.consume('RPAREN')
                self.consume('SEMI')
                statements.append(Print(name))
            else:
                raise Exception(f"Sintaks Error: Perintah tidak dikenali '{self.current()[1]}'")
        return statements

    def parse_expr(self):
        node = self.parse_term()
        while self.current()[0] in ('PLUS', 'MINUS'):
            op = self.consume(self.current()[0])
            node = BinOp(op, node, self.parse_term())
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current()[0] in ('MUL', 'DIV'):
            op = self.consume(self.current()[0])
            node = BinOp(op, node, self.parse_factor())
        return node

    def parse_factor(self):
        if self.current()[0] == 'NUM':
            return Num(int(self.consume('NUM')))
        elif self.current()[0] == 'ID':
            return Var(self.consume('ID'))
        elif self.current()[0] == 'LPAREN':
            self.consume('LPAREN')
            node = self.parse_expr()
            self.consume('RPAREN')
            return node
        raise Exception(f"Sintaks Error: Faktor tidak valid '{self.current()[1]}'")