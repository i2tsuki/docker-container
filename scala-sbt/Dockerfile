FROM hseeberger/scala-sbt

ARG UID=${UID}
ARG GID=${GID}

# Configure user account
RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

RUN apt-get -yq update && \
    apt-get -yq install bash

USER docker
ENV HOME /home/docker
WORKDIR /home/docker
