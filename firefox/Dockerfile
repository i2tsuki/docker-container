FROM debian:jessie

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker && \
    groupadd -g 18 alsa && \
    gpasswd -a docker alsa

RUN yes "toor" | passwd

ADD rootfs/etc/apt/sources.list /etc/apt/sources.list
RUN apt-get -yq update && apt-get -yq upgrade
RUN apt-get install -yq firefox-esr fonts-migmix flashplugin-nonfree flashplugin-nonfree-extrasound browser-plugin-freshplayer-pepperflash alsa-utils

USER docker
ENV HOME /home/docker
