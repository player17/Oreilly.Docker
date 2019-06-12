Docker первое знакомство !
==========================
* https://github.com/using-docker

Чистим Doker локальный
----------------------
* `docker images` // Список образов
* `docker ps -a` // Список всех контейнеров
* `docker rm $(docker ps -aq)` // Удалить работающие контейнеры
* `docker rm -v $(docker ps -aq -f status=exited)`  // Удалить остановленые контейнеры
* `docker rmi -f $(docker images -q)`  // Удалить все образы // -f силовое удаление

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
* `docker images` // Список созданных образов
* `docker stop $(docker ps -q)`  // Остановить работающие контейнеры
* `docker rm $(docker ps -aq)` // Удалить контейнеры
* `docker rmi -f $(docker images -aq)` // Удалить образы
* `docker-compose build` // Перестроить + Скачать образы из docker-compose.yml
* `docker-compose up -d`  // Запустить в фоновом режиме из docker-compose.yml // Ctrl + С выход из консоли
* `http://127.0.0.1:5000`  // Приложение доступно для работы

Разное
------
* `docker build -t identidock .`  // Создаем образ identidock из dockerfile
* `docker run --name identidock -e "ENV=DEV" -p 5000:5000 identidock`  // Запоускаем образ под разработчиком на 5000 порту (http://127.0.0.1:5000) из dockerfile


