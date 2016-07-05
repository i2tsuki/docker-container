FROM debian:jessie

# Configure user account
RUN groupadd -g 1000 uwsgi && \
    useradd -m -d /home/docker -s /bin/bash -u 1000 -g 1000 docker

RUN apt-get -yq update && \
    apt-get install -yq curl python3-pip uwsgi uwsgi-plugin-python3 uwsgi-plugin-router-access

RUN mkdir -pv /var/run/uwsgi

USER docker
ENV HOME /home/docker
