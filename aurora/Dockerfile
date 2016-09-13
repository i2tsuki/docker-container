FROM debian:sid

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

ADD rootfs/etc/apt/sources.list /etc/apt/sources.list

RUN apt-get -yq update && \
    apt-get -yq install debian-keyring
RUN apt-get install -yq pkg-mozilla-archive-keyring
RUN gpg --batch --check-sigs --fingerprint --keyring /etc/apt/trusted.gpg.d/pkg-mozilla-archive-keyring.gpg --keyring /usr/share/keyrings/debian-keyring.gpg pkg-mozilla-maintainers
RUN apt-get install --allow-unauthenticated -yq -t experimental firefox

USER docker
ENV HOME /home/docker
ENV PULSE_SERVER tcp:127.0.0.1:4713
