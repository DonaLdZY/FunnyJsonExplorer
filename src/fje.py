import argparse

from container_factory import  FactoryRegistry,TreeFactory, RectangleFactory
from funny_json_explorer import FunnyJsonExplorer
from icon_factory import IconFactory

def main():
    parser = argparse.ArgumentParser(description="This is a description of the script.")
    parser.add_argument("--filename", "-f", type=str, help="the JSON file to be explored")
    parser.add_argument("--style", "-s", type=str, default="tree", help="explor style (tree/rectangle)")
    parser.add_argument("--icon", "-i", type=str, default="space", help="icon family (chess/star/poker-face/angle/emoji)")
    args = parser.parse_args()

    icon_factory = IconFactory(args.icon)
    
    registry = FactoryRegistry()
    registry.register_factory('tree', TreeFactory())
    registry.register_factory('rectangle', RectangleFactory())
    
    style_factory = registry.get_factory(args.style)
    

    explorer = FunnyJsonExplorer(style_factory, icon_factory)
    explorer.show(args.filename)


if __name__ == "__main__":
    main()
