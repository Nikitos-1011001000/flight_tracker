from src.models import Airplane


def run_cli(api_client, storage):
    country = input("Введите страну: ").strip()
    bbox = api_client.get_country_bbox(country)
    states = api_client.get_aeroplanes(bbox)
    airplanes = [Airplane.from_state(s)
                 for s in states if s[7]
                 is not None or s[9] is not None]

    print(f"Найдено самолётов: {len(airplanes)}")

    for ap in airplanes:
        storage.add(ap)

    n = int(input("Введите N для топа по высоте: "))
    top_by_altitude = sorted(
        [a for a in airplanes if a.baro_altitude is not None],
        key=lambda x: x.baro_altitude,
        reverse=True
    )[:n]
    for a in top_by_altitude:
        print(a.to_dict())

    reg_country = input("Введите страну регистрации: ").strip()
    filtered = [a for a
                in airplanes
                if
                a.origin_country.lower()
                == reg_country.lower()]
    for a in filtered:
        print(a.to_dict())
