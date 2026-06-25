import time
from abc import ABC, abstractmethod
import requests


class BaseAPIClient(ABC):
    @abstractmethod
    def get_country_bbox(self, country: str) -> list[float]:
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> list[dict]:
        pass


class APIAdapter(BaseAPIClient):
    def __init__(self) -> None:
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None
        self.timeout = 30
        self.headers = {
            'User-Agent': 'FlightTrackerApp/1.0'  # обязательно для Nominatim
        }

    def get_country_bbox(self, country: str) -> list[float] | None:
        """Получает bounding box для указанной страны через OpenStreetMap."""
        time.sleep(1)
        params = {
            'q': country,
            'format': 'json',
            'limit': 1
        }
        try:
            response = requests.get(
                self.openstreetmap_url,
                params=params,
                headers=self.headers,  # добавляем заголовки
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            if data:
                # Преобразуем строки в числа с плавающей точкой
                bbox = [float(data[0]['boundingbox'][i]) for i in range(4)]
                return bbox
            return None
        except (requests.RequestException, KeyError, IndexError) as e:
            print(f"Ошибка при получении bounding box: {e}")
            return None

    def get_aeroplanes(self, country: str) -> list[dict]:
        """Получает данные о самолётах над указанной страной."""
        # Сначала получаем bounding box страны
        bbox = self.get_country_bbox(country)
        if not bbox:
            return []

        params = {
            'lamin': bbox[0],  # минимальная широта
            'lamax': bbox[1],  # максимальная широта
            'lomin': bbox[2],  # минимальная долгота
            'lomax': bbox[3]  # максимальная долгота
        }

        try:
            response = requests.get(
                self.opensky_url,
                params=params,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()

            # Преобразуем сырые данные в список словарей
            airplanes_data = []
            if 'states' in data and data['states']:
                for state in data['states']:
                    airplane = {
                        'icao24': state[0],
                        'callsign': state[1],
                        'origin_country': state[2],
                        'longitude': state[5],
                        'latitude': state[6],
                        'baro_altitude': state[7],
                        'velocity': state[9]
                    }
            airplanes_data.append(airplane)

            return airplanes_data
        except (requests.RequestException, IndexError, KeyError) as e:
            print(f"Ошибка при получении данных о самолётах: {e}")
            return []
