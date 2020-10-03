# verloop2020

  - Just download and install packages from requirements.txt
  - And Run project :)


How to run :
```sh
$ manage.py runserver
```
> Project Structure

    |___ app 
    |        |___ templates
    |        |___ admin.py
    |        |___ apps.py
    |        |___ models.py
    |        |___ test.py
    |        |___ views.py
    |        |___ urls.py   
    |
    |___ verloop2020
    |                 |___ staticfiles
    |                 |___ asgi.py
    |                 |___ settings.py
    |                 |___ urls.py
    |                 |___ wsgi.py
    |
    |___ manage.py
 
# docs

 - GET method recieve all Saved Request records
 - POST method require to pass sample json

## My Temporary Api_Key
- { "book_url": "https://www.goodreads.com/book/show/12177850.xml?key=6mM5giON9W4CYjn1EKIA"} # working
- { "book_url": "https://www.goodreads.com/book/show/12067.xml?key=6mM5giON9W4CYjn1EKIA"}   # working
- { "book_url": "https://www.gooreads.com/book/show/22034.xml?key=6mM5giON9W4CYjn1EKIA"} # invalidURL
- { "book_url": "https://www.goodreads.com/book/show/3577922658.xml?key=6mM5giON9W4CYjn1EKIA"} # error

