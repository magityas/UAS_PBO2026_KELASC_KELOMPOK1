# services/produksi_services.py
import time
import sys
from typing import Any, List

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

    def simulasikan_produksi(self, produk: Any, daftar_produk: List[Any] = None) -> None:
        if daftar_produk:
            print("\n=== DAFTAR PRODUK YANG TERSEDIA DI SISTEM ===")
            for i, p in enumerate(daftar_produk):
                print(f"{i + 1} [{p.kode}] {p.nama}")
            print("==============================================\n")

        self.ketik_animasi(f"\n--- Memulai proses produksi untuk produk: {produk.kode} ---")
        time.sleep(0.5) 

        original_print = print

        def custom_print(*args, **kwargs):
            teks_gabung = " ".join(map(str, args))
            if "->" in teks_gabung or "===" in teks_gabung:
                self.ketik_animasi(teks_gabung)
                time.sleep(0.8) 
            else:
                original_print(*args, **kwargs)

        import builtins
        builtins.print = custom_print

        try:
            produk.proses_produksi()
        finally:
            builtins.print = original_print

        self.ketik_animasi("--- Proses produksi selesai ---")
