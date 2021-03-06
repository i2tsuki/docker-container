# uwsgi docker container
## Descrption
Running uwsgi in docker container.

## Usage
``` sh
# build docker image
docker build -t uwsgi .

# run docker container
ROOTFS=$(readlink -f ./rootfs)
docker run -ti \
           -v ${ROOTFS}/etc/uwsgi:/etc/uwsgi:ro \
		   -v ${ROOTFS}/home/docker/wsgi.py:/home/docker/wsgi.py:ro \
		   uwsgi /bin/bash

# execute command in docker
pip3 install --user werkzeug
cd

docker exec -ti -u 0 uwsgi /bin/bash

# simple container runch
docker run -ti -p 5000:5000 uwsgi

# docker swarm
docker swarm init --listen-addr 127.0.0.1:2377
docker service create --name http --replicas 1 -p 80:5000/tcp uwsgi
docker service ls
docker service rm front
```
