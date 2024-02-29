from system.application import Application
from system.utils.config_parser import ConfigParser
import bottle


class Web:
    config: ConfigParser
    port = 3000
    app: bottle.Bottle
    application: Application

    def __init__(self, application: Application):
        self.app = bottle.Bottle()
        self.config = application.config_parser
        self.application = application

        self.app.route("/", callback=self.main)
        self.app.route("/resource/<resource_id>/<row_id>", callback=self.row)
        self.app.route("/resource/<resource_id>", callback=self.resource)
        print(f"Application started at port {self.port}!")

        self.app.run(port=self.port)

    def __current_resource_data__(self, resource_id: int) -> dict:
        resource = next((item for item in self.config.data.resources if item.id == resource_id), None)

        db_query = self.application.db.query(f"SELECT * FROM {resource_id}")
        description = db_query.description
        db_data = db_query.fetchall()

        data_processed = {
            "columns": [field[0] for field in description],
            "data": db_data
        }

        data = {
            "id": resource.id,
            "title": resource.title,
            "data": data_processed
        }

        return data

    def __current_row_data__(self, resource_id: int, row_id: int) -> dict:
        result = self.application.db.query(f"SELECT * FROM {resource_id} WHERE id = {row_id}").fetchone()
        return result

    def __generate_template_config__(self, resource_id=None, row_id=None):
        current_resource = None
        if resource_id:
            current_resource = self.__current_resource_data__(resource_id)

        current_row = None
        if row_id:
            current_row = self.__current_row_data__(resource_id, row_id)

        data = {
            "app_title": self.config.data.title,
            "current_resource": current_resource,
            "current_row": current_row,
            "page_title": current_resource["title"] if current_resource else None,
            "resources": [
                {
                    "id": resource.id,
                    "title": resource.title
                } for resource in self.config.data.resources
            ],
            "raw_config": self.config.raw_data
        }
        return data

    def main(self):
        tpl = bottle.template("main.tpl", self.__generate_template_config__())
        return tpl

    def resource(self, resource_id):
        tpl = bottle.template("main.tpl", self.__generate_template_config__(resource_id=resource_id))
        return tpl

    def row(self, resource_id, row_id):
        tpl = bottle.template("main.tpl", self.__generate_template_config__(resource_id=resource_id, row_id=row_id))
        return tpl