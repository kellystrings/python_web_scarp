# This app do webscrap data from html site

from bs4 import BeautifulSoup
import csv


html_path = 'apple_store.html'

with open(html_path, 'r') as html_file:
    html_content = html_file.read()

# print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')

header = soup.find('h1')

Product_divs = soup.find_all('div', class_="product")

# Opening a CSV file for later
with open('apple_products.csv', 'w') as file_csv:
    writer = csv.writer(file_csv)

# Adding Header
    writer.writerow(['product_name', 'price', 'qty_left', 'ratings', 'est'])

    for product in Product_divs:
        product_name = product.find('h3').text #if product.find('h3').text else 'NA'
        price = product.find('p').text.replace('Price: ', '')
        qty_left = product.find_all('p')[1].text.replace('Quantity Available: ', '')
        ratings = product.find('p', class_="rating").text
        est = product.find_all('p')[-1].text.replace('Estimated Shipping: ', '')
        # print(est, '\n')

        # Saving the data
        writer.writerow([product_name, price, qty_left, ratings, est])


print('Congratulations, Data scrapped and saved successfully')    


# print(menus)
# print(header)