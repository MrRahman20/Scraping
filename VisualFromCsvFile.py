import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Membaca data dari file CSV
data = pd.read_csv('D:\Source\scraping\data_penduduk.csv', sep=';')
# Menghapus titik dari kolom 'Populasi 2020' dan mengonversinya ke integer
data['Populasi 2020'] = data['Populasi 2020'].str.replace('.', '').astype(int)
# Menghitung total populasi untuk persentase
total_populasi = data['Populasi 2020'].sum()
# Membuat bar chart
plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Populasi 2020', y='Provinsi', data=data, palette='viridis')
# Menambahkan anotasi untuk setiap bar di sebelah kanan luar
max_x = data['Populasi 2020'].max() + 5000000  # Menentukan posisi tetap di luar kotak
for index, row in data.iterrows():
    jumlah = row['Populasi 2020']
    persentase = (jumlah / total_populasi) * 100
    barplot.text(max_x, index, f'{jumlah:,} ({persentase:.2f}%)', color='black', ha="left", va="center")
plt.title('Data Penduduk Indonesia Provinsi (2020)')
plt.xlabel('Populasi 2020')
plt.ylabel('Provinsi')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Membuat pie chart
plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    data['Populasi 2020'], 
    labels=data['Provinsi'], 
    autopct='%1.1f%%', 
    startangle=10,
    textprops=dict(color="black"),
    labeldistance=1.2,  # Mengatur jarak label dari pusat
    pctdistance=1,    # Mengatur jarak persentase dari pusat
    radius=0.2          # Mengatur radius lingkaran lebih kecil
)
# Menyesuaikan rotasi teks agar mengikuti pusat lingkaran
for i, text in enumerate(texts):
    text.set_rotation_mode('anchor')
    angle = (wedges[i].theta2 - wedges[i].theta1) / 2 + wedges[i].theta1
    if angle > 180:
        angle -= 360
    text.set_rotation(angle)
    text.set_horizontalalignment('center')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_bbox(dict(facecolor='black', alpha=0.5, edgecolor='none'))
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle('Data Penduduk Indonesia Provinsi (2020)', y=0.03)  # Menempatkan judul di bawah
plt.show()