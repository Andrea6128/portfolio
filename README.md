# portfolio
Personal portfolio site made in Django.

## requirements
requirements.txt

## install
- extract the archive
- create venv in the project root dir
- run your database server
- create a database called 'portfolio'
- edit settings.py db login credentials
- do migrations '''python3 manage.py migrate'''
- create your superuser '''python3 manage.py createsuperuser'''
- additionally fill up your db with fixtures
'''python3 manage.py loaddata db-fixture.json'''
- '''python3 manage.py runserver'''
- go to http://127.0.0.1/8000 in your browser
