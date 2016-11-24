Merging branches safely: http://stackoverflow.com/questions/14168677/merge-development-branch-with-master

# Crescendo-Music-Education-v2
A relaunch of the CME website using Django & Nginx hosted on Digitalocean cloud service.

Live: http://104.236.23.31/

Dev environment: https://cme-dev-env-a2017jlee.c9users.io/

### WARNING:
Changed must be manually synced to the server using SFTP

## TODO:
### Create Static Pages
- [x] Create index.html

- [ ] Create about/story.html
- [ ] Create about/mission.html
- [ ] Create about/directors.html

- [x] Create join/tutors.html
- [ ] Create join/students.html
- [ ] Create join/information.html

- [ ] Create services/performances.html
- [ ] Create services/structure.html
- [ ] Create services/tutors.html

- [ ] Create information/curriculum.html
- [ ] Create information/general.html

- [ ] Create media/gallery.html
- [ ] Create media/news.html

- [ ] Create contact.html

### Update metadata for SEO
### Create signup pages
### Create tutors page (currently using TypeForm)


## C9 Basics
Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://cme-dev-env-a2017jlee.c9users.io/' and the admin page from 
'https://cme-dev-env-a2017jlee.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide
