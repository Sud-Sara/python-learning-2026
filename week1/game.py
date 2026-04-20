import random

def main():
    limit= 0

    while True:
        try:
            limit=input("Level: ")
            if not (limit.isnumeric()) or not 0<int(limit)<9999:
                pass
            else:
                break
        except:
            pass

    n=random.randint(1,int(limit))

    while True:
        try:
            guess=input("Guess: ")
            if not(guess.isnumeric()) or not (0<=int(guess)<int(limit)):
                pass
            guess=int(guess)
            if guess==n:
                print("Just right!")
                break
            elif guess>n:
                print("Too large!")
            elif 0<guess<n:
                print("Too small!")
        except:
            pass



if __name__ == "__main__":
    main()
