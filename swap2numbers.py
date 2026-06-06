def swap1(a,b):
    print("Before swapping: a = ", a, " b = ", b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping:  a = ", a, " b = ", b)

def swap2(a, b):
    print("Before swapping: a = ", a, " b = ", b)
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After Swapping:  a = ", a, " b = ", b)

swap1(-1,3)
swap2(2,4)