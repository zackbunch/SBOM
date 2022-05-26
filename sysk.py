from src.parsers.cli import Parser
from src.parsers.pip import PIP

def main():
    args = Parser.get_args()
    pip = PIP()
    if args.sbom:
        pip.generate_sbom()

    

    
   
    
    


if __name__ == '__main__':
    main()