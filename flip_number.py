n = input()
if len(n) == 5:
    print(int(n[::-1]))
else:
    a = n[0] + n[-1:0:-1]  
    print(int(a))
