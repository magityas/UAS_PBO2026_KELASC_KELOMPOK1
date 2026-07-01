import math
from typing import Any, Dict
from services.bahan_baku_services import BahanBakuService

class ProfitService:
    def __init__(self, bahan_baku_service: BahanBakuService = None):
        self.bahan_baku_service = bahan_baku_service or BahanBakuService()
        self.kapasitas_per_loyang = 20  # Ketetapan kesepakatan: 1 loyang = 20 unit

    def estimasi_profit(self, produk: Any, jumlah_pcs: int, daftar_produk: list[Any] = None) -> Dict[str, Any]:
        # 1. Hitung jumlah loyang yang dibutuhkan (pembulatan ke atas)
        loyang_dibutuhkan = math.ceil(jumlah_pcs / self.kapasitas_per_loyang)
        total_unit_diproduksi = loyang_dibutuhkan * self.kapasitas_per_loyang
        
        # 2. Hitung sisa roti yang tidak terpakai (waste)
        sisa_roti = total_unit_diproduksi - jumlah_pcs
        
        # 3. Hitung total biaya produksi (produk.biaya dianggap sebagai biaya PER LOYANG)
        total_biaya = loyang_dibutuhkan * produk.biaya
        
        # 4. Hitung total harga jual (produk.harga dianggap sebagai harga jual PER UNIT)
        total_harga_jual = jumlah_pcs * produk.harga
        
        # 5. Hitung potensi kerugian akibat sisa roti yang tidak terjual (waste)
        biaya_per_unit = produk.biaya / self.kapasitas_per_loyang
        potensi_kerugian = sisa_roti * biaya_per_unit
        
        # 6. Hitung profit bersih riil dan margin persentase
        estimasi_profit = total_harga_jual - total_biaya
        margin_persen = (estimasi_profit / total_harga_jual * 100) if total_harga_jual > 0 else 0

        return {
            "loyang_dibutuhkan": loyang_dibutuhkan,
            "total_unit_diproduksi": total_unit_diproduksi,
            "sisa_roti": sisa_roti,
            "total_biaya": total_biaya,
            "total_harga_jual": total_harga_jual,
            "potensi_kerugian": potensi_kerugian,
            "estimasi_profit": estimasi_profit,
            "margin_persen": margin_persen
        }