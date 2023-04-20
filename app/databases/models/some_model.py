class loai:
    def __init__(self, ten, link):
        self.ten = ten
        self.link = link

class batdongsan:
    def __init__(self, tieude, gia, diachi, dientich, sdt, sophongngu, mota, nguoidang, anh, id_diachi, id_loai_thue, id_loai_ban):
        self.tieude = tieude
        self.gia = gia
        self.diachi = diachi
        self.dientich = dientich
        self.sdt = sdt
        self.sophongngu = sophongngu
        self.mota = mota
        self.nguoidang = nguoidang
        self.anh = anh
        self.id_diachi = id_diachi
        self.id_loai_thue = id_loai_thue
        self.id_loai_ban = id_loai_ban

def tinh_tp(id,ten):
    def __init__(self,id, ten):
        self.id = id
        self.ten = ten

def quan_huyen(id,ten, id_tinh_tp):
    def __init__(self,id, ten, id_tinh_tp):
        self.id = id
        self.ten = ten
        self.id_tinh_tp = id_tinh_tp

def phuong_xa(id,ten, id_quan_huyen):
    def __init__(self,id, ten, id_quan_huyen):
        self.id = id
        self.ten = ten
        self.id_quan_huyen = id_quan_huyen

def dia_chi(id,ten, id_phuong_xa):
    def __init__(self, ten, id_phuong_xa):
        self.id = id
        self.ten = ten
        self.id_phuong_xa = id_phuong_xa




