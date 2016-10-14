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
        test_name, status, _, _ = line.split(",")
        _, action, product = test_name.split("[")[0].split(".")[-3].split("_", 2)

        # add key to dict
        if product not in results:
            results[product] = {}

        results[product][action] = status

    return results


def parse(path_dir):
    data = {}

    for _file in os.listdir(path_dir):
        call = parse_data(os.path.join(path_dir, _file))

        # iterate over keys in returned
        for key, value in call.items():
            if key not in data:
                data[key] = {}

            # add values to key
            data[key].update(value)

    final_data = {}
    d_format = "{:%B %d, %Y, %I:%M:%S %p}"

    for product, actions in data.items():
        status = "success"

        for act in ['create', 'validate', 'cleanup']:

            # gets the status of the action
            if actions.get(act) != "success":
                status = "{0}_{1}".format(act, actions.get(act))
                break

        final_data[product] = {'status': status,
                               'time': d_format.format(datetime.now())}
    return final_data


def entry_point():
    cls_args = ArgumentParser().parse_args()
    print parse(cls_args.upgrade_dir)
