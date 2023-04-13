# Write a Python function to find the maximum of three numbers

def maximum(a,b,c,):
    if a > b:
        d = a
    else:
        d = b
    if d > c:
        print(d,"is maximum")
    else:
        print(c,"is maxiumum")

maximum(12,15,30)