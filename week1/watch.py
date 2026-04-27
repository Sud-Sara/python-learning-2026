import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^<iframe.*src=\"https?://(?:www\.)?(?:youtube\.com/embed/)(?P<vcode>\w*)\".*></iframe>$"
    restr="https://youtu.be/"
    if matches := re.match(pattern, s):
        restr+=matches.group("vcode")
        return restr

    return


if __name__ == "__main__":
    main()
