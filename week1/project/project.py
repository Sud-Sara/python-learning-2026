import sys

def main():
    print("\nHey, how are you doing!")
    print("What would you like to do today?")
    print("\nType:")
    print("\t'News'   : For latest news Today.")
    print("\t'Sports' : To find out about sporting events today.")
    print("\t'Quote'  : For an inspirational quote.")
    print("\t'X'      : To quit the program")

    while True:
        choice=(validate(input("\nEnter:>")))
        print(choice)


def validate(s):
    if s.strip().lower() == "x":
        sys.exit("\nGoodbye, see you soon again!\n\n")
    elif s.strip().lower() == "news":
        get_news()
    elif s.strip().lower() == "sports":
        get_sports()
    elif s.strip().lower() == "qoute":
        get_quote()
    else:
        return "Invalid input"


def get_news():
    print("\nGenerating latest news for you!")



def get_sports():
    print("\nLets see what games are out there today!")



def get_quote():
    print("\n Quote of the moment:")

    

if __name__ == "__main__":
    main()