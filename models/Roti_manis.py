from abc import ABC, abstractmethod

class BahanBaku:
    def __init__(self, nama, jumlah):
        self.__nama = nama
        self.__jumlah = jumlah
        
    @property
    def nama(self):
        return self.__nama
    
    @property
    def jumlah(self):
        return self.__jumlah
    
    def __str__(self):
        return f"{self.__nama} : {self.__jumlah}"
    
class ProsesProduksi(ABC):
    @abstractmethod
    def jalankan(self):
        pass
    
class Pengadonan(ProsesProduksi):
    def jalankan(self):
        print("-> Melakukan proses pengadonan")
        
class Pengembangan(ProsesProduksi):
    def jalankan(self):
        print("-> Melakuan proses pengembangan adonan")
        
class Pemanggangan(ProsesProduksi):
    def jalankan(self):
        print("-> Melakukan proses pemamnggangan adonan")
        
class ProduksiRoti(ABC):
    def __init__(self, nama, kode, bahan, biaya, harga):
        self.__nama = nama
        self.__kode = kode
        self.__bahan = bahan
        self.__biaya = biaya
        self.__harga = harga
      
    @property
    def nama(self):
        return self.__nama
      
    @property
    def kode(self):
        return self.__kode
    
    @property
    def bahan(self):
        return self.__bahan
    
    @property
    def biaya(self):
        return self.__biaya

    @property
    def harga(self):
        return self.__harga

    @abstractmethod
    def proses_produksi(self):
        pass
    
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
   
nama = input("Masukan nama varian: ")
kode = input("Masukan kode produk: ")

jumlah_bahan = int(input("Jumlah bahan: "))
bahan = []

for i in range(jumlah_bahan):
    print(f"\nBahan ke-{i+1}")
    nama_bahan = input("Nama bahan: ")
    jumlah = input("Jumlah: ")
    bahan.append(BahanBaku(nama_bahan, jumlah))
    
biaya = int(input("Biaya produksi: "))
harga = int(input("Harga jual: "))

produk = PabrikRoti.buat_varian(
    nama,
    kode,
    bahan,
    biaya,
    harga
)
