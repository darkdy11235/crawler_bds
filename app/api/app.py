from fastapi import FastAPI
from routes.bat_dong_san import BatDongSanRouter,LoaiNhaDatBanRouter, LoaiNhaDatChoThueRouter
from config.openapi import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(BatDongSanRouter)
app.include_router(LoaiNhaDatBanRouter)
app.include_router(LoaiNhaDatChoThueRouter)
