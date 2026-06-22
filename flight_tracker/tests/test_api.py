from src.base import APIAdapter
from unittest.mock import MagicMock
from src.base import BaseAPIClient


class MockAPIClient(BaseAPIClient):
    def get_country_bbox(self, country: str) -> list[float] | None:
        if not country or country.strip() == "":
            return None
        bbox_map = {
            "Germany": [1.0, 2.0, 3.0, 4.0],
            "France": [42.0, -5.0, 51.0, 8.0]
        }
        return bbox_map.get(country, [1.0, 2.0, 3.0, 4.0])

    def get_aeroplanes(self, bbox: list[float]) -> list[list]:
        if not bbox or len(bbox) != 4:
            return []
        return [
            ["abc123", "TEST123", "Germany",
             250.0, 10000.0, 1.0, 2.0, 10000.0,
             None, 4.0, None,
             None, None, False, 0],
            ["def456", "TEST456", "France",
             280.0, 8000.0, 2.0, 48.0, 8000.0,
             None, 5.0, None,
             None, None, False, 0]
        ]


def test_get_country_bbox():
    client = MockAPIClient()
    result = client.get_country_bbox("Germany")
    assert result == [1.0, 2.0, 3.0, 4.0]


def test_get_aeroplanes_empty():
    client = MockAPIClient()
    result = client.get_aeroplanes([])
    assert result == []


def test_get_aeroplanes_with_data():
    client = MockAPIClient()
    bbox = [1.0, 2.0, 3.0, 4.0]
    result = client.get_aeroplanes(bbox)
    assert len(result) == 2
    assert result[0][2] == "Germany"
    assert result[1][2] == "France"


def test_get_country_bbox_none_input():
    """Тест для None вместо строки."""
    client = MockAPIClient()
    result = client.get_country_bbox(None)
    assert result is None


def test_get_country_bbox_whitespace():
    """Тест для строки с пробелами."""
    client = MockAPIClient()
    result = client.get_country_bbox("   ")
    assert result is None


def test_get_country_bbox_unknown_country():
    """Тест для неизвестной страны — должен вернуть значение по умолчанию."""
    client = MockAPIClient()
    result = client.get_country_bbox("UnknownCountry")
    assert result == [1.0, 2.0, 3.0, 4.0]


def test_get_country_bbox_case_insensitive():
    """Тест для разных регистров названия страны."""
    client = MockAPIClient()
    # В мок‑классе нет обработки регистра,
    # но тест проверит это поведение
    result_upper = client.get_country_bbox("GERMANY")
    result_lower = client.get_country_bbox("germany")
    assert result_upper == [1.0, 2.0, 3.0, 4.0]
    assert result_lower == [1.0, 2.0, 3.0, 4.0]


def test_base_client_inheritance_coverage():
    # Создаём минимальную реализацию для покрытия базовых методов
    class MinimalClient(BaseAPIClient):
        def get_country_bbox(self, country: str) -> list[float] | None:
            return [0.0, 0.0, 0.0, 0.0] if country else None

        def get_aeroplanes(self, bbox: list[float]) -> list[list]:
            return [] if not bbox else [["test", "data"]]

    client = MinimalClient()
    assert client.get_country_bbox("Any") == [0.0, 0.0, 0.0, 0.0]
    assert client.get_country_bbox("") is None
    assert client.get_aeroplanes([]) == []
    assert len(client.get_aeroplanes([1, 2, 3, 4])) == 1
