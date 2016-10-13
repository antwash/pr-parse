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

    data = output.pop().split(',')

    # strip data from each row
    action = data[0].split('[')[0].split('.')[-3].split('_')[1]
    status = data[1]

    results = {
        'action': action,
        'status': status
    }

    return results


def entry_point():
    cls_args = ArgumentParser().parse_args()
    data = {'persistent': []}

    for _file in os.listdir(cls_args.upgrade_dir):
        call = parse_data(open(os.path.join(cls_args.upgrade_dir,
                                            _file)).read())
        data['persistent'].append(call)

    print data
    #print all(d.pop()['status'] == "success" for d in data)


