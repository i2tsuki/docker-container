FROM astefanutti/decktape

ARG UID=${UID}
ARG GID=${GID}

USER root
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk add --update --no-cache font-ipa@testing bash font-noto font-noto-emoji@testing

USER node
ENTRYPOINT /bin/bash
