import sys
import pyfiglet
from pyfiglet import Figlet


def main():
    figlet=Figlet()
    flist = figlet.getFonts()
    if len(sys.argv)==1 or (len(sys.argv)==3 and sys.argv[1]in ["-f", "--font"] and sys.argv[2] in flist):
        maal = input("Input: ")
        if len(sys.argv)==1:
            print(pyfiglet.figlet_format(maal))
        elif len(sys.argv)==3:
            print(pyfiglet.figlet_format(maal, font=sys.argv[2]))
    else:
        sys.exit("Invalid usage")


if __name__== "__main__":
    main()
