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
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)

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


class ButterCookiesOriginal(ButterCookies):
    pass

class ButterCookiesCoklat(ButterCookies):
    pass

class ButterCookiesKeju(ButterCookies):
    pass

class PabrikRoti:
    @staticmethod
    def buat_varian(jenis, nama, kode, bahan, biaya, harga):
        if jenis == "cookies_original":
            return ButterCookiesOriginal(nama, kode, bahan, biaya, harga)
        elif jenis == "cookies_coklat":
            return ButterCookiesCoklat(nama, kode, bahan, biaya, harga)
        elif jenis == "cookies_keju":
            return ButterCookiesKeju(nama, kode, bahan, biaya, harga)
        else:
            raise ValueError(f"Varian '{jenis}' tidak tersedia")