import inflect

def main():

    p=inflect.engine()
    names = []

    while True:
        try:
            item=input("Name: ").strip()
            names.append(item)

        except EOFError:
            print("\nAdieu, adieu, to", p.join(names))
            break

if __name__ == "__main__":
    main()
