import csv
import sys
import tabulate

def main():
    filename = validate_input()
    table=[]

    try:
        with open(filename) as file:
            for line in file:
               table.append(line.strip().split(","))
            print(tabulate.tabulate(table, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def validate_input():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]


if __name__ =="__main__":
    main()
