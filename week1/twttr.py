def main():
    answer = input("Input: ").strip()
    print("Output: ", end="")
    print (f"{shorten(answer)}")



def shorten(ans):
    retans=""
    for c in ans:
        if not c in ["A","E","I","O","U","a","e","i","o","u"]:
            retans+=c
    return retans




if __name__ == "__main__":
    main()
