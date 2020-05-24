import json


class Config(object):
    class _Config(object):
        def __init__ (self):
            with open("config.json") as jsonConfigFile:
                self.config = json.load(jsonConfigFile)
    instance = None
    def __init__(self):
        if not Config.instance:
            Config.instance = Config._Config()
    def __getitem__(self, key):
        return self.instance.config[key]
    def __setitem__(self, key, value):
        self.instance.config[key] = value
