import json
from pathlib import Path
from src.models import Airplane
from storage.base import BaseStorage


class JSONStorage(BaseStorage):
    def __init__(self, filename: str):
        self.path = Path(filename)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def _load(self):
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, data):
        self.path.write_text(
            json.dumps(data,
                       ensure_ascii=False, indent=2),
            encoding="utf-8")

    def add(self, airplane: Airplane) -> None:
        data = self._load()
        data.append(airplane.to_dict())
        self._save(data)

    def get_by(self, **criteria):
        data = self._load()
        result = []
        for item in data:
            ok = True
            for key, value in criteria.items():
                if item.get(key) != value:
                    ok = False
                    break
            if ok:
                result.append(item)
        return result

    def remove(self, **criteria) -> int:
        data = self._load()
        new_data = []
        removed = 0
        for item in data:
            ok = all(item.get(k) == v for k, v in criteria.items())
            if ok:
                removed += 1
            else:
                new_data.append(item)
        self._save(new_data)
        return removed
