class FieldModel:
    id: str
    title: str
    type: str
    length: int
    required: bool

    def __init__(self, field):
        self.id = field["id"]
        self.title = field["title"]
        self.type = field["type"]
        self.length = 20 if "length" not in field else field["length"]
        self.required = False if "required" not in field else field["required"]