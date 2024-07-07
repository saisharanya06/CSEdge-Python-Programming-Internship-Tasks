import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape book data and save to CSV
def scrape_books_and_save_to_csv(url, csv_filename):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize empty list to store book data
    books_data = []

    # Find all book items
    books = soup.find_all('article', class_='product_pod')

    # Extract data for each book
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        # Append data to list
        books_data.append({
            'Title': title,
            'Price': price
        })

    # Save data to CSV file
    save_to_csv(books_data, csv_filename)
    print(f'Scraped data saved to {csv_filename}')

# Function to save data to CSV file
def save_to_csv(data, filename):
    # Define fieldnames for CSV
    fieldnames = ['Title', 'Price']

    # Write data to CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    # URL of the website to scrape (books.toscrape.com)
    url = 'http://books.toscrape.com/catalogue/category/books/history_32/index.html'

    # CSV filename to save the scraped data
    csv_filename = 'books_data.csv'

    # Scrape the website and save data to CSV
    scrape_books_and_save_to_csv(url, csv_filename)
