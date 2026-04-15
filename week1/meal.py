def main():
    answer = input("What time is it?").lower().strip()
    tim =convert(answer)
    if 6<tim<9:
        print("breakfast time")
    elif 11<tim<14:
        print("lunch time")
    elif 17<tim<20:
        print("dinner time")


def convert(time):
    hours, minutes= time.split(":")
    hours=float(hours)
    minutes= float(minutes)/60
    return hours+minutes


if __name__ == "__main__":
    main()
