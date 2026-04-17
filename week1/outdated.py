def main():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            indate=input("Date: ").title().strip()
            if "/" in indate:
                MM,DD,YYYY = [int(x) for x in indate.split("/")]
#               print(indate, MM,DD,YYYY)
                if 1<=MM<=12 and 1<=DD<=31 and 1<=YYYY<=9999:
                    print(f"{YYYY}-{MM:02}-{DD:02}")
                    break
                else:
                    pass
            elif " " in indate :
                mm,dd,yyyy = indate.split(" ")
                if not "," in dd:
                    raise ValueError()
                dd= int(dd.removesuffix(","))
                yyyy= int(yyyy)
#               print(indate, mm,dd,yyyy)
                if mm.isalpha() and mm.title() in months and 1<=dd<=31 and 1<=yyyy<=9999:
                    mm=months.index(mm)+1
                    print(f"{yyyy}-{mm:02}-{dd:02}")
                    break
                else:
                    pass
            else:
                pass
        except (ValueError):
                pass


if __name__ == "__main__":
    main()
