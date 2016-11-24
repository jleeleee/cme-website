# Crescendo Music Education Website

A relaunch of the CME website using Django & Nginx hosted on Digitalocean cloud service.

Live: http://104.236.23.31/

Dev environment: https://cme-dev-env-a2017jlee.c9users.io/

#### Note:
* Changed must be manually synced to the server using SFTP
* Home page is not templated due to its completely different structure
* Merging branches safely: http://stackoverflow.com/questions/14168677/merge-development-branch-with-master


#### TODO:
Task | Status
    ---|---
index.html | Done
about/story.html | Not Started
about/mission.html | Not Started
about/directors.html | Not Started
join/tutors.html | Done
join/students.html | Not Started
join/information.html | Not Started
services/performances.html | Not Started
services/structure.html | Not Started
services/tutors.html | Not Started
information/curriculum.html | Not Started
information/general.html | Not Started
media/gallery.html | Not Started
media/news.html | Not Started
contact.html | Not Started
**Metadata for SEO** | **TBD**
**Signup pages** | **TBD**
**Tutor Account Pages** | **TBD**
---
### C9 Settings
Application: 'https://cme-dev-env-a2017jlee.c9users.io/'

Admin Page: 'https://cme-dev-env-a2017jlee.c9users.io/admin'.

#### Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
#### Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.
