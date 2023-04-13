# Write a Python program to reverse a string. Go to the editor. String : "1234abcd"

def reverse(str):
    out = str[::-1]
    return out

x = reverse("1234abcd")
print(x)