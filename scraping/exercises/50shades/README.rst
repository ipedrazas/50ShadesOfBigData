50shades
==============================

Scraping exercises


Deployment
------------

Run these commands to deploy the project to Heroku:

.. code-block:: bash

    heroku create
    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups
    heroku pg:promote HEROKU_POSTGRESQL_COLOR
    heroku config:add DJANGO_CONFIGURATION=Production
    heroku config:add DJANGO_SECRET_KEY=RANDOM_SECRET_KEY
    git push heroku master
    heroku run python 50shades/manage.py syncdb --noinput --settings=conf.settings
    heroku run python 50shades/manage.py migrate --settings=conf.settings
    heroku run python 50shades/manage.py collectstatic --settings=conf.settings