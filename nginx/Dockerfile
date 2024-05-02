FROM nginx:1.25

RUN mkdir -p /var/www/static
RUN mkdir -p /var/www/media
COPY ./static/ /var/www/static/
COPY ./media/ /var/www/media/

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d