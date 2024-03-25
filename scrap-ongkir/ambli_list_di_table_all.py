import csv
from bs4 import BeautifulSoup
import requests
import time

# Fungsi untuk melakukan scraping pada satu halaman
def scrape_page(url, writer):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    questions = soup.select('.ap-questions-item')
    for question in questions:
        title = question.select_one('.ap-questions-title a').text.strip()
        url = question.select_one('.ap-questions-title a')['href']
        writer.writerow({'Title': title, 'URL': url})
    
    return soup  # Mengembalikan objek soup untuk digunakan di luar fungsi

# URL halaman web yang akan di-scrape
base_url = 'https://tanyapaket.cekresi.com/'
start_page = 1

# Membuka file CSV untuk menyimpan data
with open('data_tanyapaket.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    current_page = start_page
    soup = None  # Inisialisasi objek soup
    while True:
        url = f'{base_url}/page/{current_page}/'
        print(f'Scraping page {current_page}...')
        soup = scrape_page(url, writer)
        
        # Temukan tautan ke halaman berikutnya
        next_page_link = soup.select_one('.ap-pagination .page-numbers[href]')
        if next_page_link:
            current_page += 1
            time.sleep(1)  # Hindari permintaan terlalu cepat
        else:
            break

print('Scraping selesai!')
