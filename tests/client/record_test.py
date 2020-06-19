import pytest

from rets.client.resource import Resource
from rets.client.resource_class import ResourceClass
from rets.client.record import Record


@pytest.fixture()
def key_field_resource_class():
    resource = Resource(metadata={"KeyField": "lowercase"}, http_client=None)
    resource_class = ResourceClass(resource=resource, metadata={}, http_client=None)

    return resource_class


@pytest.fixture()
def data():
    return {"Lowercase": "What is this? A center for ants?"}


def test_record_constructor(key_field_resource_class, data):
    record = Record(resource_class=key_field_resource_class, data=data)

    assert record.resource_key == "What is this? A center for ants?"
