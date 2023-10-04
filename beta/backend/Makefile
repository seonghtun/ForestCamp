build:
	docker build -t server .
run :
	docker run -it -d --add-host=host.docker.internal:host-gateway --name camp -p 3000:3000 server
exec :
	docker exec -it camp /bin/bash
stop:
	docker stop camp
start : 
	docker start camp
rm :
	docker rm camp
rmi :
	docker rmi server
img :
	docker images
ps :
	docker ps
psa :
	docker ps -a
logs :
	docker logs camp
