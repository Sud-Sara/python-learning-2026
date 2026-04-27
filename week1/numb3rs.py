import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    Valid = False

    if matches := re.match(pattern, ip):
        for i in matches.groups():
            if (0 <= int(i) <= 255) and not (len(i) > 1 and i.startswith("0")):
                Valid = True
            else:
                return False
    return Valid


if __name__ == "__main__":
    main()
