# Кабинеты

## Задание

> Необходимо создать сайт с админ панелью и 2-мя кабинетами на Flask или Django.
> Сайт может быть не оформлен красиво.
> Структура на выбор.
> Можно взять за основу сайт kwork.ru.
> На сайте помимо админки должны быть два кабинета заказчика и исполнителя.
> Минимальный набор полей в профилях (имя, контактные данные, опыт). БД PostgreSQL

## Использованные технологии

-   python: 3.12
-   django: 5.0.4
-   psycopg2-binary: 2.9.9
-   environs: 11.0.0
-   pillow: 10.3.0

## Данные для демонстрации

При использовании данных для демонстрации из фикстуры, будут созданы 3 пользователя:

-   Суперпользователь

```
email: admin@mail.com
password: password
```

-   Обычный пользователь c заполненным профилем

```
email: user@mail.com
password: password
```

-   Eще один обычный пользователь с пустыми данными

```
email: another_user@mail.com
password: password
```

## Развертывание на локальной машине

### Через Docker Compose

1. Склонировать репозиторий

```
git clone https://github.com/sitdoff/Anverali-Group.git
```

3. Перейти в папку проекта, создать файл .env. В файле .env параметр POSTGRES_HOST нужно указать как "db"

```bash
# Структура файла .env представлена в .env_example
cd Anverali-Group/ &&
mv .env_example .env
```

2. Запустить создание образов с использованием Docker Compose

```bash
docker compose up --build
```

3. После окончания сборки, проект будет доступен по адресу http://localhost:8000/

### Без использования Docker Compose

1. Склонировать репозиторий

```
git clone https://github.com/sitdoff/Anverali-Group.git
```

2. Перейти в папку проекта, создать виртуальное окружение и установить в него зависимости

```bash
cd Anverali-Group/ &&
python3 -m venv venv &&
source venv/bin/activate &&
pip install -r requirements.txt
```

3. Создать файл .env и изменить в нём данные, если это требуется.

```bash
# Структура файла .env представлена в .env_example
mv .env_example .env
```

4. База данных должна быть готова принимать подключения с данными, указанными в .env.
   Для демонстрации можно поднять PostgreSQL в докере командой, которая представлена ниже.
   В команде значения переменных POSTGRES_DB, POSTGRES_USER и POSTGRES_PASSWORD должны быть такими же, как в файле .env.

```bash
docker run --hostname=f83069fd7dbc --mac-address=02:42:ac:11:00:02 --env=POSTGRES_DB=postgres --env=POSTGRES_USER=postgres --env=POSTGRES_PASSWORD=postgres --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/16/bin --env=GOSU_VERSION=1.16 --env=LANG=en_US.utf8 --env=PG_MAJOR=16 --env=PG_VERSION=16.1-1.pgdg120+1 --env=PGDATA=/var/lib/postgresql/data --volume=/var/lib/postgresql/data -p 5432:5432 --restart=no --runtime=runc -d postgres:latest

```

5. Создать миграции, применить миграции и загрузить данные для демонстрации из фикстуры

```bash
python3 freelance/manage.py makemigrations &&
python3 freelance/manage.py migrate &&
python3 freelance/manage.py loaddata demo_data.json
```

6. Запустить проект используя встроенный в Django сервер.

```bash
python3 freelance/manage.py runserver --settings=core.settings.development
```

Проект будет доступен по адресу http://localhost:8000/
