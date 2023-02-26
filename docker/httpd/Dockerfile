FROM httpd:2.4

COPY httpd-proxy.conf /usr/local/apache2/conf/extra/
RUN echo "Include conf/extra/httpd-proxy.conf" >> /usr/local/apache2/conf/httpd.conf
