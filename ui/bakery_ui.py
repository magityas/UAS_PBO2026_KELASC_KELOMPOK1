import time
import sys
from services.produk_services import ProdukService
from services.profit_services import ProfitService
from services.produksi_services import ProduksiService
from models.Croissant import BahanBaku

class BakeryUI:
    def __init__(self):
        self.produk_service = ProdukService()
        self.profit_service = ProfitService()
        self.produksi_service = ProduksiService()

    def format_rupiah(self, angka: float) -> str:
        return f"Rp {angka:,.0f}".replace(",", ".")

    def ketik_animasi(self, teks: str, kecepatan: float = 0.03):
        """Fungsi untuk memunculkan huruf satu per satu dengan efek jeda pada titik-titik"""
        for huruf in teks:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            if huruf == '.':
                time.sleep(0.3)
            else:
                time.sleep(kecepatan)
        print()

    def tampilkan_menu(self):
        print("\n" + "=" * 30)
        print(" SISTEM PRODUKSI BAKERY ")
        print("=" * 30)
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Hapus Produk")
        print("4. Estimasi Profit")
        print("5. Simulasi Produksi")
        print("6. Keluar")
        print("=" * 30)

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            self.tambah_produk()
        elif pilihan == "2":
            self.tampilkan_semua_produk()
        elif pilihan == "3":
            self.hapus_produk()
        elif pilihan == "4":
            self.estimasi_profit()
        elif pilihan == "5":
            self.simulasi_produksi()
        elif pilihan == "6":
            print("Keluar dari program.")
            return False
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        return True

    def tambah_produk(self):
        print("\n === KATEGORI PRODUK ===")
        print("1. Croissant")
        print("2. Kue Kering")
        print("3. Roti Manis")

        pilih = input("Pilih kategori produk : ")
        if pilih == "1":
            kategori = "croissant"
        elif pilih == "2":
            kategori = "kue kering"
        elif pilih == "3":
            kategori = "roti_manis"
        else:
            print("Pilihan kategori tidak valid.")
            return

        print("\n*Catatan Kue Kering hanya menerima jenis: 'Butter Cookies' atau 'Muffin'")
        jenis = input("Masukkan jenis produk: ")
        nama = input("Masukkan nama produk : ")
        kode = input("Masukkan kode produk : ")
        try:
            biaya = float(input("Masukkan biaya produksi : "))
            harga = float(input("Masukkan harga jual : "))
        except ValueError:
            print("[ERROR] Input angka biaya atau harga tidak valid.")
            return

        try:
            berhasil = self.produk_service.tambah_produk(kategori, jenis, nama, kode, [], biaya, harga)
            if berhasil:
                print("[SUCCESS] Produk berhasil disimpan ke memori.")
            else:
                print("[FAILED] Gagal menambahkan produk ke dalam sistem.")
        except ValueError as e:
            print(f"[ERROR] {e}")

    def tampilkan_semua_produk(self):
        daftar = self.produk_service.ambil_semua_produk()
        if not daftar or len(daftar) == 0:
            print("\n[!] Belum ada produk yang tersimpan di dalam sistem.")
            return False

        print(f"\n === DAFTAR PRODUK ({len(daftar)} Terdeteksi) ===")
        for i, produk in enumerate(daftar):
            print("-" * 30)
            print(f"No.             : {i + 1}")
            print(f"Nama Produk     : {produk.nama}")
            print(f"Kode Produk     : {produk.kode}")
            print(f"Biaya Produksi  : {self.format_rupiah(produk.biaya)}")
            print(f"Harga Jual      : {self.format_rupiah(produk.harga)}")
        print("-" * 30)
        return True

    def hapus_produk(self):
        print("\n === HAPUS PRODUK ===")
        if not self.tampilkan_semua_produk():
            return

        kode = input("Masukkan kode produk yang ingin dihapus : ")
        produk = self.produk_service.cari_produk_by_kode(kode)
        if not produk:
            print("Produk tidak ditemukan!")
            return

        konfirmasi = input(f"Apakah Anda yakin ingin menghapus produk '{produk.nama}'? (y/n): ")
        if konfirmasi.lower() == "y":
            if self.produk_service.hapus_produk_by_kode(kode):
                print("Produk sukses dihapus.")
            else:
                print("Produk gagal dihapus.")
        else:
            print("Penghapusan dibatalkan.")

    def estimasi_profit(self):
        print("\n === ESTIMASI PROFIT ===")
        if not self.tampilkan_semua_produk():
            return

        kode = input("Masukkan kode produk untuk estimasi profit : ")
        produk = self.produk_service.cari_produk_by_kode(kode)
        if not produk:
            print("Produk tidak ditemukan!")
            return
        try:
            jumlah = int(input("Jumlah pcs yang ingin diproduksi : "))
            if jumlah <= 0:
                print("Jumlah pcs harus lebih dari 0.")
                return
        except ValueError:
            print("Input jumlah pcs tidak valid.")
            return

        hasil = self.profit_service.estimasi_profit(produk, jumlah)
        print("\n=== Hasil Estimasi Profit ===")
        print(f"Produk              : {produk.nama}")
        print(f"Jumlah Produksi     : {jumlah}")
        print(f"Total Biaya Produksi: {self.format_rupiah(hasil['total_biaya'])}")
        print(f"Total Harga Jual    : {self.format_rupiah(hasil['total_harga_jual'])}")
        print(f"Estimasi Profit     : {self.format_rupiah(hasil['estimasi_profit'])}")
        print(f"Margin Profit       : {hasil['margin_persen']:.2f}%")

    def simulasi_produksi(self):
        print("\n === SIMULASI PRODUKSI ===")
        if not self.tampilkan_semua_produk():
            return

        kode = input("Masukkan kode produk untuk simulasi produksi : ")
        produk = self.produk_service.cari_produk_by_kode(kode)
        if not produk:
            print("Produk tidak ditemukan!")
            return

        print(f"\n--- Input Bahan Baku untuk {produk.nama} ---")
        try:
            jumlah_bahan = int(input("Berapa jenis bahan baku yang ingin dimasukkan? : "))
        except ValueError:
            print("[ERROR] Masukkan jumlah jenis berupa angka.")
            return

        list_bahan_baru = []
        for i in range(jumlah_bahan):
            print(f"Bahan ke-{i+1}:")
            nama_bahan = input("  Nama barang/bahan baku : ")
            jumlah_input = input("  Jumlah/Takaran (misal: 500gr, 5 butir): ")

            obj_bahan = BahanBaku(nama_bahan, jumlah_input)
            list_bahan_baru.append(obj_bahan)

        setattr(produk, "_ProduksiRoti__bahan", list_bahan_baru)

        print("\n[INFO] Barang/Bahan Baku berhasil dimasukkan ke dalam adonan:")
        for b in produk.bahan:
            print(f" - {b.nama} ({b.jumlah})")

        print()
        self.ketik_animasi(f"Mempersiapkan mesin produksi untuk {produk.nama}.....")
        self.ketik_animasi("Mencampur seluruh bahan baku ke dalam wadah adonan.....")
        self.ketik_animasi("Memproses adonan kue sesuai resep rahasia.....")

        self.produksi_service.simulasikan_produksi(produk)

    def run(self):
        while True:
            status = self.tampilkan_menu()
            if not status:
                break
