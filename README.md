# multidiscipline-project-backend

## Setup

Clone the repository:

```sh
$ git clone git@github.com:thanhlam152/multidiscipline-project-backend.git
$ cd multidiscipline-project-backend
```

Create a virtual environment to install dependencies in and activate it (on Mac):
```sh
$ python3 -m venv venv
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:
```sh
(venv)$ pip3 install -r requirements.txt
```
## Set up environment for project
You can view the required fields in file `example.env`.
Then create a file `.env` and fill all the required fields based to your own settings.

You can view the file `backend/settings.py` to understand what these fields used for.


## Migrate database

```sh
(venv)$ python3 manage.py makemigrations
(venv)$ python3 manage.py migrate
```

## Create admin account
```sh
(venv)$ python3 manage.py createsuperuser
```

## Run server
```sh
(venv)$ python3 manage.py runserver
```

## Run notification service
```sh
(venv)$ python3 adaFruitConnection.py
```

# Important note
To send to the correct machine, be sure to swap the Expo token in adaFruitConnection.py and notification.py according 
to what the terminal print when open notification tab of the mobile app.  
