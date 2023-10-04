build:
	docker build -t myredis .
run:
	docker run -p 5000:6379 -d --name myredis myredis 
exec:
	docker exec -it myredis redis-cli
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
