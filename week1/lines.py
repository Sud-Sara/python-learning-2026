import sys

def main():
    name = validate_input()
    print(countlines(name))

def countlines(filename):
    try:
        loc=0
        with open(filename) as file:
            for line in file:
                if line.lstrip().startswith("#") or line.strip()=="":
                    pass
                else:
                    loc+=1
            return loc
    except FileNotFoundError:
        sys.exit("File does not exist")

def validate_input():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]

if __name__ == "__main__":
    main()
