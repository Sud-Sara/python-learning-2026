import random


def main():
    level=get_level()
    x={}
    y={}
    score=0
    for n in range (0,10):
        x[n]=generate_integer(level)
        y[n]=generate_integer(level)

    for n in range (0,10):
        errorcounter=0
        while True:
            try:
                if x[n]+y[n]==int(input(f"{x[n]} + {y[n]} = ")):
                    score+=1
                    break
                elif errorcounter<2:
                    print("EEE")
                    errorcounter+=1
                else:
                    print("EEE")
                    print(f"{x[n]} + {y[n]} = {x[n]+y[n]}")
                    break
            except:
                pass
    print("Score: ", score)


def get_level():
    while True:
        level=input("Level: ")
        if level.isnumeric() and int(level) in [1,2,3]:
            return int(level)


def generate_integer(level):
    if not 1<=level<=3:
        raise ValueError()
    elif level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
