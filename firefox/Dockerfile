# syntax=docker/dockerfile:1.0-experimental

FROM ubuntu:20.04

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

RUN yes "toor" | passwd

RUN apt-get -yq update && \
    apt-get install -yq firefox && \
    apt-get install -yq fonts-migmix

RUN apt install -y pepperflashplugin-nonfree browser-plugin-freshplayer-pepperflash flashplugin-installer

RUN --mount=type=cache,id=apt,target=/var/cache/apt \
    apt-get install -yq language-pack-ja && \
    update-locale LANG=ja_JP.UTF-8
ENV LANG "ja_JP.UTF-8"
ENV LC_ALL "ja_JP.UTF-8"

USER docker
ENV HOME /home/docker
ENV PULSE_SERVER /run/pulse/native

CMD /bin/bash
