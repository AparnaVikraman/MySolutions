if __name__ == '__main__':
    str  =  input().strip()
    i=1
    while True:
        if i-1 >=0 and str[i-1] == str[i]:
            str1 = str[i-1:].replace(str[i], '', 2)
            str = str[:i-1] + str1
            i = i-2 if i-2 >=0 else -1
        i+=1
        if len(str) == i:
            break
    if str:
        print(str)
    else:
        print("Empty String")
