def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length= len(s)


    if not (2<=length<=6 and s.isalnum() and s[0:2].isalpha()):
        return False

    al_after_num=False
    for c in s:
        if c.isnumeric():
            if not al_after_num and c=="0":
                return False
            al_after_num=True
        elif al_after_num:
            return False

    return True


if __name__ == "__main__":
    main()
