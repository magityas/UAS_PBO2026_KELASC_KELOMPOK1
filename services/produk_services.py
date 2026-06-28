from typing import Any, List, Optional

try:
    from repository.produk_repository import ProdukRepository
except ImportError:
    ProdukRepository = None


class ProdukService:

    def __init__(self, repository: Optional[ProdukRepository] = None): # type: ignore
        self.repository = repository or (ProdukRepository() if ProdukRepository else None)
    
    def tambah_produk(self, produk: Any) -> bool:
        if self.cari_produk_by_kode(produk.kode) is not None:
            return False
        self.repository.tambah(produk)
        return True
    
    def ambil_semua_produk(self) -> List[Any]:
        """
        buat dipakai di menu "tampilkan semua produk".
        """
        return self.repository.get_semua()
    
    def cari_produk_by_kode(self, kode: str) -> Optional[Any]:
        for produk in self.repository.get_semua():
            if produk.kode == kode:
                return produk
        return None