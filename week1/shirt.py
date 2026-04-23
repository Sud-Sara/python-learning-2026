import sys
from PIL import Image
from PIL import ImageOps


def main():

    rfilename, wfilename = validate_input()
    #print(rfilename, wfilename)
    blend_file(rfilename,wfilename)


def blend_file(filename, saveAs):
    table=[]
    try:
        with Image.open(filename) as img, Image.open("shirt.png") as shimg:
            img=ImageOps.fit(img, shimg.size)
            img.paste(shimg,(0,0), shimg)
            img.save(saveAs)

            #print(img.size, shimg.size)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


def validate_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].lower().endswith(".jpeg") or sys.argv[1].lower().endswith(".jpg")or sys.argv[1].lower().endswith(".png")):
        sys.exit("Invalid input file")
    elif not (sys.argv[2].lower().endswith(".jpeg") or sys.argv[2].lower().endswith(".jpg")or sys.argv[2].lower().endswith(".png")):
        sys.exit("Invalid output file")
    elif not (sys.argv[1].lower().split(".")[-1] == sys.argv[2].lower().split(".")[-1]):
        sys.exit("Input and output have different extensions")
    else:
        return sys.argv[1].lower(), sys.argv[2].lower()


if __name__ =="__main__":
    main()
