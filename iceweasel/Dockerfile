FROM debian:jessie

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

ADD rootfs/etc/apt/sources.list /etc/apt/sources.list

RUN apt-get -yq update && \
    apt-get install -yq iceweasel fonts-migmix paman sudo libasound2-plugins flashplugin-nonfree flashplugin-nonfree-extrasound

USER docker
ENV HOME /home/docker
ENV PULSE_SERVER tcp:127.0.0.1:4713
