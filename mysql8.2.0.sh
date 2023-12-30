#!/bin/sh
docker run \
--name mysql \
-p 3306:3306 \
--restart unless-stopped \
--privileged=true \
-v ~/mysql8.2.0/conf.d:/etc/mysql/conf.d \
-v ~/mysql8.2.0/log:/var/log/mysql \
-v ~/mysql8.2.0/data:/var/lib/mysql \
-v /etc/localtime:/etc/localtime \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql:8.2.0
