from services.produk_services import ProdukService
from services.profit_services import ProfitService
from services.produksi_services import ProduksiService

class BakeryUI:
    def __init__(self):
        self.produk_service = ProdukService()
        self.profit_service = ProfitService()
        self.produksi_service = ProduksiService()

    def format_rupiah(self, angka: float) -> str:
        return f"Rp {angka:,.0f}".replace(",", ".")

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

        while True:
            pilih = input("Pilih kategori produk : ").strip()
            if pilih in ["1", "2", "3"]:
                break
            print("[ERROR] Pilihan kategori wajib diisi dengan angka 1, 2, atau 3!")

        if pilih == "1":
            kategori = "croissant"
        elif pilih == "2":
            kategori = "kue kering"
        elif pilih == "3":
            kategori = "roti_manis"

        if kategori == "kue kering":
            print("\n*Catatan Kue Kering hanya menerima jenis: 'Butter Cookies' atau 'Muffin'")

        while True:
            jenis = input("Masukkan jenis produk: ").strip()
            if jenis:
                break
            print("[ERROR] Jenis produk wajib diisi, tidak boleh kosong!")

        while True:
            nama = input("Masukkan nama produk : ").strip()
            if nama:
                break
            print("[ERROR] Nama produk wajib diisi, tidak boleh kosong!")

        while True:
            kode = input("Masukkan kode produk : ").strip()
            if kode:
                break
            print("[ERROR] Kode produk wajib diisi, tidak boleh kosong!")

        while True:
            try:
                biaya_input = input("Masukkan biaya produksi per-loyang : ").strip()
                if not biaya_input:
                    print("[ERROR] Biaya produksi wajib diisi!")
                    continue
                biaya = float(biaya_input)
                if biaya < 0:
                    print("[ERROR] Biaya produksi tidak boleh minus!")
                    continue
                break
            except ValueError:
                print("[ERROR] Input tidak valid. Harap masukkan angka untuk biaya produksi!")

        while True:
            try:
                harga_input = input("Masukkan harga jual per-pcs : ").strip()
                if not harga_input:
                    print("[ERROR] Harga jual wajib diisi!")
                    continue
                harga = float(harga_input)
                if harga < 0:
                    print("[ERROR] Harga jual tidak boleh minus!")
                    continue
                break
            except ValueError:
                print("[ERROR] Input tidak valid. Harap masukkan angka untuk harga jual!")

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

        while True:
            try:
                jumlah_input = input("Jumlah unit (pcs) yang dipesan konsumen : ").strip()
                if not jumlah_input:
                    print("[ERROR] Jumlah pcs wajib diisi!")
                    continue
                jumlah = int(jumlah_input)
                if jumlah <= 0:
                    print("[ERROR] Jumlah pcs harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("[ERROR] Input tidak valid. Harap masukkan angka bulat untuk jumlah pcs!")

        hasil = self.profit_service.estimasi_profit(produk, jumlah)
        
        print("\n=== Hasil Estimasi Profit ===")
        print(f"Produk                  : {produk.nama}")
        print(f"Jumlah Pesanan          : {jumlah} unit")
        print(f"Loyang yang Dibutuhkan  : {hasil['loyang_dibutuhkan']} loyang (Total produksi: {hasil['total_unit_diproduksi']} unit)")
        print(f"Sisa Roti (Waste)       : {hasil['sisa_roti']} unit")
        print("-" * 45)
        print(f"Total Biaya Produksi    : {self.format_rupiah(hasil['total_biaya'])}")
        print(f"Total Harga Jual        : {self.format_rupiah(hasil['total_harga_jual'])}")
        print(f"Potensi Kerugian Waste  : {self.format_rupiah(hasil['potensi_kerugian'])}")
        print(f"Estimasi Profit Bersih  : {self.format_rupiah(hasil['estimasi_profit'])}")
        print(f"Margin Profit           : {hasil['margin_persen']:.2f}%")

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

        while True:
            try:
                jumlah_bahan_input = input("Berapa jenis bahan baku yang ingin dimasukkan? : ").strip()
                if not jumlah_bahan_input:
                    print("[ERROR] Jumlah jenis bahan baku wajib diisi!")
                    continue
                jumlah_bahan = int(jumlah_bahan_input)
                if jumlah_bahan <= 0:
                    print("[ERROR] Jumlah jenis bahan baku harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("[ERROR] Input tidak valid. Harap masukkan angka bulat untuk jumlah jenis bahan!")

        data_bahan_mentah = []
        for i in range(jumlah_bahan):
            print(f"Bahan ke-{i+1}:")

            while True:
                nama_bahan = input("  Nama barang/bahan baku : ").strip()
                if nama_bahan:
                    break
                print("[ERROR] Nama bahan baku tidak boleh kosong!")

            while True:
                jumlah_input = input("  Jumlah/Takaran (misal: 500gr, 5 butir): ").strip()
                if jumlah_input:
                    break
                print("[ERROR] Jumlah/Takaran tidak boleh kosong!")

            data_bahan_mentah.append({
                "nama": nama_bahan,
                "jumlah": jumlah_input
            })

        self.produksi_service.jalankan_simulasi_lengkap(produk, data_bahan_mentah)

    def run(self):
        while True:
            status = self.tampilkan_menu()
            if not status:
                break