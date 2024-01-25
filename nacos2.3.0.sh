#!/bin/sh
docker run \
--name=nacos \
--restart=unless-stopped \
-p 8848:8848 \
-p 9848:9848 \
-p 9849:9849 \
--privileged=true \
-v ~/nacos2.3.0/conf:/home/nacos/conf \
-v ~/nacos2.3.0/logs:/home/nacos/logs \
-e MODE=standalone \
-d nacos/nacos-server:v2.3.0
