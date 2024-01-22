RU
Уставновка:
1. Скачать zip-архив из этого репозитория и распаковать
2. Установить python 3.10 - python 3.11(https://www.python.org/downloads/) | Linux: sudo apt install python3.10
3. Перейти в в корневую директорию проекта и создать виртуальное окружение - python -m venv venv(Для линукса предварительно установить виртуальное окружение: sudo apt install python3.10-venv)
4. Активировать виртуальное окружение -  venv/scripts/activate | Linux: source venv/bin/activate
5. Установить зависимости - pip install -r requirements.txt | Linux: pip3 install -r requirements.txt
6. Сгенерировать секретный ключ - создать файл key.py и вставить следующее содержимое -
7. 
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
8. Запустить файл и скопировать из командной строки сгенерированый ключ - python key.py
9. Создать файл .env в корне проекта и прописать одну строчку SECRET_KEY = тут_ваш_секретный_ключ
10. Совершать миграции для базы данных - python manage.py makemigrations, python manage.py migrate
11. Запустить сервер - python manage.py runserver

Installation:
1. Download the zip archive from this repository and unzip it
2. Install python 3.10 - python 3.11(https://www.python.org/downloads/) | Linux: sudo apt install python3.10
3. Go to the root directory of the project and create a virtual environment - python -m venv venv(For Linux, pre-install the virtual environment: sudo apt install python3.10-venv).
4. activate the virtual environment - venv/scripts/activate | Linux: source venv/bin/activate
5. Install dependencies - pip install -r requirements.txt | Linux: pip3 install -r requirements.txt
6. Generate a secret key - create a key.py file and paste the following contents -
7. 
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
8. Run the file and copy the generated key from the command line - python key.py
9. Create an .env file in the root of the project and write one line SECRET_KEY = here_your_secret_key
10. Make migrations for the database - python manage.py makemigrations, python manage.py migrate
11. Start the server - python manage.py runserver
