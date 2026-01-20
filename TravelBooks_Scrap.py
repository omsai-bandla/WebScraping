import requests
import pandas
from bs4 import BeautifulSoup
response = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
#print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
#For Travel Books Titles
names = []  
for i in range(1, 10):
    title = soup.find_all('h3')[i-1].find('a')['title']
    names.append(title)
print(names)
#For Travel Books Prices    
prices = []
for i in range(1, 10):
    price = soup.find_all('p', class_='price_color')[i-1].text
    prices.append(price)    
print(prices)
#For Travel Books Ratings
ratings = []
for i in range(1, 10):
    rating = soup.find_all('p', class_='star-rating')[i-1]['class'][1]
    ratings.append(rating)  
print(ratings)
#For Links of Travel Books
links = []
for i in range(1, 10):
    link = soup.find_all('h3')[i-1].find('a')['href']
    full_link = "https://books.toscrape.com/catalogue/category/books/travel_2/" + link
    links.append(full_link)
print(links)
#For images of Travel Books
images = []
for i in range(1, 10):
    img = soup.find_all('div', class_='image_container')[i-1].find('img')['src']
    full_img_link = "https://books.toscrape.com/catalogue/category/books/travel_2/" + img.replace('../..', '')
    images.append(full_img_link)
print(images)
#For review availability of Travel Books
reviews = []
for i in range(1, 10):
    review = soup.find_all('p', class_='instock availability')[i-1].text.strip()
    reviews.append(review)
print(reviews)
#For UPC of Travel Books
upcs = []
for i in range(1, 10):
    book_page_link = links[i-1]
    book_response = requests.get(book_page_link)
    book_soup = BeautifulSoup(book_response.content, 'html.parser')
    upc = book_soup.find('th', string='UPC').find_next_sibling('td').get_text(strip=True)
    upcs.append(upc)
print(upcs)
#For Tax of Travel Books
taxes = []
for i in range(1, 10):
    book_page_link = links[i-1]
    book_response = requests.get(book_page_link)
    book_soup = BeautifulSoup(book_response.content, 'html.parser')
    tax = book_soup.find('th', string='Tax').find_next_sibling('td').get_text(strip=True)
    taxes.append(tax)
print(taxes)
#Creating DataFrame
data = {
    'Name': names,
    'Price': prices,
    'Rating': ratings,
    'Link': links,
    'Image': images,
    'Review Availability': reviews,
    'UPC': upcs,
    'Tax': taxes
}
df = pandas.DataFrame(data)
print(df)
#Saving DataFrame to CSV
df.to_csv('travel_books.csv', index=False)
