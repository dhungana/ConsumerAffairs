FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3 libmysqlclient-dev
RUN echo 'ServerName localhost\n' >> /etc/apache2/apache2.conf
COPY ./consumer_affairs_site.conf /etc/apache2/sites-available/000-default.conf
RUN service apache2 restart
RUN ln -f /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln -f /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 80 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
