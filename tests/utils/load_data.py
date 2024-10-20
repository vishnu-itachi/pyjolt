import os
from pathlib import Path

import pyjson5 as json


def load_data(operation_path) -> tuple[dict, dict, dict]:
    resources = os.path.join(Path(__file__).parents[2], "tests/resources")
    operation = os.path.join(resources, operation_path)
    input_path = os.path.join(operation, "input.json")
    spec_path = os.path.join(operation, "spec.json")
    expected_output_path = os.path.join(operation, "expected_output.json")

    with open(input_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    with open(spec_path, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    with open(expected_output_path, "r", encoding="utf-8") as f:
        expected_output_data = json.load(f)

    return input_data, spec_data, expected_output_data
