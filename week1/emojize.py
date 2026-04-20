import emoji


def main():
    str = input("Input: ")
    print(emoji.emojize(str, language="alias"))


if __name__ == "__main__":
    main()
