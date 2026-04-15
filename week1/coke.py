def main():
    due=50
    owed=0
    while due>0 :
        coin = int(input("Inset Coin: ").strip())
        if coin in [5, 10, 25]:
            due=due-coin
            owed= 0-due
            if due<=0:
                print("Change Owed:", owed)
            else:
                print("Amount Due:", due)
        else:
            print("Amount Due:", due)

if __name__ == "__main__":
    main()
