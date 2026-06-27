from typing import Any, Dict

from .bahan_baku_services import BahanBakuService


class ProfitService:
    def __init__(self, bahan_baku_service: BahanBakuService = None):
        self.bahan_baku_service = bahan_baku_service or BahanBakuService()

    def estimasi_profit(self, produk: Any, jumlah_pcs: int) ->Dict[str, float]:
        rasio = self.bahan_baku_service.hitung_rasio_produksi(produk, jumlah_pcs)
        total_biaya = produk.biaya * rasio
        total_harga_jual = produk.harga * rasio
        estimasi_profit = total_harga_jual - total_biaya
        margin_persen = (estimasi_profit / total_harga_jual * 100) if total_harga_jual > 0 else 0

        return {
            "total_biaya": total_biaya,
            "total_harga_jual": total_harga_jual,
            "estimasi_profit": estimasi_profit,
            "margin_persen": margin_persen
        }