import argparse


class Parser:
    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(
            description="A tool for retrieving basic information about packages on your system"
        )
        parser.add_argument(
            "-report", dest="report", help="Specifies the report type to be generated"
        )
        parser.add_argument(
            'sbom', help='Generate SBOM'
        )

        return parser.parse_args()
