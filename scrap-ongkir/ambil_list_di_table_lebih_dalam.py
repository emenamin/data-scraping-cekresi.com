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
        question_page_soup = scrape_question_page(url)
        if question_page_soup:
            message = question_page_soup.select_one('.ap-q-content').text.strip()
            category = question_page_soup.select_one('.question-categories a').text.strip()
            writer.writerow({'Title': title, 'URL': url, 'Message': message, 'Category': category})
    
    return soup  # Mengembalikan objek soup untuk digunakan di luar fungsi

# Fungsi untuk melakukan scraping pada halaman detail pertanyaan
def scrape_question_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    else:
        print(f'Failed to scrape question page: {url}')
        return None

# URL halaman web yang akan di-scrape
base_url = 'https://tanyapaket.cekresi.com/'
start_page = 1
max_page = 10  # Jumlah maksimum halaman yang akan di-scrape

# Membuka file CSV untuk menyimpan data
with open('data_tanyapaket.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'URL', 'Message', 'Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    current_page = start_page
    soup = None  # Inisialisasi objek soup
    while current_page <= max_page:
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
