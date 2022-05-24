from src.parsers.cli import Parser
from src.parsers.pip import get_pip_packages, get_pip_package_json, get_detailed_pip

def main():
    args = Parser.get_args()
    get_detailed_pip()
   
    
    


if __name__ == '__main__':
    main()