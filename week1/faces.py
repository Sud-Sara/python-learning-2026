def main ():
    str= input("-->")
    print(convert(str))


def convert(str):
    str= str.replace(":)", "😐").replace(":(", "🙂")
    return str


main()