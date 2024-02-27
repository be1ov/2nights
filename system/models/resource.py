import typing as tp
from system.models.field import FieldModel


class ResourceModel:
    id: str
    title: str
    fields: tp.List[FieldModel]

    def __init__(self, resource):
        self.fields = []
        self.id = resource["id"]
        self.title = resource["title"]

        _fields = resource["fields"]
        for field in _fields:
            self.fields.append(FieldModel(field))
        print(self.id, self.fields)
        print(self.id, _fields)