from abc import ABC, abstractmethod
from models.Croissant import ProduksiRoti, Pengadonan, Pengembangan, Pemanggangan

class Rotimanis(ProduksiRoti):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)
        self.proses = [
            Pengadonan(),
            Pengembangan(),
            Pemanggangan()
        ]
        
    def proses_produksi(self):
        print(f"\n=== Produksi {self.nama} ===")
        for p in self.proses:
            p.jalankan()
            
class PabrikRoti:
    @staticmethod
    def buat_varian(nama, kode, bahan, biaya, harga):
        return Rotimanis(nama, kode, bahan, biaya, harga)
