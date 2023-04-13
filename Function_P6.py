# Write a Python function to check whether a number falls within a given range.

def test_range(n):
    if n in range(1,20):
        print(" %s is in the range" % str(n))
    else:
        print("The number is outside the given range.")


test_range(5)
