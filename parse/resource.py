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


def parse_data(sub_file):
    output = sub_file.splitlines()[1:]

    results = []

    for row in output:
        data = row.split(',')

        # strip data from each row
        test = data[0].split('[')[0].split('.')[-2]
        status = data[1]
        start = data[2]
        stop = data[3]

        results.append({
            'test-name': test,
            'status': status,
            'start': start,
            'stop': stop
        })
    return results


def entry_point():
    cls_args = ArgumentParser().parse_args()
    data = []
    for _file in os.listdir(cls_args.upgrade_dir):
        result = parse_data(open(os.path.join(cls_args.upgrade_dir,
                                              _file)).read())
        if result:
            data.append(result)

    print result

