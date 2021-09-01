import requests
from bs4 import BeautifulSoup

url='https://dounotech.com/category/job-openings/'
response = requests.get(url)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, 'html.parser')
    h2s = soup.findAll('h2')
    # [print(str(h2)+'\n\n') for h2 in h2s]
    for h2 in h2s:
        a = h2.find('a')
        link = a['href']
        links.append('https://dounotech.com/category/job-openings'+link)
    print(links)
    # <h2 class="entry-title">
    #     <a href="https://dounotech.com/2021/03/12/remote-react-django-developer/" rel="bookmark">Remote React/Django Developer
    #     </a>
    # </h2>