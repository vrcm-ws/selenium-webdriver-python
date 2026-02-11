import json

from pathlib import Path
from typing import Any


def load_json_data(file_name: str) -> list[Any]:

    base_path: Path = Path(__file__).parent.parent
    data_path: Path = base_path / "test_data" / file_name

    with open(data_path, "r") as f:
        return json.load(f)
