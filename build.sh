docker stop dynamicdns
docker rm dynamicdns
docker build -t dynamicdns .
docker create --name dynamicdns --restart unless-stopped dynamicdns:latest
docker start dynamicdns
