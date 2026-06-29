from typing import Any, List

class ProduksiService:
    def simulasikan_produksi(self, produk: Any, daftar_produk: List[Any] = None) -> None:
        if daftar_produk:
            print("\n=== DAFTAR PRODUK YANG TERSEDIA DI SISTEM ===")
            for i, p in enumerate(daftar_produk):
                print(f"{i + 1} [{p.kode}] {p.nama}")
            print("==============================================\n")

        print(f"\n--- Memulai proses produksi untuk produk: {produk.kode} ---")
        produk.proses_produksi()
        print ("--- Proses produksi selesai ---")