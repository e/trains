# Test KPN
## Setup

Clone the repository

```
git clone git@github.com:e/trains.git
```

cd into the directory

```
cd trains
```

Create virtualenv

```
virtualenv venv -p `which python3`
```

Activate virtualenv

```
source venv/bin/activate
```

Install requirements

```
pip install -r requirements-dev.txt
```

## To run the tests

```
pytest --cov=departures --cov-report=html -s
```

Then you can navigate to htmlcov/index.html to see the report

![coverage](https://user-images.githubusercontent.com/4753511/108735425-d6f20f80-7530-11eb-8b97-d6bd15bbf676.png)

## To run the development server

```
python manage.py runserver
````

Then you can navigate to http://localhost:8000/departures to see a list of stations with a link to show the departures from each station, and to http://localhost:8000/departures/GVC to see the departures for the assignment

![index](https://user-images.githubusercontent.com/4753511/108735360-c0e44f00-7530-11eb-8c18-1ebd78b02bad.png)

![departures](https://user-images.githubusercontent.com/4753511/108741145-b2993180-7536-11eb-9e32-c0afb496757b.png)
