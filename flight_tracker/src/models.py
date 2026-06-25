from dataclasses import dataclass, field


@dataclass(order=False)
class Airplane:
    icao24: str
    callsign: str | None
    origin_country: str
    velocity: float | None
    baro_altitude: float | None
    latitude: float | None = field(default=None)
    longitude: float | None = field(default=None)

    def __post_init__(self):
        if not isinstance(self.icao24, str) or not self.icao24:
            raise ValueError("invalid icao24")
        if self.callsign is not None and not isinstance(self.callsign, str):
            raise ValueError("invalid callsign")
        if self.velocity is not None and self.velocity < 0:
            raise ValueError("invalid velocity")
        if self.baro_altitude is None or isinstance:
            return
        raise ValueError("invalid altitude")

    def _speed_value(self):
        return self.velocity if self.velocity is not None else -1

    def _alt_value(self):
        return self.baro_altitude if self.baro_altitude is not None else -1

    def __lt__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return (self._speed_value(),
                self._alt_value()) < (other._speed_value(),
                                      other._alt_value())

    def __eq__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return ((self._speed_value(),
                self._alt_value()) ==
                (other._speed_value(), other._alt_value()))

    def to_dict(self):
        return {
            "icao24": self.icao24,
            "callsign": self.callsign,
            "origin_country": self.origin_country,
            "velocity": self.velocity,
            "baro_altitude": self.baro_altitude,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    @classmethod
    def from_state(cls, state: list):
        callsign = state[1].strip() if isinstance(state[1], str) else None
        return cls(
            icao24=state[0],
            callsign=callsign,
            origin_country=state[2],
            longitude=state[5],
            latitude=state[6],
            baro_altitude=state[7],
            velocity=state[9],
        )
