

def get_square(num):
    result = num*num
    return result

for i in range(0,11,2):
    sq = get_square(i)
    print("square of ",i,"is",sq)