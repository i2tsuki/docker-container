# uwsgi docker container
## Descrption
Running uwsgi in docker container.

## Usage
``` sh
# build docker image
docker build -t uwsgi . && rm -fv ./Dockerfile

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

# docker swarm
```
