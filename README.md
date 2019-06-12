Docker первое знакомство
========================

Чистим Doker локальный
----------------------
* docker images // Список образов
* docker ps -a // Список всех контейнеров
* docker rm $(docker ps -aq)  // Удалить работающие контейнеры
* docker rm -v $(docker ps -aq -f status=exited)  // Удалить остановленые контейнеры
* docker rmi -f $(docker images -q)  // Удалить все образы // -f силовое удаление

Git Hub
-------
* pull // Сливаем удаленный репозиторий
* commit // Ctrl + K
* push // Ctrl + Shift + K

Docker Hub
----------
* После push в git в docker hub срабатывает автопостроение // проверяем результат построения

Docker local
------------
* Переходи в директорию проекта // Папку расшариваем
* docker build -t identidock .  // Создаем образ identidock из docker-compose.yml
* docker run --name identidock -e "ENV=DEV" -p 5000:5000 identidock  // Запоускаем образ под разработчиком на 5000 порту (127.0.0.1:5000)

