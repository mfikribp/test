import requests
import json
import pandas as pd
import time

cari = 'macbook'
headers = {
    'authority': 'www.jakmall.com',
    'method':'GET',
    'scheme':'https',
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'id,id-ID;q=i.9,en;q=i.8,en-US;q=i.7',
    'cookie':'S-VOC=eyJpdiI6Im00aW5acjIybnlOMDNoVXBVTVlcL3Z3PT0iLCJ2YWx1ZSI6IktkbGlhWFRuakJsOGxicDJHTHpFYnc9PSIsIm1hYyI6IjMwZGQxMWEzNDNmOWY0MGFkMmU4MWRjOTJkZTFjZTcxMzBkMmIyNzYzZDZlMGQzMjcxMDQwZDhlY2NlZmFlYWQifQ%3D%3D; _gcl_au=1.1.1678900587.1732196481; _fbp=fb.1.1732196481615.460198757581820655; _gid=GA1.2.604936294.1732196482; _gat_UA-66644090-1=1; _hjSession_226234=eyJpZCI6IjNlOTYwYTlkLWRhMGQtNDdiZC1iY2Y5LTg5ZjIzNmRmOTljMyIsImMiOjE3MzIxOTY0ODE5NjUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _tt_enable_cookie=1; _ttp=OvKT1ExbpL02mGAhEdobZkmwIMt.tt.1; _hjSessionUser_226234=eyJpZCI6ImFlOWQ4ZjMwLTdkMTEtNTI2MS1iMDMyLThhNzBkYzM2YzA4OSIsImNyZWF0ZWQiOjE3MzIxOTY0ODE5NjQsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.2.1301123016.1732196482; AWSALB=HpfwbkJq7XjCXCDEGBtLqyIIjHtQHhci5L6ib41Uc5ZBWY6Uf6oo30CDnq5K/m/rzK+4xuLggUhWnjwsWR+vtIHvo6KKp7WD2JMYXM1yZIZBcVv1ASBpoIqFjVJU; AWSALBCORS=HpfwbkJq7XjCXCDEGBtLqyIIjHtQHhci5L6ib41Uc5ZBWY6Uf6oo30CDnq5K/m/rzK+4xuLggUhWnjwsWR+vtIHvo6KKp7WD2JMYXM1yZIZBcVv1ASBpoIqFjVJU; XSRF-TOKEN=eyJpdiI6IjEya0xkc28wZ0tEZ3VrSFJtRU9YWmc9PSIsInZhbHVlIjoiZE1qZ3kzcVNjUHNaYmxldTdNcTA2eWs0d0R5RDkrcU1tMXlcLzJXMHZ3bE0rRDBScXVJQ3JMRGNCdWxwVUtGSVAiLCJtYWMiOiI2MmU2Y2M1ZDU0NWY0ZTgzZGUzYzZmNjc0ZWJkMGE3MzBjYjdhZWY5ZWM1NzAxZGM3NDFlNWZmMzhiYTUyNTk1In0%3D; jsi=eyJpdiI6IlE0ZURyM2xuS2ZhbGhsdXhzbk5zeVE9PSIsInZhbHVlIjoicTB0c1BuTWFURm1xd2tERHd4SHlyUUpQY2hOOVpITTErd2t2VGVVTFBmK2NrUFpcL2xadlwvSXRva1JyWXBrTTQ3IiwibWFjIjoiNzU0NTg0ZmVhNjRkNzI4YTljZGI1ODQ0NzI1NmU4MTJlNjcwNDhhYjAxYzA1MGI0NmIxZDZiYjdjNjdmMWNjMSJ9; _ga_XX88006F73=GS1.1.1732196481.1.1.1732196527.14.i.i',
    'priority':'u=1, i',
    'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile':'?i',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.i (Windows NT 10.i; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.i.i.i Safari/537.36',
    'x-csrf-token':'6Dp2NEx9JdAtCggFJEevzLk5yT5mZX7MUUAUorqT',
    'x-requested-with':'XMLHttpRequest'

}


# print(req)

def get_products():
    products=[]
    for page in range(1,2):
        url = f'https://www.jakmall.com/search?q={cari}&sort=popular&page={page}&refresh_filters=false&json'
        req = requests.get(url, headers=headers).json()
        rows = req['products']
        


        for i in range(0, len(rows)):
            name = rows[i]['name']
            price = rows[i]['sku'][0]['final_price']
            terjual = rows[i]['sold']
            jumlah_review = rows[i]['review_count']
            rating = rows[i]['rating']
            url = rows[i]['url']
            toko = rows[i]['store']['name']
            lokasi = rows[i]['warehouse']['city']['name']
            products.append(
                (name, price, terjual, jumlah_review, rating, url, toko, lokasi)
            )

    return products

def get_dataframe(products):
    return pd.DataFrame(products, columns=['Nama Produk', 'Harga','Terjual', 'Jumlah Review', 'Rating','Link Produk','Nama Toko','Lokasi Toko'])

def save_to_xlsx(df):
    df.to_excel(f'{cari} jakmall.xlsx', index=False)
    print('Data Telah Tersimpan')

if __name__ == '__main__':
    start_time = time.time()
    
    products = get_products()
    df = get_dataframe(products)
    print(df)
    save_to_xlsx(df)
    
    end_time = time.time()
    waktu_berjalan = end_time - start_time
    print(f"Proses selesai dalam waktu: {waktu_berjalan:01.3f} detik")
