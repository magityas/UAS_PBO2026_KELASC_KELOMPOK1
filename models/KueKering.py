from abc import ABC, abstractmethod
from models.Croissant import BahanBaku, ProduksiRoti, Pengadonan, Pengembangan, Pemanggangan

class Topping(ABC):
    def jalankan(self):
        print("-> Melakukan proses pemberian topping")

class KueKering(ProduksiRoti):
    @abstractmethod
    def proses_produksi(self):
        pass

class ButterCookies(KueKering):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)
        self.proses = [
            Pengadonan(),
            Pemanggangan(),
            Topping()
        ]

    def proses_produksi(self):
        print(f"\n=== Produksi {self.nama} ===")
        for p in self.proses:
            p.jalankan()

class Muffin(KueKering):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)
        self.proses = [
            Pengadonan(),
            Pengembangan(),
            Pemanggangan(),
            Topping()
        ]

    def proses_produksi(self):
        print(f"\n=== Produksi {self.nama} ===")
        for p in self.proses:
            p.jalankan()

class PabrikRoti:
    @staticmethod
    def buat_varian(jenis, nama, kode, bahan, biaya, harga):
        if jenis.lower() in ["butter cookies", "butter"]:
            return ButterCookies(nama, kode, bahan, biaya, harga)
        elif jenis.lower() == "muffin":
            return Muffin(nama, kode, bahan, biaya, harga)
        else:
            raise ValueError(f"Jenis '{jenis}' tidak tersedia. Pilih 'Butter Cookies' atau 'Muffin'.")