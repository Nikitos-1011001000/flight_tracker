from src.cli import run_cli


class FakeAPI:
    def get_country_bbox(self, country):
        return [1.0, 2.0, 3.0, 4.0]

    def get_aeroplanes(self, bbox):
        return [
            ["abc123", "CALL1 ", "Germany",
             None, None, 10.0, 20.0, 3000.0, None,
             250.0, None, None, None, False, 0],
            ["def456", "CALL2 ", "Germany", None,
             None, 11.0, 21.0, 4000.0, None, 150.0,
             None, None, None, False, 0],
        ]


class FakeStorage:
    def __init__(self):
        self.items = []

    def add(self, airplane):
        self.items.append(airplane)


def test_run_cli(monkeypatch, capsys):
    inputs = iter(["Germany", "1", "Germany"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    storage = FakeStorage()
    run_cli(FakeAPI(), storage)

    out = capsys.readouterr().out
    assert "Найдено самолётов: 2" in out
    assert len(storage.items) == 2
