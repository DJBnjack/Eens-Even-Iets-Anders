docker build -t eens .
docker kill eens
docker rm eens
docker run -d -p 8888:8888 --name eens eens 