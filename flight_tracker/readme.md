\# Flight Tracker



Содержание:

\## Flight Tracker

\## Установка

\## Ожидаемый вывод







\## Flight Tracker

Приложение для отслеживания полётов в реальном времени. Показывает местоположение самолётов над выбранной страной и их основные параметры.







\## Установка (Installation) — пошаговая инструкция по развёртыванию:



* клонирование репозитория;



* создание виртуального окружения (рекомендуется);



* установка зависимостей из requirements.txt.



Пример:

bash

git clone https://github.com/Nikitos-1011001000/flight\_tracker.git

cd flight\_tracker

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\\Scripts\\activate  # Windows

pip install -r requirements.txt

poetry run python main.py


\## Ожидаемый вывод:

Введите страну: Russia
Найдено самолётов: 2415
Введите N для топа по высоте: 1
{'icao24': '8005b9', 'callsign': 'VTBRS   ', 'origin_country': 'India', 'velocity': 244, 'baro_altitude': 14325.6, 'latitude': 43.2763, 'longitude': 19.7617}
Введите страну регистрации: Russia

...



