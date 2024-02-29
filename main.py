from system.models.web import Web
from system.application import Application

if __name__ == "__main__":
    config_file = "configuration.json"

    application = Application(config_file)
    web = Web(application)
