import requests
from app.crawler.models.some_model import *
from app.crawler.crawler import *

host = "127.0.0.1"
port = 8000
API_URL = "http://" + host + ":" + str(port)

loai_thue, loai_ban = crawl_loai_thue_loai_ban()

for i in range(len(loai_thue)):
    loai_thue[i].id = i+1
    loai_json = {'id': i+1, 'ten': loai_thue[i].ten, 'link': loai_thue[i].link}
    requests.post(API_URL + "/loai_nha_dat_cho_thue", json = loai_json)

for i in range(len(loai_ban)):
    loai_ban[i].id = i+1
    loai_json = {'id': i + 1, 'ten': loai_thue[i].ten, 'link': loai_thue[i].link}
    requests.post(API_URL + "/loai_nha_dat_ban", json=loai_json)


def insert_post():
    count_id=0
    for j in range(len(loai_thue)):
        link_posts_thue = crawl_all_link(loai_thue[j],2)
        for i in range(len(link_posts_thue)):
            count_id+=1
            post = crawl_post(link_posts_thue[i])
            post_json = {'id': count_id,'tieu_de': post.tieude, 'dia_chi_cu_the': post.diachi, 'gia': int(post.gia/100000), 'dien_tich': post.dientich,
                         'sdt': post.sdt, 'so_phong_ngu': post.sophongngu, 'mo_ta': post.mota, 'nguoi_dang': post.nguoidang,
                         'anh': post.anh,
                         'id_loai_thue': loai_thue[j].id}
            requests.post(API_URL + "/bat_dong_san", json=post_json)
        for j in range(len(loai_ban)):
            link_posts_ban = crawl_all_link(loai_ban[j], 2)
            for i in range(len(link_posts_ban)):
                count_id += 1
                post = crawl_post(link_posts_ban[i])
                post_json = {'id': count_id, 'tieu_de': post.tieude, 'dia_chi_cu_the': post.diachi,
                             'gia': int(post.gia / 100000), 'dien_tich': post.dientich,
                             'sdt': post.sdt, 'so_phong_ngu': post.sophongngu, 'mo_ta': post.mota,
                             'nguoi_dang': post.nguoidang,
                             'anh': post.anh,
                             'id_loai_ban': loai_ban[j].id}
                requests.post(API_URL + "/bat_dong_san", json=post_json)
insert_post()



