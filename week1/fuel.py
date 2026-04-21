def main():
    while True:
        try:
            fuel = input("Fraction: ")
            percent = convert(fuel)
            print(gauge(percent))

            break

        except (ValueError, ZeroDivisionError,TypeError):
            pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x<0 or y<0 or x>y:
            raise ValueError()
        else:
             return int(round((x/y)*100))
    except ValueError:
            raise ValueError
    except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    try:
        if percentage>100 or percentage<0:
            raise ValueError()
        elif percentage <=1:
            return ("E")
        elif percentage>=99:
            return ("F")
        else:
            return str(percentage)+"%"
    except ValueError:
            raise ValueError


if __name__ == "__main__":
    main()
