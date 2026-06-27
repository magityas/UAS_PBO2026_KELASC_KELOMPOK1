from models.Croissant import Croissant, PabrikRoti as PabrikCroissant
from models.KueKering import ButterCookies, Muffin, PabrikRoti as PabrikKueKering
from models.Roti_manis import Rotimanis, PabrikRoti as PabrikRotiManis

class ProdukRepository:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        print(f"Produk '{produk.nama}' berhasil ditambahkan.")

    def tampilkan_semua(self):
        if len(self.daftar_produk) == 0:
            print("Belum ada produk yang tersimpan.")
            return

        print("\n=== Daftar Semua Produk ===")
        for i, produk in enumerate(self.daftar_produk):
            print(f"{i + 1}. [{produk.kode}] {produk.nama} - Harga: Rp{produk.harga}")
