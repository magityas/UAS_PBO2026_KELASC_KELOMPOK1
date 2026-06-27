from models.Croissant import Croissant, PabrikRoti as PabrikCroissant
from models.KueKering import ButterCookies, Muffin, PabrikRoti as PabrikKueKering
from models.Roti_manis import Rotimanis, PabrikRoti as PabrikRotiManis

#Croissant
class CroissantRepository:
    def __init__(self):
        self.daftar_croissant = []

    def tambah(self, jenis, nama, kode, bahan, biaya, harga):
        produk = PabrikCroissant.buat_varian(jenis, nama, kode, bahan, biaya, harga)
        self.daftar_croissant.append(produk)
        print(f"Produk croissant '{nama}' berhasil ditambahkan.")

    def tampilkan_semua(self):
        if len(self.daftar_croissant) == 0:
            print("Belum ada produk croissant.")
            return

        print("\n=== Daftar Croissant ===")
        for i, produk in enumerate(self.daftar_croissant):
            print(f"{i + 1}. [{produk.kode}] {produk.nama} - Harga: Rp{produk.harga}")

    def cari_by_kode(self, kode):
        for produk in self.daftar_croissant:
            if produk.kode == kode:
                return produk
        return None

    def hapus(self, kode):
        produk = self.cari_by_kode(kode)
        if produk != None:
            self.daftar_croissant.remove(produk)
            print(f"Produk '{produk.nama}' berhasil dihapus.")
        else:
            print(f"Produk dengan kode '{kode}' tidak ditemukan.")

#Kue Kering
class KueKeringRepository:
    def __init__(self):
        self.daftar_kuekering = []

    def tambah(self, jenis, nama, kode, bahan, biaya, harga):
        produk = PabrikKueKering.buat_varian(jenis, nama, kode, bahan, biaya, harga)
        self.daftar_kuekering.append(produk)
        print(f"Produk kue kering '{nama}' berhasil ditambahkan.")

    def tampilkan_semua(self):
        if len(self.daftar_kuekering) == 0:
            print("Belum ada produk kue kering.")
            return

        print("\n=== Daftar Kue Kering ===")
        for i, produk in enumerate(self.daftar_kuekering):
            print(f"{i + 1}. [{produk.kode}] {produk.nama} - Harga: Rp{produk.harga}")

    def cari_by_kode(self, kode):
        for produk in self.daftar_kuekering:
            if produk.kode == kode:
                return produk
        return None

    def hapus(self, kode):
        produk = self.cari_by_kode(kode)
        if produk != None:
            self.daftar_kuekering.remove(produk)
            print(f"Produk '{produk.nama}' berhasil dihapus.")
        else:
            print(f"Produk dengan kode '{kode}' tidak ditemukan.")

#Roti Manis
class RotiManisRepository:
    def __init__(self):
        self.daftar_rotimanis = []

    def tambah(self, jenis, nama, kode, bahan, biaya, harga):
        produk = PabrikRotiManis.buat_varian(jenis, nama, kode, bahan, biaya, harga)
        self.daftar_rotimanis.append(produk)
        print(f"Produk roti manis '{nama}' berhasil ditambahkan.")

    def tampilkan_semua(self):
        if len(self.daftar_rotimanis) == 0:
            print("Belum ada produk roti manis.")
            return

        print("\n=== Daftar Roti Manis ===")
        for i, produk in enumerate(self.daftar_rotimanis):
            print(f"{i + 1}. [{produk.kode}] {produk.nama} - Harga: Rp{produk.harga}")

    def cari_by_kode(self, kode):
        for produk in self.daftar_rotimanis:
            if produk.kode == kode:
                return produk
        return None

    def hapus(self, kode):
        produk = self.cari_by_kode(kode)
        if produk != None:
            self.daftar_rotimanis.remove(produk)
            print(f"Produk '{produk.nama}' berhasil dihapus.")
        else:
            print(f"Produk dengan kode '{kode}' tidak ditemukan.")