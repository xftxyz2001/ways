#!/bin/sh
docker run \
--name redis \
--restart unless-stopped \
-p 6379:6379 \
--privileged=true \
-v ~/redis7.2.3/data:/data \
-v ~/redis7.2.3/redis.conf:/etc/redis/redis.conf \
-d redis:7.2.3 \
redis-server /etc/redis/redis.conf \
--appendonly yes \
--requirepass 123456
