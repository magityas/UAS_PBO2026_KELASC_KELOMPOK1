from typing import Any, Dict, List

class BahanBakuService:
    def hitung_rasio_produksi(self, produk: Any, jumlah_pcs: int) -> float:
        if jumlah_pcs <= 0:
            raise ValueError("Jumlah pcs harus lebih dari 0.")
        
        jumlah_pcs_resep = getattr(produk, "Jumlah_pcs_resep", 1)
        return jumlah_pcs / jumlah_pcs_resep
    
    def hitung_kebutuhan_bahan(self, produk: Any, jumlah_pcs: int) -> List[Dict[str, float]]:
        rasio = self.hitung_rasio_produksi(produk, jumlah_pcs)
        return [
            { "nama": bahan.nama, "jumlah": bahan.jumlah * rasio }
            for bahan in produk.bahan
        ]