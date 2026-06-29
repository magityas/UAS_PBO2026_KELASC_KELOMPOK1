from models.Croissant import Croissant, PabrikRoti as PabrikCroissant
from models.KueKering import ButterCookies, Muffin, PabrikRoti as PabrikKueKering
from models.Roti_manis import Rotimanis, PabrikRoti as PabrikRotiManis

_instance_croissant = []
_instance_kuekering = []
_instance_rotimanis = []

class CroissantRepository:
    def __init__(self):
        self.daftar_croissant = _instance_croissant

    def tambah_produk(self, jenis, nama, kode, bahan, biaya, harga):
        produk = PabrikCroissant.buat_varian(nama, kode, bahan, biaya, harga)
        self.daftar_croissant.append(produk)
        print(f"Produk croissant '{nama}' berhasil disimpan di repo.")

    def tampilkan_semua(self):
        return self.daftar_croissant

    def cari_kode(self, kode):
        for produk in self.daftar_croissant:
            if str(produk.kode) == str(kode):
                return produk
        return None

    def hapus(self, kode):
        produk = self.cari_kode(kode)
        if produk is not None:
            self.daftar_croissant.remove(produk)
            print(f"Produk '{produk.nama}' berhasil dihapus.")

class KueKeringRepository:
    def __init__(self):
        self.daftar_kuekering = _instance_kuekering

    def tambah_produk(self, jenis, nama, kode, bahan, biaya, harga):
        produk = PabrikKueKering.buat_varian(jenis, nama, kode, bahan, biaya, harga)
        self.daftar_kuekering.append(produk)
        print(f"Produk kue kering '{nama}' berhasil disimpan di repo.")

    def tampilkan_semua(self):
        return self.daftar_kuekering

    def cari_kode(self, kode):
        for produk in self.daftar_kuekering:
            if str(produk.kode) == str(kode):
                return produk
        return None

    def hapus(self, kode):
        produk = self.cari_kode(kode)
        if produk is not None:
            self.daftar_kuekering.remove(produk)

class RotiManisRepository:
    def __init__(self):
        self.daftar_rotimanis = _instance_rotimanis

    def tambah_produk(self, jenis, nama, kode, bahan, biaya, harga):
        produk = PabrikRotiManis.buat_varian(nama, kode, bahan, biaya, harga)
        self.daftar_rotimanis.append(produk)
        print(f"Produk roti manis '{nama}' berhasil disimpan di repo.")

    def tampilkan_semua(self):
        return self.daftar_rotimanis

    def cari_kode(self, kode):
        for produk in self.daftar_rotimanis:
            if str(produk.kode) == str(kode):
                return produk
        return None

    def hapus(self, kode):
        produk = self.cari_kode(kode)
        if produk is not None:
            self.daftar_rotimanis.remove(produk)
