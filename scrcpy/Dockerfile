# syntax=docker/dockerfile:1.0-experimental

FROM debian:sid

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

RUN yes "toor" | passwd

RUN apt-get -yq update && \
    apt-get install -yq scrcpy

USER docker
WORKDIR /home/docker

ENV LANG "ja_JP.UTF-8"
ENV LC_ALL "ja_JP.UTF-8"
ENV HOME /home/docker
ENV PULSE_SERVER /run/pulse/native

CMD /bin/bash
