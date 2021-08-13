# FEED-NEWS-SCRAPER-DJANGO-PROJECT

## Introduction
Django based REST API service for financial news. Service have two parts: REST api service and scraping service.
REST API is used for fetching data and scraping service will collect and store data from Yahoo finance site.
Scraper service will use Yahoo RSS feed for collecting data ([https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US](https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US), getting data for AAPL symbol Apple Inc)
Scraping service collect news for following symbols, AAPL, TWTR, GC=F(GOLD), INTC

Scraper service will use celery extension [https://github.com/celery/django-celery-beat](https://github.com/celery/django-celery-beat)

**Project is Dockreized (services are run in Docker containers)**
Docker version: **v3.9**
Docker is creating a base image using Python with version: **v3.9.6**
Docker-compose one container with four services
 - **db:**  Creates a db volume and uses PostgreSQL https://hub.docker.com/_/rabbitmq
 - **web:** Project in build on using python command to run a development server
 -  **rabbitmq:** Message broker also it creates rabbitmq monitor panel
 -  **celery_worker:** this service only use celery command
 
 ### Docker images
 Application uses in docker hub three images
 ***Hint:** more detail about images are in links. There  you can find all documentation about them*
 
 - **PostgreSQL:**  https://hub.docker.com/_/postgres
 - **RabbitMQ:**  https://hub.docker.com/_/rabbitmq
 - **Celery:** https://hub.docker.com/_/celery

## Instalation
Clone project from this github repository.

    git clone repository-url project-name

When the project is donwloaded in the root file there is `Dockerfile`, `docker-compose.yml` and `requirements.txt`.
These files will be used only for running the project docker container.
Docker container will run Python install package manager `pip` it will install and manage additional libraries and dependencies.

The first command is to run docker container run services and migrate the database.

    docker-compose run web python NewsProject/manage.py migrate

This command will migrate databases and also project.

Then create superuser to access admin panel `http://localhost:8000/admin/` using this command

    docker-compose run web python NewsProject/manage.py createsuperuser

Then we build a project

    docker-compose build

This command will do all process that we specified in `Dockerfile`, `docker-compose.yml` and `requirements.txt`. It will create a base image using Python create all services with images and install libraries and dependencies.

When everything is installed, now start all services and images using the command

    docker-compose up

This command will run all images and development server will be available  `http://localhost:8000/`**
**Hint:** To access /api/articles/ use superuser to login*

## Additional requirements
### Starting celery beat
When starting the docker container we also use the celery command to activate one worker to find periodic tasks that are running at a certain time. To start using celery beat in terminal run command new command
**Hint:** Celery beat proccess will start evey 60 seconds, To check if worker is activate go back in terminal where you start `docker-compose up`

    docker-compose run web sh -c "cd NewsProject && celery -A NewsProject beat --loglevel=info"

This command will monitor rss news feeds and store them in database. In `NewsProject/celery.py` you can find all beat scheadule. For evey beat it checks difrent news symbols

### Running tests
All tests can be found in direcotry `NewApi/tests/`
Command that you run tests in container is

    docker-compose run web sh -c "cd NewsProject && python manage.py test --debug-mode"
For developming testing use command `python manage.py test --debug-mode` in NewsProject folder

### RabbitMQ managment tool
For monitoring celery beat schedules you can see in managment tool http://localhost:15672/#/

### Other
**Hint:** To access articles api list use `/api/articles/` route