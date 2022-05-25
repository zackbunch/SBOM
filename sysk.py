from src.parsers.cli import Parser
from src.parsers.pip import PIP

def main():
    args = Parser.get_args()
    pip = PIP()
    pip.write_json()

    
   
    
    


if __name__ == '__main__':
    main()