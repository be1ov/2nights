from system.utils.config_parser import ConfigParser
import bottle


class Web:
    config: ConfigParser
    port = 3000
    app: bottle.Bottle

    def __generate_template_config__(self, resource_id=None):
        current_resource = next((item for item in self.config.data.resources if item.id == resource_id), None)
        data = {
            "app_title": self.config.data.title,
            "page_title": current_resource.title,
            "resource_title": current_resource.title,
            "resources": [
                {
                    "id": resource.id,
                    "title": resource.title
                } for resource in self.config.data.resources
            ],
            "resource_id": resource_id
        }
        return data

    def __init__(self, config):
        self.app = bottle.Bottle()
        self.config = config

        self.app.route("/", callback=self.main)
        self.app.route("/resource/<resource_id>", callback=self.resource)
        print(f"Application started at port {self.port}!")

        self.app.run(port=self.port)

    def main(self):
        tpl = bottle.template("main.tpl", self.__generate_template_config__())
        return tpl

    def resource(self, resource_id):
        tpl = bottle.template("main.tpl", self.__generate_template_config__(resource_id=resource_id))
        return tpl