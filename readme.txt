# Compiler Bahasa "SimpleMath" - Kelompok 1

Proyek ini adalah implementasi kompilator (*compiler*) berbasis *Command Line Interface* (CLI) untuk bahasa pemrograman kustom bernama **SimpleMath**. Kompilator ini dibangun menggunakan Python murni tanpa *library* eksternal (seperti PLY/Lex/Yacc), sebagai pemenuhan Tugas Akhir mata kuliah Teknik Kompilator.

Anggota Kelompok 1
1. Yohanes Letare [2455201011]
2. Dalova Keyza [2455201089]
3. Jhoni Cardo 	[2455201051]
4. Melda Wanti 	[2455201009]
5. Alzi Aprian 	[2455201037]
6. Rivaldi Vito [2455201072]



---

## Fitur Kompilator
Kompilator ini memproses kode sumber (*source code*) melalui 5 tahapan utama secara berurutan:
1. **Scanner (Lexical Analyzer):** Membaca teks mentah dan memecahnya menjadi token valid.
2. **Parser (Syntax Analyzer):** Memeriksa aturan tata bahasa (*grammar*) dan merakit *Abstract Syntax Tree* (AST) dengan hierarki matematika yang benar (perkalian dieksekusi lebih dulu dari penjumlahan).
3. **Semantic Analyzer:** Memvalidasi *Symbol Table* (mencegah deklarasi variabel ganda dan mendeteksi pemanggilan variabel yang belum dideklarasikan).
4. **Optimizer:** Menerapkan 2 teknik optimasi yaitu:
   * *Constant Folding:* Menghitung ekspresi konstanta lebih awal (contoh: `10 * 5` otomatis menjadi `50`).
   * *Dead Code Elimination:* Menghapus variabel fiktif/sampah yang dideklarasikan tapi tidak pernah digunakan.
5. **Intermediate Code Generator (ICG):** Menghasilkan *Three Address Code* (TAC) yang siap diterjemahkan ke bahasa mesin.

*(Dilengkapi dengan Error Handling yang informatif di tahap Leksikal, Sintaks, dan Semantik).*

---

## Struktur Direktori
```text
Kelompok_1_SimpleMath/
│
├── src/                  # Kode sumber (Mesin Kompilator)
│   ├── main.py           # File eksekusi utama CLI
│   ├── scanner.py        # Logika Lexical Analyzer
│   ├── parser.py         # Logika Syntax Analyzer & AST
│   ├── semantic.py       # Logika Semantic Analyzer
│   ├── optimize.py       # Logika Optimasi (Folding & DCE)
│   └── icg.py            # Logika pembentukan TAC
│
├── tests/                # Folder bahan pengujian (Test Cases)
│   ├── python src/main.py tests/test1_sukses.src
│   ├── python src/main.py tests/test2_optimasi.src
|   ├── python src/main.py tests/test3_err_leksikal.src
|   ├── python src/main.py tests/test4_err_sintaks.src
|   ├── python src/main.py tests/test5_err_semantik.src
│   └── python src/main.py tests/test1.src
│
└── README.md             # Dokumentasi proyek