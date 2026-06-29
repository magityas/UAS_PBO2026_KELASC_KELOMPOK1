# services/produksi_services.py
import time
import sys
from typing import Any, List, Dict
from models.Croissant import BahanBaku

class ProduksiService:
    def ketik_animasi(self, teks: str, kecepatan: float = 0.03):
        """Fungsi pembantu untuk memunculkan teks huruf demi huruf"""
        for huruf in teks:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            if huruf == '.':
                time.sleep(0.3)
            else:
                time.sleep(kecepatan)
        print()

    def jalankan_simulasi_lengkap(self, produk: Any, data_bahan_mentah: List[Dict[str, str]]) -> None:
        """
        Memproses data bahan baku dari UI, memasukkannya ke objek produk,
        dan menjalankan seluruh rangkaian animasi simulasi produksi.
        """
        list_bahan_baru = []
        for bahan in data_bahan_mentah:
            obj_bahan = BahanBaku(bahan["nama"], bahan["jumlah"])
            list_bahan_baru.append(obj_bahan)

        setattr(produk, "_ProduksiRoti__bahan", list_bahan_baru)

        print("\n[INFO] Barang/Bahan Baku berhasil dimasukkan ke dalam adonan:")
        for b in produk.bahan:
            print(f" - {b.nama} ({b.jumlah})")
        print()

        self.ketik_animasi(f"Mempersiapkan mesin produksi untuk {produk.nama}.....")
        self.ketik_animasi("Mencampur seluruh bahan baku ke dalam wadah adonan.....")
        self.ketik_animasi("Memproses adonan kue sesuai resep rahasia.....")

        self.ketik_animasi(f"\n--- Memulai proses produksi untuk produk: {produk.kode} ---")
        time.sleep(0.5)

        original_print = print
        def custom_print(*args, **kwargs):
            teks_gabung = " ".join(map(str, args))
            if "->" in teks_gabung or "===" in teks_gabung:
                self.ketik_animasi(teks_gabung)
                time.sleep(0.8) # Jeda antar tahapan proses adonan
            else:
                original_print(*args, **kwargs)

        import builtins
        builtins.print = custom_print

        try:
            produk.proses_produksi()
        finally:
            builtins.print = original_print

            self.ketik_animasi("--- Proses produksi selesai ---")
