from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TEXT, Float
from config.db import meta, engine

loai_nha_dat_ban = Table(
    "loai_nha_dat_ban",
    meta,
    Column("id", String(255), primary_key=True),
    Column("ten", TEXT),
    Column("link", TEXT),
)

loai_nha_dat_cho_thue = Table(
    "loai_nha_dat_cho_thue",
    meta,
    Column("id", String(255), primary_key=True),
    Column("ten", TEXT),
    Column("link", TEXT),
)

bat_dong_san = Table (
    "bat_dong_san",
    meta,
    Column("id", String(255), primary_key=True),
    Column("tieu_de",TEXT,),
    Column("dia_chi_cu_the", TEXT),
    Column("gia", Integer),
    Column("dien_tich",Float ),
    Column("sdt",String(10)),
    Column("so_phong_ngu", Integer),
    Column("mo_ta",TEXT),
    Column("nguoi_dang",String(20)),
    Column("anh", TEXT),
    Column("id_loai_ban", String(255), ForeignKey("loai_nha_dat_ban.id"), nullable=True),
    Column("id_loai_thue", String(255), ForeignKey("loai_nha_dat_cho_thue.id"), nullable=True)
)

meta.create_all(engine)
