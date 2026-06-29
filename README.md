# 🥐 Sistem Produksi Bakery (UAS PBO 2026)

Aplikasi **Sistem Produksi Bakery** berbasis Python yang dibuat untuk tugas **UAS Pemrograman Berorientasi Objek 2026**.

Program ini menerapkan konsep **OOP**, **Layered Architecture**, dan pengelolaan produk bakery dengan fitur produksi serta estimasi profit.

---

| NIM | Nama | GitHub | Bagian |
|---|---|---|---|
| K3525028 | Immelda Sekar Mellinda | [@lmmelda](https://github.com/lmmelda) | Models  |
| K3525064 | Maulana Shandy Eka Saputra | [@shandyeka491](https://github.com/shandyeka491) | Models |
| K3525079 | Thiraza Naufal Zhafran Windra | [@zhafraz](https://github.com/zhafraz) | Repository |
| K3525085 | Sabrosa Noval Rachmadhani | [@SabronR](https://github.com/SabronR) | Services |
| K3525075 | Tsalits In'am Illiyyin | [@tsaliy](https://github.com/tsaliy) | UI |
| K3525086 | Maychel Agitya Prasetyo  | [@Magityas](https://github.com/Magityas) | Main Code, Debugging |


---

# 🗂️ Struktur Project

```
UAS_PBO2026_KELASC_KELOMPOK1/

├── main.py
├── models/
│   ├── Croissant.py
│   ├── KueKering.py
│   └── Roti_manis.py
│
├── repository/
│   └── produk_repository.py
│
├── services/
│   ├── produk_services.py
│   ├── produksi_services.py
│   ├── profit_services.py
│   └── bahan_baku_services.py
│
└── ui/
    └── bakery_ui.py
```

---

# ✨ Fitur

- ➕ Tambah produk bakery
- 📋 Menampilkan daftar produk
- ❌ Menghapus produk
- 💰 Menghitung estimasi profit
- 🎬 Simulasi proses produksi
- 🛡️ Validasi input pengguna

Kategori produk:

- 🥐 Croissant
- 🍪 Kue Kering
- 🍞 Roti Manis

---

# 🚀 Cara Menjalankan

Pastikan sudah memiliki:

- Python 3.10+

Clone repository:

```bash
git clone https://github.com/Kudo/UAS_PBO2026_KELASC_KELOMPOK1.git

cd UAS_PBO2026_KELASC_KELOMPOK1
```

Jalankan:

```bash
python main.py
```

---

# 🛠️ Konsep PBO

Konsep yang digunakan:

- **Inheritance** → Pewarisan class produk
- **Polymorphism** → Perbedaan proses produksi tiap produk
- **Encapsulation** → Pengamanan atribut object
- **Singleton Pattern** → Penyimpanan data repository
- **Layered Architecture** → Pemisahan Models, Services, Repository, UI

---

# 📌 Menu Program

```
1. Tambah Produk
2. Tampilkan Semua Produk
3. Hapus Produk
4. Estimasi Profit
5. Simulasi Produksi
6. Keluar
```

---

**UAS Pemrograman Berorientasi Objek 2026**  
Kelompok 1 — Kelas C