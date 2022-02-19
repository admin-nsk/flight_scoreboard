Проект тобло авиаперелетов
===
***

Данный проект использует стек: Python 2.7, Django 1.9, DRF 3.5.1

В проекте главная страница выводит табло аиварейсов с указанием
* Номера рейса
* Города вылета
* Города прилета
* Плановой даты и времени вылета
* Плановой даты и времени прилета
* Статуса авиарейса

В проекте доступны REST API для работы рейсами

Документация по API генерируется автоматически и доступна по адресу
```http://localhost:8000/swagger_api/```


***
## Развертивание в ручном режиме

1. Для запуска проекта необходимо проверить, установлен ли Python 2.7 на сервер <br/>
```$ python -v```<br/>
2. Если Python не установлен, то установить <br/>
```$ sudo apt install python2```
3. Установить Git<br/>
```$ sudo apt-get install git```
4. Cкачать код проекта с github<br/>
```$ git pull https://github.com/admin-nsk/flight_scoreboard```
5. Перейти в папку с проектом, создать виртуальное окружение и активировать его<br/>
```$ cd project_dir```<br/>
```$ python2 -m venv venv```<br/>
```$ source ./env/bin/activate```
6. Установить зависимости проекта<br/>
```$ pip install -r requirements.txt```
7. Установить supevisor<br/>
```$ sudo apt install supervisor```
8. Создать скрипт запуска gunicorn<br/>
```$ vim /home/www/code/project/bin/start_gunicorn.sh```<br/>
С кодом:<br/> 
```
    #!/bin/bash
    source /home/www/code/project/env/bin/activate
    source /home/www/code/project/env/bin/postactivate
    exec gunicorn  -c "/home/www/code/project/gunicorn_config.py" project.wsgi
```
9. Установить права на выполнение<br/>
10. Создать конфигурационный файл<br/>
```$ vim project/supervisor.testserver.conf```
```
C содержимым:
[program:www_gunicorn]
	command=/home/www/code/project/bin/start_gunicorn.sh
	user=www
	process_name=%(program_name)s
	numprocs=1
	autostart=true
	autorestart=true
	redirect_stderr=true
```
11. Установить Gunicorn<br/>
```$ pip install gunicorn```
12. Создать конфигурационный файл Gunicorn
```
С содержимым:
    command = '/home/www/code/project/env/bin/gunicorn'
    pythonpath = '/home/www/code/project/project'
    bind = '127.0.0.1:8001'
    workers = 3
    user = 'www'
    limit_request_fields = 32000
    limit_request_field_size = 0
    raw_env = 'DJANGO_SETTINGS_MODULE=project.settings'
```
14. Установить Nginx
` $ sudo apt-get install nginx`
15. Запустить supervisor<br/>
` $ sudo systemctl start supervisor`
16. Образец конфигурационного файла для Nginx лежит в дериктории **_deploy_**


