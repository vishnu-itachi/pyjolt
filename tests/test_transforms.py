import pytest

from pyjolt.jolt import Jolt
from tests.utils.load_data import load_data

transform_list = [
    "default",
    "remove",
    "shift",
    "sort",
    "cardinality/many",
    "cardinality/one",
]


@pytest.mark.parametrize("transform", transform_list)
def test_transforms(transform):
    input_data, spec_data, expected_output_data = load_data(transform)

    jolt = Jolt(input_data)
    jolt.transform(spec_data)
    assert jolt.data == expected_output_data
