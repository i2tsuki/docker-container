FROM debian:jessie

# Configure user account
RUN groupadd -g 1000 uwsgi && \
    useradd -m -d /home/docker -s /bin/bash -u 1000 -g 1000 docker

RUN apt-get -yq update && \
    apt-get install -yq curl python3-pip uwsgi uwsgi-plugin-python3 uwsgi-plugin-router-access

RUN mkdir -pv /var/run/uwsgi

ADD rootfs/etc/uwsgi /etc/uwsgi
ADD rootfs/home/docker /home/docker

EXPOSE 5000
USER root
CMD uwsgi /etc/uwsgi/emperor.yaml
