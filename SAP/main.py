import sys


def get_data():
    try:
        data = []
        number = int(sys.stdin.readline().strip())
        data.append(number)
        for _ in range(number):
            data.append(sys.stdin.readline().split())
            data.append(sys.stdin.readline().split())
            data.append(int(sys.stdin.readline().strip()))
        return data
    except:
        pass

def func():
    data = get_data()
    k = 1
    for _ in range(data[0]):
        string1 = data[k][0]
        k += 1
        cheng1 = 1
        for char in string1: 
            cheng1 = cheng1 * ord(char)
        string2 = data[k][0]
        k += 1
        cheng2 = 1
        for char in string2:
            cheng2 = cheng2 * ord(char)
        if cheng1 % data[k] == cheng2 % data[k]:
            print("Yes")
        else:
            print("No")
        k = k+1


func()