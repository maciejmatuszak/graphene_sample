Sample GraphQL Service
======================

Overview
--------
This is sample GraphQL service based on Django and Graphine

Usage
------
To run the service in dev environment follow the following steps:
1. Best create Virtual environment using your preferred tool. This will avoid contamination of your system python environment with requirements specific to this project
2. Install the required dependencies from `requirements.txt`
```shell
python -m pip install -r ./requirements.txt 
```
3. Initialise the database
```shell
python manage.py migrate
```


Development steps (for reference)
-------------------------------
1. Create project using `django-admin`:
```shell
django-admin startproject people_service
```

2. Initialise the database
```shell
python manage.py migrate
```

3. Run dev server
```shell
python manage.py runserver
```

4. Graphine integration
