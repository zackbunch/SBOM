import json
import subprocess as sp
from email.parser import BytesHeaderParser

import pandas as pd
from tqdm import tqdm


class PIP:
    @staticmethod
    def get_pip_package_json():
        """Get Package Name and Version from the system by
        executing the command:
             pip3 list --local --format=json

        Returns:
            json: Object containing Name and Version
        """
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

    def json_to_df(self, json_str):
        pip_df = pd.DataFrame.from_dict(json_str)
        return pip_df

    def generate_sbom(self, file_name="src/data/pip_detailed.json"):
        with open(file_name, "w+", encoding="UTF-8") as json_file:
            data = self.get_detailed_pip()
            json.dump(data, json_file, indent=3)

    @staticmethod
    def is_approved_version():
        """Validates if installed software version is
        on approved product list"""
        pass
