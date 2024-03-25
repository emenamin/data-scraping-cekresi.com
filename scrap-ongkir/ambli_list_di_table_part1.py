import csv
from bs4 import BeautifulSoup
import requests

# URL halaman web yang akan di-scrape
url = 'https://tanyapaket.cekresi.com/'

# Mengambil konten HTML dari halaman web
response = requests.get(url)
html_content = response.text

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Membuka file CSV untuk menyimpan data
with open('data_tanyapaket.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Menentukan nama kolom
    fieldnames = ['Title', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Menulis header kolom ke dalam file CSV
    writer.writeheader()
    
    # Mengambil semua elemen dengan kelas 'ap-questions-item' di dalam div 'ap-questions'
    questions = soup.select('.ap-questions-item')
    
    # Iterasi melalui setiap elemen pertanyaan
    for question in questions:
        # Mengambil judul pertanyaan
        title = question.select_one('.ap-questions-title a').text.strip()
        
        # Mengambil URL pertanyaan
        url = question.select_one('.ap-questions-title a')['href']
        
        # Menulis data ke dalam file CSV
        writer.writerow({'Title': title, 'URL': url})
