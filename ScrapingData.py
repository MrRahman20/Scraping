import requests
from bs4 import BeautifulSoup
import csv

# URL dari halaman Wikipedia yang ingin Anda scraping
url = 'https://id.wikipedia.org/wiki/Demografi_Indonesia'

# Mengirim permintaan HTTP GET ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Membuat objek BeautifulSoup dari konten halaman
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Mencari tabel yang berisi data jumlah penduduk menurut provinsi
    table = soup.find('table', {'class': 'wikitable sortable'})
    
    # Memeriksa apakah tabel ditemukan
    if table:
        # Mengambil semua baris dari tabel
        rows = table.find_all('tr')
        
        # Membuka file CSV untuk menulis di dalam folder 'scraping'
        with open('scraping/data_penduduk.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')  # Menggunakan titik koma sebagai pemisah
            # Menulis header
            writer.writerow(['Provinsi', 'Populasi 2020'])
            
            # Memproses setiap baris
            for row in rows[1:]:  # Lewati header
                # Mengambil semua sel dari baris
                cells = row.find_all('td')
                # Memeriksa apakah baris memiliki data yang diinginkan
                if len(cells) > 3:  # Pastikan ada cukup kolom
                    # Kolom pertama adalah nama provinsi dan kolom keempat adalah populasi 2020
                    nama_provinsi = cells[0].get_text(strip=True)
                    populasi_2020 = cells[3].get_text(strip=True)
                    # Menulis data ke file CSV dalam satu baris
                    writer.writerow([nama_provinsi, populasi_2020])
        print("Data berhasil diekspor ke data_penduduk.csv")
    else:
        print("Tabel tidak ditemukan.")
else:
    print(f"Permintaan gagal dengan status code: {response.status_code}")