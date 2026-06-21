import re

# 1. ATURAN TOKEN (Sama seperti rules, mendefinisikan pola regex)
TOKEN_SPEC = [
    ('COMMENT', r'--.*'),             # Mengenali komentar (diawali --)
    ('VAR',     r'\bvar\b'),          # Keyword: var
    ('PRINT',   r'\bprint\b'),        # Keyword: print
    ('ID',      r'[a-zA-Z_]\w*'),     # Nama variabel (huruf/underscore diikuti huruf/angka)
    ('NUM',     r'\d+'),              # Angka (0-9)
    ('ASSIGN',  r'='),                # Operator assignment (=)
    ('PLUS',    r'\+'),               # Operator tambah (+)
    ('MINUS',   r'-'),                # Operator kurang (-)
    ('MUL',     r'\*'),               # Operator kali (*)
    ('DIV',     r'/'),                # Operator bagi (/)
    ('LPAREN',  r'\('),               # Kurung Buka
    ('RPAREN',  r'\)'),               # Kurung Tutup
    ('SEMI',    r';'),                # Titik koma (;)
    ('WS',      r'[ \t\n]+'),         # Spasi, tab, enter (Whitespace)
    ('ERR',     r'.'),                # Karakter tidak dikenal (untuk error handling)
]

# 2. MESIN SCANNER
def tokenize(code):
    tokens = []
    # Menggabungkan semua pola regex di atas menjadi satu pola besar
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    line_num = 1
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        
        # Abaikan spasi dan komentar, tapi hitung baris baru untuk pelacakan error
        if kind == 'WS' or kind == 'COMMENT':
            if '\n' in value:
                line_num += value.count('\n')
            continue
        elif kind == 'ERR':
            raise Exception(f"Leksikal Error: Karakter tidak valid '{value}' di baris {line_num}")
            
        tokens.append((kind, value))
        
    return tokens

# 3. BLOK PENGUJIAN SEMENTARA
if __name__ == "__main__":
    # Ini adalah contoh kode SimpleMath dari panduan ujian
    contoh_kode = """
    var x = 10;
    var y = 5;
    var z = x + y * 2;
    print(z);   -- output: 20
    """
    
    print("Memproses kode:")
    print(contoh_kode)
    print("-" * 30)
    
    try:
        hasil_token = tokenize(contoh_kode)
        print("Daftar Token yang Dihasilkan:")
        for token in hasil_token:
            print(token)
    except Exception as e:
        print(f"Error: {e}")