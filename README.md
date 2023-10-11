## 10x Genomics Platform Engineering Technical Coding Prompt

### The project

Create a web service that converts a CSV file into an API that exposes JSON, as specified in `README_PROJECT.md`. This is a copy of the readme file from https://raw.githubusercontent.com/aos-10x/10x-platform-eng-interview-prompt/master/README.md, the reason for the copy is that the repo may change over time (or access may change), so want to properly capture the project requirements at the time of writing the project.

This project completes the initial task and the first bonus task, to run with Docker. 

For tests I setup and used pytest. I ran them locally, there is most likely better practices in production, however I think should still convey my general ability to think about tests, write them, etc. Note that my background is a java background. With this exercise, I've tried to map a lot of my java understanding to python, as such, I may have made some mistakes. I'm noting details of what I did, so we can discuss them, in case there is a better way, or more standard way.

### Run and Test the application with
docker build -t weather-app .
docker run -p 8000:8000 weather-app

Test with the following links, and with any other valid filter criteria (should work for all fields and exact data matches):
http://127.0.0.1:8000/weather/query?limit=5 
http://127.0.0.1:8000/weather/query?date=2012-06-04 
http://127.0.0.1:8000/weather/query?weather=rain 
http://127.0.0.1:8000/weather/query?weather=rain&limit=5 
http://127.0.0.1:8000/weather/query?weather=rain&limit=20

TODO: Note that http://127.0.0.1:8000/weather/query?blah=2&foo=3 Fails, an improvement would need to address so if parameters don't align with columns that it wouldn't fail like it currently does.

#### Project layout
`./` - contains various modules used in the application. Originally had different folder layout. This also contains the Dockerfile you should be able to use to run and test the application. TODO: There should be a more standard way to organzie the files. 
`./django_project` - folder I used for django setup
`./resources/` - contains non-source related files, e.g. seattle-weather.csv which contains the base data we are referencing.
`./tests/` - contains test related files. Tests are written with pytest. 
`Dockerfile` - contains details on Docker setup
`LICENSE` - Did best practices of including a liencse file, used MIT License, since nothing really needed.

#### Notes 

This is more of a reference for myself, as I used this as a learning exercise. I'm putting misc notes for myself and and URLs I used as part of the project. There was a lot more, but this is a cleaned up and shorter version of notes I had.

https://www.atlassian.com/git/tutorials/saving-changes/gitignore
https://docs.python-guide.org/writing/structure/
https://djangoforbeginners.com/hello-world/

#### Virtual Enviornment
cd ~/workspace/10xGenomics
pip3 install -U virtualenv
virtualenv 10xGenomics
pip3 install pytest
pip3 install django

Now that the server is running, lets make custom endpoint for the weather api.

django-admin startproject django_project .
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py startapp weather
python manage.py runserver  

Ctrl+C to exit, server running locally
deactivate, to end virtual environment 

# Docker Stuff
docker build -t weather-app .
docker run -p 8000:8000 weather-app
Test with http://127.0.0.1:8000/weather/query?weather=rain&limit=5 and http://127.0.0.1:8000/weather/query?weather=rain&limit=20

# Unit Tests
Searched and looks like there are two common options for unit tests. PyTest and unittest. PyTest looked to be simpler/cleaner, so my tests use PyTest.

To install use:
pip3 install pytest

https://www.tutorialspoint.com/pytest/pytest_identifying_test_files_and_functions.htm

From main project directory run 
`pytest tests/`

This ran all of the tests in the weather_test.py file. This could use more time to get the setup and tear down to work properly. I could also segment better to align with better unit tests. It also seems like there may be a more standard way for tests with Django, as per the 2nd bonus portion. 

#### Other Potential to TODOs

Check Style, see if way to auto format to align with PEP8 and other best practice standards. 
Other static analysis, e.g. SonarQube, etc.
Security scans
Cyclomatic Complexity scans

There are various notes throughout the practical for things I'd improve upon before submitting code for production. I've noted many comments with `TODO` with notes to myself.

#### Docstring
From what I could find PEP8 looks to be the gold bar standard for documentation. I'm not 100% sure, if I'm following them fully, however I've referenced them and tried to make the code look similar to the examples I found. For example: 

* https://peps.python.org/pep-0008/
* https://peps.python.org/pep-0257/

