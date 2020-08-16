# pull official base image
FROM python:3.8.3-alpine
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache --virtual .build-deps-edge \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
  gdal-dev \
  geos-dev \
  proj-dev \
  gdal \
  geos \
  proj

RUN apk add --update curl gcc g++
 
RUN pip install --upgrade pip

RUN addgroup -S django \
  && adduser -S -G django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
  && rm -rf /requirements

COPY . /app
RUN chown -R django /app

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start

RUN chown -R django:root /app/staticfiles

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
