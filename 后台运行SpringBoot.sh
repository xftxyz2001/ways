PID=$(ps -ef | grep app.jar | grep -v grep | awk '{ print $2 }')
if [ -z "$PID" ]
then
    echo Application is already stopped
else
    echo kill -9 $PID
    kill -9 $PID
fi
nohup java -jar rocketblog/target/app.jar >> applog &
