FROM node:14.16-alpine as build

RUN apk add git openssh-client

# In order to be able to install packages from private
# repos we need to inject an ssh secret key
RUN mkdir -p /root/.ssh
COPY ssh /root/.ssh
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# This line is actually important, otherwise OS complains about 
# secret_key being too accessible
RUN chmod 0600 /root/.ssh/secret_key

WORKDIR /usr/app

COPY package*.json .
RUN npm install

COPY . .
RUN npm run build

FROM nginx:1.19.8-alpine

COPY --from=build /usr/app/dist /usr/share/nginx/html

# The image will run /docker-entrypoint.d/20-envsubst-on-templates.sh
# which runs envsubst on /etc/nginx/templates/nginx.conf.template to 
# /etc/nginx/conf.d/nginx.conf
COPY nginx/nginx.conf.template /etc/nginx/templates/nginx.conf.template
