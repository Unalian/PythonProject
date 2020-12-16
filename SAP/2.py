import sys
def get_data():
    try:
        data = []
        data.append(list(map(int, sys.stdin.readline().split())))
        data.append(sys.stdin.readline().split())
        return data
    except:
        pass

def func():
    data = get_data()
    m = data[0][1]
    string = str(data[1][0])
    right = 0
    left = 0
    k = 0
    res = 0

    if len(string) == 0:
        print("0")
        return

    while right < len(string) and left <= right:
        if k == m:
            r, l = 0, 0
            while string[left] == 'B':
                left += 1
                l += 1
            right += 1
            r += 1
            while string[right + 1] == 'B':
                right += 1
                r += 1
            res += (l+1) * (r+1)
            right += 1
            k += 1
        else:
            if k > m:
                if left < len(string) and string[left] == 'A':
                    k -= 1
                    left += 1
                else:
                    left += 1
            else:
                right += 1
                if right<len(string) and string[right] == 'A':
                    k += 1
    print(res)













func()