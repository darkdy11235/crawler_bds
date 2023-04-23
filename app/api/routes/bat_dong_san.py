from fastapi import APIRouter
from config.db import conn
from models.some_model import bat_dong_san, loai_nha_dat_ban, loai_nha_dat_cho_thue
from schemas.bat_dong_san import LoaiNhaDatBan, LoaiNhaDatChoThue, BatDongSan
from typing import List
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

BatDongSanRouter = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)

@BatDongSanRouter.get(
    "/bat_dong_san",
    tags=["bat_dong_san"],
    response_model=List[BatDongSan],
    description="Get a list of all Real Estate",
)
def get_bat_dong_san():
    return conn.execute(bat_dong_san.select()).fetchall()

@BatDongSanRouter.get(
    "/bat_dong_san/loai_nha_dat_ban",
    tags=["bat_dong_san"],
    response_model=List[BatDongSan],
    description="Get a list of sell type Real Estate",
)
def get_bat_dong_san_by_type():
    query = bat_dong_san.select().where(bat_dong_san.c.id_loai_ban.isnot(None)).select_from(bat_dong_san.join(loai_nha_dat_ban))
    return conn.execute(query).fetchall()

@BatDongSanRouter.get(
    "/bat_dong_san/loai_nha_dat_cho_thue",
    tags=["bat_dong_san"],
    response_model=List[BatDongSan],
    description="Get a list of rent type Real Estate",
)
def get_bat_dong_san_by_type():
    query = bat_dong_san.select().where(bat_dong_san.c.id_loai_thue.isnot(None)).select_from(bat_dong_san.join(loai_nha_dat_cho_thue))
    return conn.execute(query).fetchall()

@BatDongSanRouter.post("/bat_dong_san", tags=["bat_dong_san"], response_model=BatDongSan, description="Create a new Real Estate")
def create_new_real_estate(new_bat_dong_san: BatDongSan):
    new_real_estate = {
        "id": new_bat_dong_san.id,
        "tieu_de": new_bat_dong_san.tieu_de,
        "dia_chi_cu_the": new_bat_dong_san.dia_chi_cu_the,
        "gia": new_bat_dong_san.gia,
        "dien_tich": new_bat_dong_san.dien_tich,
        "sdt": new_bat_dong_san.sdt,
        "so_phong_ngu": new_bat_dong_san.so_phong_ngu,
        "mo_ta": new_bat_dong_san.mo_ta,
        "nguoi_dang": new_bat_dong_san.nguoi_dang,
        "anh": new_bat_dong_san.anh,
        "id_loai_ban": new_bat_dong_san.id_loai_ban,
        "id_loai_thue": new_bat_dong_san.id_loai_thue
    }
    print(new_real_estate)
    result = conn.execute(bat_dong_san.insert().values(new_real_estate))
    return conn.execute(bat_dong_san.select().where(bat_dong_san.c.id == result.lastrowid)).first()

@BatDongSanRouter.delete("/bat_dong_san/{id}", tags=["bat_dong_san"], status_code=HTTP_204_NO_CONTENT)
def delete_estate(id: str):
    conn.execute(bat_dong_san.delete().where(bat_dong_san.c.id == id))
    return conn.execute(bat_dong_san.select().where(bat_dong_san.c.id == id)).first()




LoaiNhaDatBanRouter = APIRouter()
@LoaiNhaDatBanRouter.get("/loai_nha_dat_ban",
    tags=["loai_nha_dat_ban"],
    response_model=List[LoaiNhaDatBan],
    description="Get a list of all type of real estate",
)
def get_typeOfRealEstate():
    return conn.execute(loai_nha_dat_ban.select()).fetchall()

@LoaiNhaDatBanRouter.post("/loai_nha_dat_ban",
    tags=["loai_nha_dat_ban"],
    response_model=LoaiNhaDatChoThue,
    description="Insert Type of Estate",)
def create_new_type_real_estate(new_type: LoaiNhaDatBan):
    new_type_sell = {
        "id": new_type.id,
        "ten": new_type.ten,
        "link": new_type.link
    }
    print(new_type_sell)
    result = conn.execute(loai_nha_dat_ban.insert().values(new_type_sell))
    return conn.execute(loai_nha_dat_ban.select().where(loai_nha_dat_ban.c.id == result.lastrowid)).first()



LoaiNhaDatChoThueRouter = APIRouter()
@LoaiNhaDatChoThueRouter.get("/loai_nha_dat_cho_thue",
    tags=["loai_nha_dat_cho_thue"],
    response_model=List[LoaiNhaDatChoThue],
    description="Get a list of all type of real estate",
)
def get_typeOfRealEstate():
    return conn.execute(loai_nha_dat_cho_thue.select()).fetchall()


@LoaiNhaDatChoThueRouter.post("/loai_nha_dat_cho_thue",
    tags=["loai_nha_dat_cho_thue"],
    response_model=LoaiNhaDatChoThue,
    description="Insert Type of Estate",)
def create_new_type_real_estate(new_type: LoaiNhaDatChoThue):
    new_type_sell = {
        "id": new_type.id,
        "ten": new_type.ten,
        "link": new_type.link
    }
    print(new_type_sell)
    result = conn.execute(loai_nha_dat_cho_thue.insert().values(new_type_sell))
    return conn.execute(loai_nha_dat_cho_thue.select().where(loai_nha_dat_cho_thue.c.id == result.lastrowid)).first()