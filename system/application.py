from system.utils.config_parser import ConfigParser
from system.models.database import Database


class Application:
    config_parser: ConfigParser
    title: str
    author: str
    version: str
    db: Database

    def __init__(self, config_file: str):
        self.config_parser = ConfigParser(config_file)

        self.title = self.config_parser.data.title
        self.author = self.config_parser.data.author
        self.version = self.config_parser.data.version
        self.db = Database()

        for resource in self.config_parser.data.resources:
            stmt = f"CREATE TABLE IF NOT EXISTS {resource.id} (id integer primary key"
            for field in resource.fields:
                if field.type.startswith("refto:"):
                    # it's a reference to another object
                    ftable_name = field.type.split(":")[1]
                    stmt += f", \"{field.id}\" integer {'NOT NULL' if field.required else ''}, FOREIGN KEY(\"{field.id}\") REFERENCES {ftable_name}(id)"
                else:
                    stmt += f", \"{field.id}\" {field.type} varying({field.length}) {'NOT NULL' if field.required else ''}"
            stmt += ")"
            self.db.query(stmt)
