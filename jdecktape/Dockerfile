FROM astefanutti/decktape

ARG UID=${UID}
ARG GID=${GID}

# Configure user account
RUN groupadd -g ${GID} docker && \
    useradd -m -d /home/docker -s /bin/bash -u ${UID} -g ${GID} docker

RUN apt-get -yq update && \
    apt-get -yq install fonts-migmix bash

USER docker
ENTRYPOINT ["/decktape/phantomjs", "/decktape/decktape.js"]
CMD ["-h"]
