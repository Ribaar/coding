import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the website
url = 'https://komikindo.id/daftar-manga/?list'
response = requests.get(url)

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the a tags with class "tip" and extract their text and href
judul = []
links = []
for a in soup.find_all('a', class_='tip'):
    judul.append(a.text)
    links.append(a['href'])

# Create a dataframe with the extracted data
df = pd.DataFrame({'judul': judul, 'links': links})

# Open each link and extract the sinopsis and jenis
sinopsis = []
jenis = []
for link in df['links']:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    sinopsis.append(soup.find('p').text)
    span = soup.find('span', string='Jenis Komik:')
    jenis.append(span.find_next_sibling('a').text)

# Add the 'sinopsis' and 'jenis' columns to the dataframe
df['sinopsis'] = sinopsis
df['jenis'] = jenis

# Create an Excel file with the data
df.to_excel('komik_data.xlsx', index=False)