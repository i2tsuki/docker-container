# syntax=docker/dockerfile:1.0-experimental

FROM ubuntu:20.04

RUN apt-get update -yq
RUN apt-get install -yq iproute2 dnsutils iputils-ping

RUN --mount=type=cache,id=apt,target=/var/cache/apt \
    apt-get install -yq language-pack-ja && \
    update-locale LANG=ja_JP.UTF-8
ENV LANG "ja_JP.UTF-8"
ENV LC_ALL "ja_JP.UTF-8"

CMD /bin/bash
