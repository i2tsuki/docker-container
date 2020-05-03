# syntax=docker/dockerfile:1.0-experimental

FROM ubuntu:19.10

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

# Ref: https://wiki.winehq.org/Ubuntu
RUN --mount=type=cache,id=apt,target=/var/cache/apt \
    dpkg --add-architecture i386 && \
    apt-get -yq update && \
    apt-get -yq install software-properties-common curl
RUN curl -LO "https://dl.winehq.org/wine-builds/winehq.key" && \
    apt-key add winehq.key && \
    apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' && \
    apt-get -yq update

RUN --mount=type=cache,id=apt,target=/var/cache/apt \
    apt-get -yq install --install-recommends winehq-staging
RUN --mount=type=cache,id=apt,target=/var/cache/apt \
    DEBIAN_FRONTEND='noninteractive' apt-get -yq install calibre winetricks winbind

RUN --mount=type=cache,id=apt,target=/var/cache/apt \
    apt-get install -yq language-pack-ja && \
    update-locale LANG=ja_JP.UTF-8

RUN yes "toor" | passwd

RUN locale-gen ja_JP.UTF-8

USER docker
WORKDIR "/home/docker"
ENV HOME "/home/docker"
ENV LANG "ja_JP.UTF-8"
ENV LC_ALL "ja_JP.UTF-8"

ENV WINEARCH "win64"

CMD /bin/bash
