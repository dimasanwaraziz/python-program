#!/home/ubuntu/venv/saham/bin/python
from bs4 import BeautifulSoup as soup
import requests
import datetime
kode_saham = ['telkom-indones', 'unilever-indon', 'bank-rakyat-in']
available_lot = [11, 9, 13]
#avg_price = [4015.72, 42200.00, 4040.00]
avg_price = [3944.55, 8211.11, 3757.69]
import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
print("====[ LAPORAN SAHAM HARIAN ]====")
print(datetime.datetime.now().strftime("%d %B %Y, %H:%M") + "\n")
i = 0
jumlah = 0
for kode in kode_saham:
    nama_cari = kode
    my_url = 'https://id.investing.com/equities/' + nama_cari
    url = requests.get(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    page_soup = soup(url.content, "html.parser")
    average_price = avg_price[i]
    last_price = page_soup.find('span', {'id':'last_last'}).text.replace('.', '').encode('utf-8')
    nama_quote = page_soup.find('h1', {'class':'float_lang_base_1 relativeAttr'}).text.strip()
    penutupan_sebelum = page_soup.find('span', {'class':'float_lang_base_2 bold'}).text.replace('.', '')
    print(f"<b>{nama_quote}</b>")
    print(f"    status ({((float(last_price)-float(penutupan_sebelum))/float(penutupan_sebelum)) * 100:.2f}%)")
    print("    Last Price : Rp " + locale.format_string("%.2f", float(last_price), grouping=True))
    print("    You average Price : Rp " + locale.format_string("%.2f", average_price, grouping=True))
    print("    Gain Lose : Rp " + locale.format_string("%.2f", (float(last_price) - average_price) * (available_lot
[i] * 100), grouping=True) + f" ({((float(last_price)-average_price)/average_price)*100:.2f}%)" + "\n")
    jumlah = jumlah + (float(last_price) - average_price) * (available_lot[i] * 100)
    i=i+1
print(f"Total Gain  Lose All : Rp {locale.format_string('%.2f', float(jumlah), grouping=True)}")
