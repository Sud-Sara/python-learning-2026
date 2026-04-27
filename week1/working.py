import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except:
        sys.exit("Invalid input")

def convert(s):

    pattern = r"^(?P<startH>[0-9]{1,2})(:(?P<startM>[0-9]{2}))? (?P<startAPM>AM|PM) to (?P<endH>[0-9]{1,2})(:(?P<endM>[0-9]{2}))? (?P<endAPM>AM|PM)$"
    restr=""

    if matches := re.match(pattern, s):
        if not (1<=int(matches.group("startH"))<=12 or 1<=int(matches.group("endH"))<=12):
            raise ValueError
        elif (matches.group("startM") and not 0<=int(matches.group("startM"))<=59):
            raise ValueError
        elif (matches.group("endM") and not 0<=int(matches.group("endM"))<=59):
            raise ValueError
        else:
            # converting and adding startH
            if matches.group("startAPM")=="AM":
                if 1<=int(matches.group("startH"))<=9:
                    restr="0"+matches.group("startH")
                elif int(matches.group("startH"))==12:
                    restr="00"
                else:
                    restr=matches.group("startH")
            elif matches.group("startAPM")=="PM" and int(matches.group("startH"))==12:
                restr= matches.group("startH")
            else:
                restr= str(int(matches.group("startH"))+12)

            # converting and adding startM
            if matches.group("startM"):
                restr+= ":"+ matches.group("startM")
            else:
                restr+= ":00"

            # adding -to-
            restr+=" to "

            if matches.group("endAPM")=="AM":
                if 1<=int(matches.group("endH"))<=9:
                    restr+="0"+matches.group("endH")
                elif int(matches.group("endH"))==12:
                    restr+="00"
                else:
                    restr+=matches.group("endH")
            elif matches.group("endAPM")=="PM" and int(matches.group("endH"))==12:
                restr+= matches.group("endH")
            else:
                restr+= str(int(matches.group("endH"))+12)


            if matches.group("endM"):
                restr+= ":"+ matches.group("endM")
            else:
                restr+= ":00"


          #  restr=(matches.group("startH") + matches.group("startM") + matches.group("endH") + matches.group("endM"))
        return restr
    else:
        raise ValueError("Invalid input")


...


if __name__ == "__main__":
    main()
