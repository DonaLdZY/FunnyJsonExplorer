# main.py
import argparse

from container_factory import TreeFactory, RectangleFactory
from funny_json_explorer import FunnyJsonExplorer
from icon_factory import IconFactory

icon_factory = (IconFactory("emoji"), IconFactory("angle"))
style_factory = (TreeFactory(), RectangleFactory())


def main():
    parser = argparse.ArgumentParser(description="This is a description of the script.")
    # 添加参数
    parser.add_argument("--filename", "-f", type=str, help="the JSON file to be explored")
    parser.add_argument("--style", "-s", type=str, default="tree", help="explor style (tree/rectangle)")
    parser.add_argument("--icon", "-i", type=str, default="space",
                        help="icon family (chess/star/poker-face/angle/emoji)")

    # 解析参数
    args = parser.parse_args()

    icon_factory = IconFactory(args.icon)

    style_factory = TreeFactory()
    if args.style == "tree":
        style_factory = TreeFactory()
    elif args.style == "rectangle":
        style_factory = RectangleFactory()
    else:
        raise KeyError("Undefined Style")

    explorer = FunnyJsonExplorer(style_factory, icon_factory)
    explorer.show(args.filename)


if __name__ == "__main__":
    main()
