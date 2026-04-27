import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    c=0
    pattern= r"\b(um)\b"
    if matches := re.findall(pattern, s.lower()):
        c=len(matches)
    return c


if __name__ == "__main__":
    main()
