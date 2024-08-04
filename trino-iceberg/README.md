docker network create --driver=bridge --subnet=172.28.0.0/16 --gateway=172.28.0.1 dev

docker exec -it kafka0 /bin/bash