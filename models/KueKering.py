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
        print("-> Melakukan proses pengembangan adonan")

class Pemanggangan(ProsesProduksi):
    def jalankan(self):
        print("-> Melakukan proses pemanggangan adonan")

class Topping(ProsesProduksi):
    def jalankan(self):
        print("-> Melakukan proses pemberian topping")


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
        if jenis == "Butter Cookies":
            return ButterCookies(nama, kode, bahan, biaya, harga)
        elif jenis == "Muffin":
            return Muffin(nama, kode, bahan, biaya, harga)
        else:
            raise ValueError(f"Jenis '{jenis}' tidak tersedia. Pilih 'Butter Cookies' atau 'Muffin'.")


jenis = input("Masukkan jenis kue kering (Butter Cookies/Muffin): ")
nama = input("Masukkan nama produk: ")
kode = input("Masukkan kode produk: ")
jumlah_bahan = int(input("Jumlah bahan: "))
bahan = []

for i in range(jumlah_bahan):
    print(f"\nBahan ke-{i+1}")
    nama_bahan = input("Nama bahan: ")
    jumlah = input("Jumlah: ")
    bahan.append(BahanBaku(nama_bahan, jumlah))

biaya = int(input("Biaya produksi: "))
harga = int(input("Harga jual: "))
produk = PabrikRoti.buat_varian(jenis, nama, kode, bahan, biaya, harga)