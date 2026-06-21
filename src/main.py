import sys
import os
from scanner import tokenize
from parser import Parser, VarDecl, Print, Var, BinOp, Num
from semantic import semantic_analysis
from optimize import apply_optimization
from icg import ICG

def tampilkan_ast(nodes):
    print("\n--- VISUALISASI AST ---")
    for node in nodes:
        gambar_cabang(node, 0)
    print("-----------------------\n")

def gambar_cabang(node, level):
    indent = "  " * level
    if isinstance(node, VarDecl):
        print(f"{indent}📦 Deklarasi: {node.name}")
        gambar_cabang(node.expr, level + 1)
    elif isinstance(node, Print):
        print(f"{indent}🖨️ Print: {node.name}")
    elif isinstance(node, BinOp):
        print(f"{indent}⚙️ Operasi: {node.op}")
        gambar_cabang(node.left, level + 1)
        gambar_cabang(node.right, level + 1)
    elif isinstance(node, Num):
        print(f"{indent}🔢 Angka: {node.val}")
    elif isinstance(node, Var):
        print(f"{indent}🔤 Panggil: {node.name}")

if __name__ == "__main__":
    # Mengecek apakah user memasukkan nama file saat menjalankan program
    if len(sys.argv) < 2:
        print("❌ Cara penggunaan: python main.py <jalur_ke_file.src>")
        sys.exit(1)

    filepath = sys.argv[1]
    
    # Mengecek apakah file yang diminta ada
    if not os.path.exists(filepath):
        print(f"❌ ERROR: File '{filepath}' tidak ditemukan!")
        sys.exit(1)

    # Membaca isi file .src
    with open(filepath, 'r') as file:
        source_code = file.read()
    
    print(f"Membaca file: {filepath}\n" + "="*40)
    try:
        # 1. Scanner
        tokens = tokenize(source_code)
        print("✅ [Scanner]  Berhasil membuat token.")
        
        # 2. Parser & AST
        parser = Parser(tokens)
        ast = parser.parse_program()
        print(f"✅ [Parser]   Berhasil membuat AST ({len(ast)} statement).")
        
        # 3. Semantic Analyzer
        semantic_analysis(ast)
        print("✅ [Semantik] Variabel divalidasi.")
        
        # 4. Optimasi
        ast_optimized = apply_optimization(ast)
        print("✅ [Optimasi] Constant Folding & Dead Code Elimination diterapkan.")
        
        tampilkan_ast(ast_optimized)
        
        # 5. ICG / TAC
        icg = ICG()
        tac_code = icg.generate(ast_optimized)
        print("✅ [ICG]      Berhasil menghasilkan Three Address Code (TAC):\n")
        
        for line in tac_code:
            print("     " + line)
            
        print("\n" + "="*40)
        print("🎉 KOMPILASI SELESAI DENGAN SUKSES! 🎉")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")