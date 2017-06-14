FROM debian:jessie

# Configure user account
ARG UID=${UID}
ARG GID=${GID}

# Backports for stretch
COPY ./rootfs/etc/apt/sources.list.d/stretch.list /etc/apt/sources.list.d/stretch.list

RUN apt-get update -yq && apt-get upgrade -yqq
