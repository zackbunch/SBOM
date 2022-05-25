import json
import subprocess as sp
from email.parser import BytesHeaderParser

from tqdm import tqdm


class PIP:
    def get_pip_package_json(self):
        cmd_results = sp.run(
            ["pip3", "list", "--local", "--format=json"],
            stdout=sp.PIPE,
            stderr=sp.PIPE,
            text=True,
            check=True,
        )
        return json.loads(cmd_results.stdout)

    def get_detailed_pip(self):
        json_str = self.get_pip_package_json()
        content = []
        for item in tqdm(json_str, desc="Writing PIP packages to JSON"):
            pip_cmd = sp.run(
                ["pip3", "show", f"{item['name']}"], stdout=sp.PIPE, stderr=sp.PIPE
            )
            header_output = BytesHeaderParser().parsebytes(pip_cmd.stdout)
            header_json = dict(header_output)
            keys_values = header_json.items()
            str_dict = {str(key): str(value) for key, value in keys_values}
            content.append(str_dict)
        return content

    def write_json(self, file_name="src/data/pip_detailed.json"):
        with open(file_name, "w+") as json_file:
            data = self.get_detailed_pip()
            json.dump(data, json_file)











