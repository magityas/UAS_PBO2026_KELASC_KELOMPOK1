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
    
class Croissant(ProduksiRoti):
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
            
class Butter(Croissant):
    pass

class Almond(Croissant):
    pass

class Coklat(Croissant):
    pass

class PabrikRoti:
    @staticmethod
    def buat_varian(jenis, nama, kode, bahan, biaya, harga):
        if jenis == "butter":
            return Butter(nama, kode, bahan, biaya, harga)
        elif jenis == "almond":
            return Almond(nama, kode, bahan, biaya, harga)
        elif jenis == "coklat":
            return Coklat(nama, kode, bahan, biaya, harga)
        else:
            raise ValueError("Varian tidak tersedia")
