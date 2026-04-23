import csv
import sys

def main():
    rfilename, wfilename = validate_input()
    table=read_file(rfilename)
    #print(table)
    write_file(wfilename, table)


def write_file(filename, table):
    try:
        with open(filename, "w") as file:
            writer=csv.writer(file)
            for line in table:
                writer.writerow(line)
    except :
        sys.exit(f"Could not write {filename}")


def read_file(filename):
    table=[]
    try:
        with open(filename) as file:
            reader=csv.reader(file)
            for line in reader:
                if line == ['name', 'house']:
                    table.append(['first','last','house'])
                else:
                    last, first =line[0].split(",")
                    table.append([first.strip(), last, line[1]])
            return table
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")


def validate_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1], sys.argv[2]


if __name__ =="__main__":
    main()
