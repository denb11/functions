
#leight = int(input("insert numbers of line: "))
#direction = str(input("insert V or H: "))
def drawLine( leight, direction):
    if direction == str("H"):
        print("--" * leight, end = "")
    else:
        print("|\n" * leight)

drawLine(5, "V")
drawLine(5, "H")


