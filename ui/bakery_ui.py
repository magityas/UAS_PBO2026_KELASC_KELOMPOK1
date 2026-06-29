from services.produk_services import ProdukService
from services.profit_services import ProfitService
from services.produksi_services import ProduksiService

class BakeryUI:
    def __init__(self):
        self.produk_service = ProdukService()
        self.profit_service = ProfitService()
        self.produksi_service = ProduksiService()

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
        
        jenis = input("Masukkan jenis produk (misal: cookies_original, muffin_coklat, dll): ")
        nama = input("Masukkan nama produk : ")
        kode = input("Masukkan kode produk : ")
        try:
            biaya = float(input("Masukkan biaya produksi : "))
            harga = float(input("Masukkan harga jual : "))
        except ValueError:
            print("Input biaya atau harga tidak valid. Harap masukkan angka.")
            return
        bahan = []

        berhasil = self.produk_service.tambah_produk(kategori, jenis, nama, kode, bahan, biaya, harga)
        if berhasil:
            print("Produk berhasil ditambahkan.")
        else:
            print("Gagal menambahkan produk.")  

    def tampilkan_semua_produk(self):
        daftar_produk = self.produk_service.ambil_semua_produk()

        if len(daftar_produk) == 0:
            print("Belum ada produk yang ditambahkan.")
            return

        print("\n === DAFTAR PRODUK ===")
        for produk in daftar_produk:
            print("-" * 30)
            print(f"Nama Produk     : {produk.nama}")
            print(f"Kode Produk     : {produk.kode}")
            print(f"Biaya Produksi  : RP {produk.biaya}")
            print(f"Harga Jual      : RP {produk.harga}")

    def hapus_produk(self):
        print("\n === HAPUS PRODUK ===")
        kode = input("Masukkan kode produk yang ingin dihapus : ")
        produk = self.produk_service.cari_produk_by_kode(kode)

        if not produk:
            print("Produk tidak ditemukan!")
            return
        
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus produk '{produk.nama}'? (y/n): ")

        if konfirmasi.lower() == "y":
            berhasil = self.produk_service.hapus_produk(kode)
            if berhasil:
                print("Produk berhasil dihapus.")
            else:
                print("Gagal menghapus produk.")
        else:
            print("Penghapusan produk dibatalkan.")

    def estimasi_profit(self):
        print("\n === ESTIMASI PROFIT ===")
        kode = input("Masukkan kode produk untuk estimasi profit : ")
        produk = self.produk_service.cari_produk_by_kode(kode)

        if not produk:
            print("Produk tidak ditemukan!")
            return
        
        try:
            jumlah_pcs = int(input("Masukkan jumlah pcs yang ingin diproduksi : "))

            if jumlah_pcs <= 0:
                print("Jumlah pcs harus lebih dari 0.")
                return
            
        except ValueError:
            print("Input jumlah pcs tidak valid. Harap masukkan angka.")
            return

        hasil = self.profit_service.estimasi_profit(produk, jumlah_pcs)
        print("=== Hasil Estimasi Profit ===")
        print(f"Produk              : {produk.nama}")
        print(f"Jumlah Produksi     : {jumlah_pcs}")
        print(f"Total Biaya Produksi: RP {hasil['total_biaya']}")
        print(f"Total Harga Jual    : RP {hasil['total_harga_jual']}")
        print(f"Estimasi Profit     : RP {hasil['estimasi_profit']}")
        print(f"Margin Profit       : {hasil['margin_persen']:.2f}%")

    def simulasi_produksi(self):
        print("\n === SIMULASI PRODUKSI ===")
        kode = input("Masukkan kode produk untuk simulasi produksi : ")
        produk = self.produk_service.cari_produk_by_kode(kode)

        if not produk:
            print("Produk tidak ditemukan!")
            return

        self.produksi_service.simulasikan_produksi(produk)

    def run(self):
        while True:
            lanjut = self.tampilkan_menu()

            if lanjut == False:
                break
    