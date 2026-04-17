def main():
    glist ={}
    total=0
    while True:
        try:
            item=input().upper().strip()
            if item in glist:
                glist[item] += 1

            else:
                glist[item] = 1

        except (KeyError, ValueError):
            print("Invalid input")
        except EOFError:
            for item in sorted(glist):
                print(f"{glist[item]} {item}")
            break

if __name__ == "__main__":
    main()
