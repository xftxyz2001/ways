#!/bin/sh
docker run \
--name rabbitmq \
--restart unless-stopped \
-p 5672:5672 \
-p 15672:15672 \
--privileged=true \
-v ~/rabbitmq3.12:/var/lib/rabbitmq \
-e RABBITMQ_DEFAULT_USER=admin \
-e RABBITMQ_DEFAULT_PASS=admin \
-d rabbitmq:3.12-management
