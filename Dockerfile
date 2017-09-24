FROM python:2.7-alpine3.6

RUN set -xe ;\
    pip install pipenv

WORKDIR /opt/app
COPY Pipfile      /opt/app
COPY Pipfile.lock /opt/app

# Haha
RUN set -xe ;\
    pipenv lock -r > requirements.txt ;\
    pip install -r requirements.txt
