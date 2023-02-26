# JWT-FastAPI

Запуск приложения:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r ./requirements.txt
# развернуть бд и накатить миграции
uvicorn app:app --reload
python3 ./initial_users_by_db.py
```
Заполнить файл Settings.py:

DB_HOST = "" 
DB_NAME = "" # name your DB
DB_USER_NAME = "" # name user your DB
DB_USER_PASSWORD = "" # pas your DB


Secret = '' # openssl rand -hex 32

Миграции:

```bash
alembic revision --autogenerate -m <text>
alembic upgrade head
```
