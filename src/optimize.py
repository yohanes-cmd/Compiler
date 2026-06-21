from parser import VarDecl, BinOp, Num

def optimize_ast(node):
    if isinstance(node, VarDecl):
        node.expr = optimize_ast(node.expr)
    elif isinstance(node, BinOp):
        # Optimasi cabang kiri dan kanan terlebih dahulu
        node.left = optimize_ast(node.left)
        node.right = optimize_ast(node.right)
        
        # CONSTANT FOLDING: Jika kiri dan kanan sama-sama angka, hitung sekarang!
        if isinstance(node.left, Num) and isinstance(node.right, Num):
            if node.op == '+': return Num(node.left.val + node.right.val)
            if node.op == '-': return Num(node.left.val - node.right.val)
            if node.op == '*': return Num(node.left.val * node.right.val)
            if node.op == '/': return Num(node.left.val // node.right.val)
    return node

def apply_optimization(ast_nodes):
    return [optimize_ast(node) if isinstance(node, VarDecl) else node for node in ast_nodes]