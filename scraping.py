import requests
from bs4 import BeautifulSoup

url='https://dounotech.com/'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title')
    print(title.text)