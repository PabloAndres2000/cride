# Cride Backend

## Before starting

See `Deployment` and `Pre-requisites` to know how to install and deploy the project

## Pre-requisites

- Docker
- Docker-compose

## Docker Commands

It's good practice in a way that you know how docker-compose works without first using the `export COMPOSE_FILE=local.yml`. I leave a brief summary

"""
dokcer-compose -f local.yml up
-- Run the application
"""

"""
docker-compose -f local.yml build
-- Rebuild docker image
"""

"""
docker-compose -f local.yml down
-- Stop and remove docker containers
"""

## Or change previous commands docker for docker-compose ...

This command `export COMPOSE_FILE=local.yml` is used to enable the use of docker-compose up, etc. without using -f local.yml ..

"""
docker-compose up
-- Run the application
"""

"""
docker-compose build
-- Rebuild docker image
"""

"""
docker-compose down
-- Stop and remove docker containers
"""

## Administrative commands

`export COMPOSE_FILE=local.yml`

"""
docker-compose run --rm django python manage.py createsuperuser
-- Create superuser
"""

## Enable debugger and remove django container

A good practice is to separate django from postgres, redis and celery, because this will allow us to run django separately so that it allows us to iterate with it. The others will continue running normally, but separate from django.

"""
docker-compose up
-- Run the application
"""

"""
docker-compose ps
-- See the containers that run
"""

"""
docker rm -f `NAME -> Django `
-- Remove Django service
"""

"""
docker-compose run --rm --service-ports django
-- detach Django services
"""
