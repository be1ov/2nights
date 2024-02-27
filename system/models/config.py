import typing as tp
from system.models.resource import ResourceModel


class ConfigModel:
    id: str
    title: str
    author: str
    version: str
    resources: tp.List[ResourceModel] = []

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.version = data["version"]

        _resources = data["resources"]
        for resource in _resources:
            _resource = ResourceModel(resource)
            self.resources.append(_resource)
