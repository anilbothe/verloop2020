from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xml.etree.ElementTree as ET
import requests

from .models import GoodReadsAudit
from .serializer import GoodReadsAuditSerializer


# Trial index page
def index(request):
    return render(request, 'index.html')

# Verloop-Challenge2020 API 
class GoodreadsAPIClient(APIView):
    """See Post method"""
    def get(self, request):        
        obj = GoodReadsAudit.objects.all()
        result = GoodReadsAuditSerializer(obj, many=True)
        return Response(result.data)
    
    # main logic
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

    # post api
    def post(self, request):        
        # url = request.data['book_url'] # e.g. https://www.goodreads.com/book/show/12177850.xml?key=5VI9EeBQZ7z2P7SadUXFvQ
        # print(request.data['book_url'])
        try:
            # Please refer good_reads.py
            result = GoodreadsAPIClient.get_book_details(book_url=request.data['book_url'])
            # print(result)
            if not result:
                return Response("ErrorGoodreadsURL")
            else:
                # save audit
                GoodReadsAudit.objects.create(
                    title            = result['title'],
                    average_rating   = result['average_rating'],
                    ratings_count    = result['ratings_count'],
                    num_pages        = result['num_pages'],
                    image_url        = result['image_url'],
                    publication_year = result['publication_year'],
                    authors          = result['authors']
                )
            return Response(result)
        except:
            return Response("InvalidGoodreadsURL")

        return Response("Something went wrong!")



# ---------------------------------------------------------------------------------
# ############################### sample JSON send ############################### #
# ---------------------------------------------------------------------------------
# My Temporary Api_Key
# 1. { "book_url": "https://www.goodreads.com/book/show/12177850.xml?key=6mM5giON9W4CYjn1EKIA"}
# 2. { "book_url": "https://www.goodreads.com/book/show/12067.xml?key=6mM5giON9W4CYjn1EKIA"}
# 3. { "book_url": "https://www.gooreads.com/book/show/22034.xml?key=6mM5giON9W4CYjn1EKIA"} # invalidURL
# 4. { "book_url": "https://www.goodreads.com/book/show/3577922658.xml?key=6mM5giON9W4CYjn1EKIA"} # error
