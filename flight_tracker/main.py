from src.base import APIAdapter
from storage.json_storage import JSONStorage
from src.cli import run_cli


def main():
    api_client = APIAdapter()
    storage = JSONStorage("airplanes.json")
    run_cli(api_client, storage)


if __name__ == "__main__":
    main()
