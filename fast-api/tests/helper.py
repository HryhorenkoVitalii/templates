import json
from typing import Any, Dict, cast


def load_fixture(filename: str) -> Dict[str, Any]:
    with open(f"tests/fixtures/{filename}") as file:
        return cast(Dict[str, Any], json.load(file))
