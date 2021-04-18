FROM node:14.16-alpine as build

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
