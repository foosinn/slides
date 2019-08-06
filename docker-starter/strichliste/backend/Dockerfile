FROM composer as builder

ENV VERSION=v1.6.1
WORKDIR /app
RUN true \
  && wget -O- https://github.com/strichliste/strichliste-backend/archive/${VERSION}.tar.gz | tar xvzf - --strip-components=1

RUN composer install --no-ansi

# ---

FROM php:7.3-fpm-alpine

RUN true \
  && apk add --virtual=.run mariadb-connector-c libpq libxml2 \
  && apk add --virtual=.build mariadb-connector-c-dev postgresql-dev libxml2-dev \
  && docker-php-source extract \
  && docker-php-ext-install ctype \
  && docker-php-ext-install dom \
  && docker-php-ext-install iconv \
  && docker-php-ext-install json \
  && docker-php-ext-install mbstring \
  && docker-php-ext-install pdo_mysql \
  && Docker-php-ext-install pdo_pgsql \
  && docker-php-ext-install tokenizer \
  && docker-php-ext-install xml \
  && docker-php-source delete \
  && apk del .build

# warum danach?
WORKDIR /app
COPY --from=builder --chown=nobody:nobody /app /app
ADD ./strichliste.env .env
ADD ./strichliste.yaml config/strichliste.yaml

USER www-data
EXPOSE 9000
