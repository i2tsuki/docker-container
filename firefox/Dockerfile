# syntax=docker/dockerfile:1.0-experimental

FROM debian:stretch

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker && \
    groupadd -g 18 alsa && \
    gpasswd -a docker alsa

RUN yes "toor" | passwd

ADD rootfs/etc/apt/sources.list /etc/apt/sources.list
RUN --mount=type=cache,id=apt-cache,target=/var/cache/apt \
    --mount=type=cache,id=apt-state,target=/var/lib/apt \
    apt-get -yq update && \
    apt-get install -yq -t unstable firefox && \
    apt-get install -yq fonts-migmix curl wget sudo
RUN curl https://raw.githubusercontent.com/cybernova/fireflashupdate/master/fireflashupdate.sh -O && \
    chmod +x fireflashupdate.sh && \
    ./fireflashupdate.sh

USER docker
ENV HOME /home/docker
