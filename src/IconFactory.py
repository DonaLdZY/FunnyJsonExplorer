from utils import load_json


class IconFactory:
    def __init__(self, icon_family, config_file='config/icon_config.json'):
        self.icon_family = icon_family
        self.config = load_json(config_file)

    def set_config(self, config_file):
        self.config = load_json(config_file)

    def set_icon_family(self, icon_family):
        self.icon_family = icon_family

    def get_icon(self, is_leaf=False):
        if self.icon_family not in self.config:
            raise ValueError(f"Unknown icon family: {self.icon_family}")
        icon_type = 'leaf' if is_leaf else 'middle'
        return self.config[self.icon_family].get(icon_type, '?')
