#!/bin/sh
docker run \
--name=mongodb \
--restart=unless-stopped \
-p 27017:27017 \
--privileged=true \
-v ~/mongo6.0.12/data:/data/db \
-v ~/mongo6.0.12/conf:/data/configdb \
-v ~/mongo6.0.12/backup:/data/backup \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=123456 \
-d mongo:6.0.12 --auth
