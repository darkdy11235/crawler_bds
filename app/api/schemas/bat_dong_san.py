from typing import Optional
from pydantic import BaseModel

class LoaiNhaDatBanBase(BaseModel):
    id: str
    ten: Optional[str] = None
    link: Optional[str] = None

class LoaiNhaDatBanCreate(LoaiNhaDatBanBase):
    pass

class LoaiNhaDatBan(LoaiNhaDatBanBase):
    class Config:
        orm_mode = True

class LoaiNhaDatChoThueBase(BaseModel):
    id: str
    ten: Optional[str] = None
    link: Optional[str] = None

class LoaiNhaDatChoThueCreate(LoaiNhaDatChoThueBase):
    pass

class LoaiNhaDatChoThue(LoaiNhaDatChoThueBase):
    class Config:
        orm_mode = True

class BatDongSanBase(BaseModel):
    id: str
    tieu_de: Optional[str] = None
    dia_chi_cu_the: Optional[str] = None
    gia: Optional[int] = None
    dien_tich: Optional[float] = None
    sdt: Optional[str] = None
    so_phong_ngu: Optional[int] = None
    mo_ta: Optional[str] = None
    nguoi_dang: Optional[str] = None
    anh: Optional[str] = None
    id_loai_ban: Optional[str] = None
    id_loai_thue: Optional[str] = None

class BatDongSanCreate(BatDongSanBase):
    pass

class BatDongSan(BatDongSanBase):

    class Config:
        orm_mode = True

