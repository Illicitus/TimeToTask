# TimeToTask
REST API web service just with 2 active functions.

- reverse string in request 'phrase'
- calculates the quantity of words in request 'phrase'

And 1 passive function.

- statistics tracking mechanism (calculate how many times each endpoint was accessed each day).

## Requirements
* `Python 3.6+`

## Tasks list
**1** - 
The API endpoint `api/strings-operations/reverses/` can accept POST request with a string and
returns the string where each word is reversed. Example: POST to `api/strings-operations/reverses/`
with data `{"phrase": "I love hamburgers"}`. In response you will get: `{"result": "I evol sregrubmah"}`

**2** - 
The API endpoint `api/strings-operations/word-counts/` should calculates the quantity of words.
Example:  POST to `api/strings-operations/word-counts/` with data `{"phrase": "I love hamburgers"}`.
In response you will get: `{"result": 3}`

**3** - 
We should develop a statistics tracking mechanism that tracks how many times each endpoint was
accessed each day. This data should be available from admin interface. For instance, as an admin
I can see the page with columns 'Date', 'URL' and 'Access count' and values '9-20-20017',
`api/strings-operations/reverses/` and 25. The admin should not have access to edit these fields.
We should be able to filter the result by endpoint url and by date.

## Task Requirements
- Use the latest versions of technologies: Python 3, Django and Django admin, DRF, SQLite, Git.
- Please, document your API
- You API should work with JSON data only
- Write tests. You are able to use your favorite test framework
- Write short README.md file with instructions how to install your app and run tests
- API should be public accessed (no need of registration and authorization for API access)
- It would be nice if you use Middlewares when developing statistics tracking system (option 4 from Specifications).

## Installation
Clone repository
```
git clone https://illicitus@bitbucket.org/illicitus/timetotask.git
```
Go to TimeToTask folder
```
cd TimeToTask
```
Install requirements
```
pip install -r requirements.txt
```
Generate SQL database 
```
python manage.py migrate
```
Project is ready to start.

## Testing
To run project tests run:
```
python manage.py test
```

## Extra
To watch statistics tracking run:
```
python manage.py createsuperuser
```
Add username, email and password.
After, you can enter to admin panel and open statistics:
```
http://127.0.0.1:8000/admin/
```
