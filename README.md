### django_blog
project from the following course: shorturl.at/hCLZ0
___
# How to install
> ## Docker
1- Clone the repo: `git clone https://github.com/arminadm/django_blog.git`

2- switch to the direction that dockerfile exist

3- use `docker build .` to build the image

4- use `docker run -p 8000:8000 -d <image tag>` to setup the container

> ## without Docker
1- Clone the repo: `git clone https://github.com/arminadm/django_blog.git`

2- install python (version: 3.8) and the requirements: `pip install -r requirements.txt`

3- run the project: `python manage.py runserver`
___
# How to use
After creating superuser using `python manage.py createsuperuser` you can access to admin panel, create any post that you want and adjust other options as many as you need to

you can see the results after your changes on the webpages
