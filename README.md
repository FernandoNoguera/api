# Django api weather

## Stack
- Django 
- Django Rest Framework 
- Redis 
- Channel 

### Create and activate your virtual enviroment

```
$ virtualenv .venv
$ source .venv/bin/activate
```

### Install all packages

```
$ pip install -r requirements.txt

```

### Create postgres user and database
`$ sudo -u posgres psql`

```sql
CREATE DATABASE api_db;
CREATE USER root WITH PASSWORD '1234';
ALTER ROLE root SET client_encoding TO 'utf8';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE api_db TO root;
```

### configure your .env file

```
$ cp api/.env.sample api/.env
```

### Run migrations on database

```
$ python manage.py migrate
```


### Run server

```
$ python manage.py runserver
```

### URL for published documentation

https://documenter.getpostman.com/view/14482878/2s935kN5S1