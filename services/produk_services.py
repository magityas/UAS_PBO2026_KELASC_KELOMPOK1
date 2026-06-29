from typing import Any, List, Optional
from repository.produk_repository import CroissantRepository, KueKeringRepository, RotiManisRepository

class ProdukService:
    def __init__(self):
        self.repo_croissant = CroissantRepository()
        self.repo_kuekering = KueKeringRepository()
        self.repo_rotimanis = RotiManisRepository()

    def tambah_produk(self, kategori: str, jenis : str, nama: str, kode: str, bahan: list, biaya: float, harga: float) -> bool:
        if self.cari_produk_by_kode(kode) is not None:
            print(f"Produk dengan kode {kode} sudah ada.")
            return False
        
        kategori = kategori.lower()
        if kategori == "croissant":
            return self.repo_croissant.tambah_produk(jenis, nama, kode, bahan, biaya, harga)
        elif kategori == "kue kering":
            return self.repo_kuekering.tambah_produk(jenis, nama, kode, bahan, biaya, harga)
        elif kategori == "roti_manis":
            return self.repo_rotimanis.tambah_produk(jenis, nama, kode, bahan, biaya, harga)
        else:
            print("Gagal: Kategori tidak valid. Pilih 'croissant', kue_kering', atau 'roti_manis'.")
            return False
        
        return True
    
    def ambil_semua_produk(self) -> List[Any]:
        semua_produk = []
        semua_produk.extend(self.repo_croissant.daftar_croissant())
        semua_produk.extend(self.repo_kuekering.daftar_kuekering())
        semua_produk.extend(self.repo_rotimanis.daftar_rotimanis())
        return semua_produk
    
    def cari_produk_by_kode(self, kode: str) -> Optional[Any]:
        produk = self.repo_croissant.cari_kode(kode)
        if produk: return produk
        
        produk = self.repo_kuekering.cari_kode(kode)
        if produk: return produk
        
        produk = self.repo_rotimanis.cari_kode(kode)
        return produk
    
    def hapus_produk_by_kode(self, kode: str) -> bool:
        if self.repo_croissant.cari_kode(kode) is not None:
            self.repo_croissant.hapus(kode)
            return True
        if self.repo_kuekering.cari_kode(kode) is not None:
            self.repo_kuekering.hapus(kode)
            return True
        if self.repo_rotimanis.cari_kode(kode) is not None:
            self.repo_rotimanis.hapus(kode)
            return True
        print(f"Produk dengan kode {kode} tidak ditemukan di kategori manapun.")
        return False