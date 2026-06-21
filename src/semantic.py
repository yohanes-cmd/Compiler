# Import class ASTNode dari parser
from parser import VarDecl, Print, Var, BinOp

def semantic_analysis(ast_nodes):
    symbol_table = set() # Ini ibarat "database" tempat kita menyimpan nama variabel
    
    for node in ast_nodes:
        if isinstance(node, VarDecl):
            # Cek apakah variabel dideklarasikan ulang (Double Declaration)
            if node.name in symbol_table:
                raise Exception(f"Semantik Error: Variabel '{node.name}' sudah dideklarasikan sebelumnya.")
            
            # Cek ekspresi di sebelah kanan sama dengan (misal: var z = x + y)
            check_expr(node.expr, symbol_table)
            
            # Simpan nama variabel ke dalam Symbol Table
            symbol_table.add(node.name)
            
        elif isinstance(node, Print):
            # Cek apakah variabel yang mau di-print sudah ada di Symbol Table
            if node.name not in symbol_table:
                raise Exception(f"Semantik Error: Variabel '{node.name}' belum dideklarasikan.")

def check_expr(node, symbol_table):
    if isinstance(node, Var):
        # Kalau variabel dipakai di dalam perhitungan matematika, cek apakah sudah ada
        if node.name not in symbol_table:
            raise Exception(f"Semantik Error: Menggunakan variabel '{node.name}' yang belum dideklarasikan.")
    elif isinstance(node, BinOp):
        # Kalau bentuknya operator (tambah/kurang/kali/bagi), cek sisi kiri dan kanannya
        check_expr(node.left, symbol_table)
        check_expr(node.right, symbol_table)