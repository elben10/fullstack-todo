ARG NODE_VERSION
ARG NGINX_VERSION

FROM node:${NODE_VERSION} as requirements-stage

WORKDIR /src

COPY . /src

RUN yarn install

RUN yarn build

FROM nginx:${NGINX_VERSION}

COPY --from=requirements-stage /src/build/ /usr/share/nginx/html