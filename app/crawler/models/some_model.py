class loai:
    def __init__(self, ten, link):
        self.id = 0
        self.ten = ten
        self.link = link

class batdongsan:
    tieude = ''
    gia = -1
    diachi = ''
    dientich = -1
    sdt = ''
    sophongngu = -1
    mota = ''
    nguoidang = ''
    sanh = ''
    loai = ''
    def __int__(self):
        self.tieude = ''
        self.gia = -1
        self.diachi = ''
        self.dientich = -1
        self.sdt = ''
        self.sophongngu = -1
        self.mota = ''
        self.nguoidang = ''
        self.sanh = ''
        self.loai = ''

class tinh_tp():
    def __init__(self, id, ten):
        self.id = id
        self.ten = ten

class quan_huyen():
    def __init__(self,id, ten, id_tinh_tp):
        self.id = id
        self.ten = ten
        self.id_tinh_tp = id_tinh_tp

class phuong_xa():
    def __init__(self,id, ten, id_quan_huyen):
        self.id = id
        self.ten = ten
        self.id_quan_huyen = id_quan_huyen

class dia_chi():
    def __init__(self, ten, id_phuong_xa):
        self.id = id
        self.ten = ten
        self.id_phuong_xa = id_phuong_xa




