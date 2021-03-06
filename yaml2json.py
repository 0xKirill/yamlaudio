import sys
import yaml
import json
import datetime


def dthandler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime("%Y-%m-%d")
    else:
        return None


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        yamldict = yaml.load(file.read().decode('utf-8'))
        print(json.dumps(yamldict, default=dthandler).encode('utf-8'))


if __name__ == '__main__':
    main()
