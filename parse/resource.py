import argparse
import os

from datetime import datetime


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        desc = "Parses data from persistent resources during an upgrade"
        usage_string = "resource-parse [-u/--upgrade-rie] "

        super(ArgumentParser, self).__init__(
            usage=usage_string, description=desc)

        self.add_argument(
            "-u", "--upgrade-dir", metavar="", required=True,
            default=None, help="The path to the upgrade test directory.")


def parse_data(sub_file):
    output = open(sub_file).read().splitlines()[1:]

    results = {}

    # if multiple lines in file
    for line in output:
        test_name, status, start, stop = line.split(",")
        _, action, product = test_name.split("[")[0].split(".")[-3].split("_", 2)

        # add key to dict
        if product not in results:
            results[product] = {}

        if action is not 'verify':
            results[product][action] = status
            results[product]['start'] = start
            results[product]['stop'] = stop
            results[product]['service'] = product
        else:
            results[product][action] = {
                action: status,
                'start': start,
                'stop': stop,
                'service': product
            }

    return results


def parse(path_dir):
    data = {}

    for _file in os.listdir(path_dir):
        if _file.endswith(".csv"):
            call = parse_data(os.path.join(path_dir, _file))

            # iterate over keys in returned
            for key, value in call.items():
                if key not in data:
                    data[key] = {}

                # add values to key
                data[key].update(value)

    return data


def entry_point():
    cls_args = ArgumentParser().parse_args()
    print parse(cls_args.upgrade_dir)
