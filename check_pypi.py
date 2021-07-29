import json
import requests
from packaging import version
import argparse

parser = argparse.ArgumentParser("Get the available PyPI versions for a package!")
parser.add_argument("package", help="The name of the PyPI package.")


def versions(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    data = json.loads(requests.get(url).text)
    versions = sorted([v for v in data["releases"].keys()], key=lambda x: version.parse(x))
    return versions

if __name__ == "__main__":
    args = parser.parse_args()
    print("\n".join(versions(args.package)))
