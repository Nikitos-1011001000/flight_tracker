from src.models import Airplane
from storage.json_storage import JSONStorage


def test_json_storage_add_get_remove(tmp_path):
    file_path = tmp_path / "airplanes.json"
    storage = JSONStorage(str(file_path))

    airplane = Airplane("abc123", "CALL1", "Germany", 120, 3000)
    storage.add(airplane)

    result = storage.get_by(origin_country="Germany")
    assert len(result) == 1
    assert result[0]["icao24"] == "abc123"

    removed = storage.remove(origin_country="Germany")
    assert removed == 1
    assert storage.get_by(origin_country="Germany") == []
