# print name 4 times using recursion

count = 0
def name():
    global count
    if count == 4:
        return
    print("Vivek")
    count += 1
    name()

name()

