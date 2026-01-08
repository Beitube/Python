h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
start = h1 * 60 + m1
end = h2 * 60 + m2

while start <= end:
    h = start // 60
    m = start % 60
    if h < 10 and m < 10:
        print("0",h,":","0",m, sep = "")
    elif h < 10:
        print("0",h,":",m, sep = "")
    elif m < 10:
        print(h,":","0",m, sep = "")    
    else:
        print(h, ":", m, sep = "")
    start += 1
