x = int(input())
y = int(input())

# test for quad 1: both positive
if (x >= 0 and y >= 0):
    print("1")
elif (x < 0 and y >= 0):
    print("2")
elif (x >= 0 and y < 0):
    print("4")
else:
    print("3")
    
