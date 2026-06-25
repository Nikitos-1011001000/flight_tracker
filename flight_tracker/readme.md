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



\## Ожидаемый вывод:

Найдено самолётов: 15

ICAO24: 3c642a, Callsign: DAL123, Latitude: 52.5, Longitude: 13.4

...



