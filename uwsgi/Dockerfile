FROM debian:stretch

ARG UID=${UID}
ARG GID=${GID}

# Configure user account
RUN groupadd -g ${GID} uwsgi && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

RUN apt-get -yq update && \
    apt-get install -yq curl python3-pip uwsgi uwsgi-plugin-python3 uwsgi-plugin-router-access

RUN apt-get install -yq lsof socat

RUN mkdir -pv /var/run/uwsgi

ADD rootfs/etc/uwsgi /etc/uwsgi
ADD rootfs/home/docker /home/docker

EXPOSE 5000
USER root
CMD uwsgi /etc/uwsgi/emperor.yaml
