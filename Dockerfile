FROM python:3.7-alpine
MAINTAINER Tuvshin-dev


ENV PYTHONNUNBUFFERED 1 
# apk package management from python alpine
COPY ./requirements.txt /requirements.txt
# those are all temporary dependencies for installing python packages
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# after install del temp-requirements
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# that creates another user with name user and docker swtiches to user
# if do not do that we person who clones this image will manipulates root access
RUN adduser -D user
USER user