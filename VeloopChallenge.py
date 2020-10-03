import requests
import xml.etree.ElementTree as ET

class GoodreadsAPIClient:

    @classmethod
    def get_book_details(cls, book_url: str) -> dict:
        context = {}
        res = requests.get(book_url) # get xml response
        root = ET.fromstring(res.content) 
        
        for child in root.findall('book'): 
            context['title'] = child.find('title').text
            context['average_rating'] = child.find('average_rating').text
            context['ratings_count'] = child.find('ratings_count').text
            context['num_pages'] = child.find('num_pages').text
            context['image_url'] = child.find('image_url').text
            context['publication_year'] = child.find('publication_year').text
            context['authors'] = child.find('authors').text

        return context    

# getting url from command line
user_input = input('Enter URL -> ')
response = GoodreadsAPIClient.get_book_details(book_url=user_input)
print(response)
