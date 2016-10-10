import argparse
import os


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        desc = "Parses data from persistent resources during an upgrade"
        usage_string = "resource-parse [-u/--upgrade-rie] "

        super(ArgumentParser, self).__init__(
            usage=usage_string, description=desc)

        self.add_argument(
            "-u", "--upgrade-dir", metavar="", required=True,
            default=None, help="The path to the upgrade test directory.")


def entry_point():
    cls_args = ArgumentParser().parse_args()
    for _file in os.listdir(cls_args.upgrade_dir):
        acrap = open(os.path.join(cls_args.upgrade_dir, _file))
        print acrap.read()
