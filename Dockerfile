FROM python:3.6.8
MAINTAINER hjpotter92 <hjpotter92+github@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/app && python -m pip install -U pip pipenv
WORKDIR /opt/app
ADD Pipfile Pipfile.lock ./
RUN pipenv install --ignore-pipfile --deploy
COPY ./ ./
RUN pipenv run ./manage.py migrate && pipenv run ./manage.py loaddata default_admin

EXPOSE 8000
CMD pipenv run ./manage.py runserver 0.0.0.0:8000
