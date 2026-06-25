import pytest
from unittest.mock import patch, Mock
from src.geosky import GeoSkyAPIClient
from src.base import APIAdapter


def get_aeroplanes_by_bbox(self, bbox: list[float]) -> list[dict]:
    if bbox is None or len(bbox) == 0:
        return []
    return [
        {'icao24': 'test1', 'callsign': 'TEST1',
         'origin_country': 'TestCountry'},
        {'icao24': 'test2', 'callsign': 'TEST2',
         'origin_country': 'TestCountry'}
    ]


class TestSimpleAPIAdapter:
    """Простые тесты с реализацией абстрактных методов."""

    def test_get_country_bbox_empty_string(self):
        """Тест get_country_bbox с пустой строкой."""
        client = APIAdapter()
        result = client.get_country_bbox("")
        assert result is None

    def test_get_country_bbox_none(self):
        """Тест get_country_bbox с None."""
        client = APIAdapter()
        result = client.get_country_bbox(None)
        assert result is None

    def test_get_aeroplanes_empty_country(self):
        """Тест get_aeroplanes с пустой строкой вместо страны."""
        client = APIAdapter()
        result = client.get_aeroplanes("")
        assert isinstance(result, list)
        assert len(result) == 0

    def test_get_aeroplanes_none_country(self):
        """Тест get_aeroplanes с None вместо страны."""
        client = APIAdapter()
        result = client.get_aeroplanes(None)
        assert isinstance(result, list)
        assert len(result) == 0


class TestGeoSkyClientWithMocks:
    """Тесты с использованием моков для сетевых запросов."""

    @patch('src.geosky.requests.get')
    def test_get_country_bbox_not_found(self, mock_get):
        """Тест для несуществующей страны."""
        mock_response = Mock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        client = APIAdapter()
        result = client.get_country_bbox("NonexistentCountry")

        assert result is None

    @patch('src.geosky.requests.get')
    def test_get_country_bbox_network_error(self, mock_get):
        """Тест обработки сетевой ошибки."""
        mock_get.side_effect = Exception("Network error")

        client = APIAdapter()

        with pytest.raises(Exception, match="Network error"):
            client.get_country_bbox("Germany")
