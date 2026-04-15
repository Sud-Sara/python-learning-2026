def main():
    answer = input("camelCase: ").strip()
    print("snake_case: ", end="")
    convert(answer)



def convert(camel):
    for c in camel:
        if c.islower():
            print(c, end="")
        else:
            c=c.lower()
            print("_"+c, end="")



if __name__ == "__main__":
    main()
