import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'http://books.toscrape.com/'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read().decode('utf-8')
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabbing all containers with class name = product_pod
containers = page_soup.findAll('article', {'class': 'product_pod'})

filename = "products.csv"
f = open(filename, 'w')

headers = "title, price, in stock\n"

f.write(headers)

container = containers[1]

for container in containers:
    # Example: Get the book title
    title = container.h3.a['title']
    price_container = container.findAll('p', {'class':'price_color'})[0].text.strip()
    available_book = container.findAll('p', {'class':'instock availability'})[0].text.strip()
    print("brand:" + title)
    print("available_book:" + available_book)
    print("Price:" + price_container)

    f.write(title + ',' +price_container + ',' + available_book + '\n')

f.close()

