import pyjson5 as json
import os
from pathlib import Path
from pprint import pprint

from pyjolt.jolt import Jolt

if __name__ == "__main__":
    resources = os.path.join(Path(__file__).parents[1], "tests/resources")
    shift = os.path.join(resources, "cardinality/many")
    input_path = os.path.join(shift, "input.json")
    expected_output = os.path.join(shift, "expected_output.json")
    spec = os.path.join(shift, "spec.json")

    with open(input_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    with open(expected_output, "r", encoding="utf-8") as f:
        expected_output_data = json.load(f)

    with open(spec, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    jolt = Jolt(input_data)
    jolt.transform(spec_data)
    pprint(expected_output_data, sort_dicts=False)
    assert jolt.data == expected_output_data
