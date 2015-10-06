import requests
from BeautifulSoup import BeautifulSoup

url = 'http://coffer.com/mac_find/?string=apple'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'table2'})

for row in table.findAll('tr'):
	for cell in row.findAll('td'):
		print cell.text.replace('\n&nbsp', '')