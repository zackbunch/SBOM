from asyncio.subprocess import PIPE
import json
import subprocess as sp
from email.parser import BytesHeaderParser


def get_pip_package_json():
    results = sp.run(
        ["pip3", "list", "-l", "--format=json"], stdout=PIPE, stderr=sp.PIPE, text=True
    )
    return results.stdout


def get_detailed_pip():
    json_str = get_pip_package_json()
    json_data = json.loads(json_str)
    with open("src/data/pip_detailed.json", "w+") as f:
        content = []
        for item in json_data:
            p = sp.run(["pip3", "show", f"{item['name']}"], stdout=PIPE, stderr=sp.PIPE)
            h = BytesHeaderParser().parsebytes(p.stdout)
            h_json = dict(h)
            content.append(h_json)
        json.dump(content, f)
