# ii) Generate multiplication table up to 10 for numbers 1 to 5.

def generate_table():
    for x in range(1, 6):
        print(x,"Table")
        for y in range(1, 11):
            print(str(x)+"x"+str(y)+"="+str(x*y))
        print()


generate_table()