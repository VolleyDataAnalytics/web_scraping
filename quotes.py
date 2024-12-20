import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'http://quotes.toscrape.com/'

# Send GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage!")

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quote elements on the page
    quotes = soup.find_all('div', class_='quote')

    # Loop through each quote and extract the text, author, and tags
    for quote in quotes:
        # Extract the text of the quote
        text = quote.find('span', class_='text').text
        # Extract the author of the quote
        author = quote.find('small', class_='author').text
        # Extract the tags associated with the quote
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        # Print the extracted information
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")
        print('-' * 80)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
