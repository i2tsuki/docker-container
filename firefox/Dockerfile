FROM debian:sid

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

ADD rootfs/etc/apt/sources.list /etc/apt/sources.list

RUN apt-get -yq update && apt-get -yq upgrade
RUN apt-get install -yq firefox-esr fonts-migmix flashplugin-nonfree flashplugin-nonfree-extrasound

USER docker
ENV HOME /home/docker
ENV PULSE_SERVER tcp:127.0.0.1:4713
