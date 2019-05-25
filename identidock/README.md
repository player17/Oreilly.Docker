docker rm -v $(docker ps -aq -f status=exited)
docker rm $(docker stop ps -q)  // Не работает

docker stop $(docker ps -q) // Остановить работающие контейнеры
docker rm $(docker ps -aq)  // Удалить работающие контейнеры
docker rmi $(docker images -aq)

ВАЖНО: если глячать пути к файлам - перезгрузи Docker for Windows
https://stackoverflow.com/questions/48586868/oci-runtime-create-failed-container-linux-go296-no-such-file-or-directory

// page 85
-- Flask
docker build -t identidock .

docker run -p 5000:5000 -v %cd%/app:/app identidock
docker run -p 5000:5000 -v ${pwd}/app:/app identidock

// page90
-- uWSGI
docker build -t identidock2 .

docker run -p 9090:9090 -p 9191:9191 -v %cd%/app:/app identidock2
docker run --name identidock2 -p 9090:9090 -p 9191:9191 -v %cd%/app:/app identidock2
curl localhost:9090
curl localhost:9191

// page93
/*
USER root
RUN chmod 755 identidock.py
USER uwsgi
*/
CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", \
 "--callable", "app", "--stats", "0.0.0.0:9191"]
docker exec -it basg


docker stop $(docker ps -q) // Остановить работающие контейнеры
docker rm $(docker ps -aq)  // Удалить работающие контейнеры
docker rmi $(docker images -aq)

docker build -t identidock3 .
docker run --name identidock3 -e "ENV=DEV" -p 5000:5000 identidock3

-- Неработает
docker build -t identidock3 .
docker run --name identidock3 -e "ENV=DEV" -p 5000:5000 -v %cd%/app:/app identidock3
docker inspect identidock3

// Хак косяков книги
COPY app /app
COPY tmp /app

EXPOSE 9090 9191
USER uwsgi

CMD ["./cdm.sh"]

// Start pdroject
docker build -t identidock3 .
docker run --name identidock3 -e "ENV=DEV" -p 5000:5000 identidock3

// Page 116
// Create Automated Build Docker hub


