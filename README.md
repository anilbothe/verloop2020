# verloop2020

  - This Project/Assignment can be solved by single python file => *VeloopChallenge.py*
  - *VeloopChallenge.py* this file include main logic
  - But I made by using Django
  - Just download and install packages from requirements.txt
  - And Run project :)

# Demo
 - To see Demo  ->  [click here](http://anilb.pythonanywhere.com/) 
 - Admin username & password is => _admin_
 - And Admin url -> [http://anilb.pythonanywhere.com/admin](http://anilb.pythonanywhere.com/admin) 

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
 
 - To see Demo  ->  [click here](http://anilb.pythonanywhere.com/) 
 - GET method recieve all Saved Request records
 - POST method require to pass sample json

## Sample URLs - Pass into POST method.
- { "book_url": "https://www.goodreads.com/book/show/12177850.xml?key=6mM5giON9W4CYjn1EKIA"} # working
- { "book_url": "https://www.goodreads.com/book/show/12067.xml?key=6mM5giON9W4CYjn1EKIA"}   # working
- { "book_url": "https://www.gooreads.com/book/show/22034.xml?key=6mM5giON9W4CYjn1EKIA"} # invalidURL
- { "book_url": "https://www.goodreads.com/book/show/3577922658.xml?key=6mM5giON9W4CYjn1EKIA"} # error

