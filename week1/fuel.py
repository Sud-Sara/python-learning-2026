def main():
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split("/")
            x = int(x)
            y = int(y)

            percent= int(round((x/y)*100))

            if x<0 or y<=0 or x>y:
                raise ValueError()

            if percent <=1:
                print("E")
            elif percent>=99:
                print("F")
            else:
                print(f" {percent}%")
            break

        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
