sudo apt update
sudo apt install docker-compose
sudo systemctl start docker
docker-compose up -d --build
docker ps
curl http://localhost:5007
docker-compose logs -f
docker exec -it flask-app bash
ls , pip list , exit

