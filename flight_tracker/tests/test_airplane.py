import pytest
from src.models import Airplane


def test_airplane_validation():
    with pytest.raises(ValueError):
        Airplane("", None, "Germany", 100, 1000)


def test_airplane_comparison():
    a1 = Airplane("abc", "AAA", "Germany", 100, 2000)
    a2 = Airplane("def", "BBB", "Germany", 150, 1000)
    assert a1 < a2
    assert a2 > a1


def test_airplane_from_state():
    state = [
        "abc123", "CALL123 ", "Germany", None, None,
        10.0, 20.0, 3000.0, None, 250.0,
        None, None, None, False, 0
    ]
    airplane = Airplane.from_state(state)
    assert airplane.icao24 == "abc123"
    assert airplane.callsign == "CALL123"
    assert airplane.origin_country == "Germany"
    assert airplane.latitude == 20.0
    assert airplane.longitude == 10.0
    assert airplane.baro_altitude == 3000.0
    assert airplane.velocity == 250.0
