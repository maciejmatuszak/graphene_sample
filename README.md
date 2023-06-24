Sample GraphQL Service
======================

Overview
--------
This is sample GraphQL service based on Django and Graphene

Assumption
----------

1. This is demo project to demonstrate GraphQL implementation using Django and Graphene
2. The project template generate potentially superfluous code related to authentication, authorisation, storage,
   debugging etc... Those should be evaluated and potentially updated for production system. For the purpose of the demo
   those are left with minimal changes.
3. Security, authorisation, authentication concerns has not been evaluated.
4. The Django project template create users table that is compatible with default authentication authorisation
   mechanism. For the purpose of this demo separate table and domain model has been created to closer match
   requirements.

Usage
------
To run the service in dev environment follow the following steps:

1. Best create Virtual environment using your preferred tool. This will avoid contamination of your system python
   environment with requirements specific to this project
2. Install the required dependencies from `requirements.txt`

```shell
python -m pip install -r ./requirements.txt 
```

3. Initialise the database

```shell
python manage.py migrate
```
4. Start the dev server

```shell
python manage.py runserver
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

4. Graphene integration

* added `graphene_django` app to the list
* added GRAPHANE configuration - pointer to schema object
* added separate app `people` to keep the people and addresses domain models and Graphene implementations

5. Update db schema migration scripts
   New model has been added for `Person` the db schema has to be updated.

```shell
python manage.py makemigrations
python manage.py migrate
```

* `makemigrations` generates migration scripts that update the database tables,
* `migrate` will apply the updated schema.
