from dataclasses import dataclass
import requests

from src.base import BaseAPIClient


@dataclass
class GeoSkyAPIClient(BaseAPIClient):
    nominatim_url: str = "https://nominatim.openstreetmap.org/search"
    opensky_url: str = "https://opensky-network.org/api/states/all"
    user_agent: str = "airplane-app/1.0"

    def _request(self, url: str, params: dict) -> dict | list:
        response = requests.get(
            url,
            params=params,
            headers={"User-Agent": self.user_agent},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    def get_country_bbox(self, country: str) -> list[float]:
        params = {
            "q": country,
            "format": "jsonv2",
            "limit": 1,
        }
        data = self._request(self.nominatim_url, params)
        if not data:
            raise ValueError("Страна не найдена")

        boundingbox = data[0]["boundingbox"]
        south, north, west, east = map(float, boundingbox)
        return [south, west, north, east]

    def get_airplanes(self, bbox: list[float]) -> list[list]:
        south, west, north, east = bbox
        params = {
            "lamin": south,
            "lomin": west,
            "lamax": north,
            "lomax": east,
        }
        data = self._request(self.opensky_url, params)
        return data.get("states") or []
