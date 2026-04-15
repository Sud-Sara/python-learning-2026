def main():
    answer = input("Input: ").strip()
    print("Output: ", end="")
    convert(answer)



def convert(camel):
    for c in camel:
        if not c in ["A","E","I","O","U","a","e","i","o","u"]:
            print(c, end="")




if __name__ == "__main__":
    main()
