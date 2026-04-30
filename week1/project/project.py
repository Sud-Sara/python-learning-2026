import sys
import feedparser

def main():

    print("\nHey, how are you doing!")
    print("What would you like to do today?")

    while True:
        print("\nType:")
        print("\t'News'   : For latest news Today.")
        print("\t'Sports' : To find out about sporting events today.")
        print("\t'Quote'  : For an inspirational quote.")
        print("\t'X'      : To quit the program")
       
        validate(input("\nEnter:>"))
        


def validate(s):
    if s.strip().lower() == "x":
        sys.exit("\nGoodbye, see you soon again!\n\n")
    elif s.strip().lower() == "news":
        get_news()
    elif s.strip().lower() == "sports":
        get_sports()
    elif s.strip().lower() == "quote":
        get_quote()
    else:
        return "Invalid input"


def get_news():
    url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    print("\n" + "="*70)
    print("📰 Generating latest news for you!")
    print("="*70 + "\n")
    
    for i, entry in enumerate(feed.entries[:5], 1):
        # Shorten the URL display
        short_url = entry.link[:50] + "..." if len(entry.link) > 50 else entry.link
        
        print(f"{i}. {entry.title}")
        print(f"   🔗 {short_url}\n")



def get_sports():
    print("\nLets see what games are out there today!")



def get_quote():
    print("\n Quote of the moment:")

    

if __name__ == "__main__":
    main()