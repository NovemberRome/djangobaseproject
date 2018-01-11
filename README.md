[![DOI](https://zenodo.org/badge/95352230.svg)](https://zenodo.org/badge/latestdoi/95352230)

# Django Base Project

## About

As the name suggests, this is a basic django project. The idea of this base project is mainly to bootstrap the web application development process through setting up such a Django Base Project which already provides a couple a django apps providing quite generic functionalites needed for building web application bound to the Digital Humanities Domain.

## Install

1. Download or Clone this repo.
2. Rename the root folder of this project `djangobaseproject` and the `djangobaseproject` folder in your projects root folder to the name chosen for your new project (e.g. to `mynewproject`).
3. In all files in the project directory, rename `djangobaseproject` to the name chosen for your new project. (Use `Find and Replace All` feature provided by your code editor.)
4. Adapt the information in `webpage/metadata.py` according to your needs.
5. Create and activate a virtual environment and run `pip install -r requirements.txt`.

## First steps

This project uses modularized settings (to keep sensitive information out of version control or to be able to use the same code for development and production). Therefore you'll have to append a `--settings` parameter pointing to the settings file you'd like to run the code with to all `manage.py` commands.

For development just append `--settings={nameOfYouProject}.settings.dev` to the following commands, e.g. `python manage.py makemigrations --settings=djangobaseproject.settings.dev`.

6. Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Next steps

Build your custom awesome Web App.

## Tests

To get needed software you can run

    pip install -r requirements_test.txt

To run the tests execute

    python manage.py test --settings=djangobaseproject.settings.test
