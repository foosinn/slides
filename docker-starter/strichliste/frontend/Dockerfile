FROM node:12-alpine as builder

ENV VERSION=v1.6.2
ENV PUBLIC_URL=/
WORKDIR /app
RUN npm add yarn
RUN true \
  && wget -O- https://github.com/strichliste/strichliste-web-frontend/archive/${VERSION}.tar.gz | tar xvpzf - --strip-components=1 \
  && yarn install \
  && yarn build

# ---

FROM nginx:alpine

COPY --from=builder --chown=nobody:nobody /app/build /app
ADD default.conf /etc/nginx/conf.d/default.conf